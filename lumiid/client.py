import requests
from typing import Optional
from .exceptions import LumiIDError, AuthenticationError, ValidationError, RateLimitError

class LumiID:
    BASE_URL = "https://api.lumiid.com/v1"
    SUPPORTED_ID_TYPES = {"NIN", "BVN", "CAC", "TIN", "NUBAN"}

    def __init__(self, api_key: str, timeout: int = 30):
        if not api_key:
            raise ValueError("api_key is required.")
        self.api_key = api_key
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

    def _post(self, endpoint: str, payload: dict) -> dict:
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = self.session.post(url, json=payload, timeout=self.timeout)
        except requests.exceptions.Timeout:
            raise LumiIDError("Request timed out.")
        except requests.exceptions.ConnectionError:
            raise LumiIDError("Failed to connect to LumiID API.")

        data = response.json()

        if response.status_code == 401:
            raise AuthenticationError("Invalid or missing API key.", status_code=401, response=data)
        if response.status_code == 422:
            raise ValidationError(data.get("message", "Validation error."), status_code=422, response=data)
        if response.status_code == 429:
            raise RateLimitError("API rate limit exceeded.", status_code=429, response=data)
        if not response.ok:
            raise LumiIDError(data.get("message", "Unknown error."), status_code=response.status_code, response=data)

        return data
    
    def verify(self, id_type: str, id_number: str, advance: bool = False) -> dict:
        if id_type not in self.SUPPORTED_ID_TYPES:
            raise LumiIDError(
                f"Unsupported ID type '{id_type}'. Supported: {self.SUPPORTED_ID_TYPES}"
            )
        try:
            if id_type == "NIN":
                if advance:
                    return self._verify_nin_advance(id_number)
                return self._verify_nin_basic(id_number)

            elif id_type == "CAC":
                if advance:
                    return self._verify_advance_cac(id_number)
                return self._verify_basic_cac(id_number)

            elif id_type == "BVN":
                if advance:
                    return self._verify_advance_bvn(id_number)
                return self._verify_basic_bvn(id_number)

            elif id_type == "TIN":
                return self._verify_tin(id_number)

            elif id_type == "NUBAN":
                return self._verify_nuban(id_number)

        except LumiIDError:
            raise
        except ValueError:
            raise
        except Exception as e:
            raise LumiIDError(f"Unexpected error: {str(e)}")
            
    def _validate_nin(self, id_number: str) -> str:
        id_number = id_number.strip()
        if not id_number.isdigit() or len(id_number) != 11:
            raise ValueError(f"NIN must be exactly 11 digits, got: '{id_number}'")
        return id_number
    def _validate_cac(self, id_number: str) -> str:
        id_number = id_number.strip()
        if not id_number.isalnum() or len(id_number) < 6:
            raise ValueError(f"CAC number must be alphanumeric and at least 6 characters, got: '{id_number}'")
        return id_number

    def _verify_nin_basic(self, id_number: str) -> dict:
        id_number = self._validate_nin(id_number)
        return self._post("/ng/nin-basic/", {"nin": id_number})

    def _verify_nin_advance(self, id_number: str) -> dict:
        id_number = self._validate_nin(id_number)
        return self._post("/ng/nin-premium/", {"nin": id_number})
    
    def _verify_basic_bvn(self, id_number: str) -> dict:
        id_number = id_number.strip()
        if not id_number.isdigit() or len(id_number) != 11:
            raise ValueError(f"BVN must be exactly 11 digits, got: '{id_number}'")
        return self._post("/ng/bvn-basic/", {"id_number": id_number})
    
    def _verify_advance_bvn(self, id_number: str) -> dict:
        id_number = id_number.strip()
        if not id_number.isdigit() or len(id_number) != 11:
            raise ValueError(f"BVN must be exactly 11 digits, got: '{id_number}'")
        return self._post("/ng/bvn-premium/", {"id_number": id_number})
    
    def _verify_basic_cac(self, id_number: str) -> dict:
        id_number = self._validate_cac(id_number)
        return self._post("/ng/cac-basic/", {"rc_number": id_number})

    def _verify_advance_cac(self, id_number: str) -> dict:
        id_number = self._validate_cac(id_number)
        return self._post("/ng/cac-premium/", {"rc_number": id_number})
    
    def _verify_tin(self, id_number: str) -> dict:
        id_number = id_number.strip()
        if not id_number.isdigit() or len(id_number) < 6:
            raise ValueError(f"TIN must be numeric and at least 6 characters, got: '{id_number}'")
        return self._post("/ng/tin-basic/", {"tin": id_number})
    
    def _verify_nuban(self, id_number: str) -> dict:
        id_number = id_number.strip()
        if not id_number.isdigit() or len(id_number) != 10:
            raise ValueError(f"NUBAN must be exactly 10 digits, got: '{id_number}'")
        return self._post("/ng/nuban-basic/", {"nuban": id_number})
