class LumiIDError(Exception):
    def __init__(self, message: str, status_code: int = None, response: dict = None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response

class AuthenticationError(LumiIDError):
    """Raised when the API key is invalid or missing."""

class ValidationError(LumiIDError):
    """Raised when the API rejects input data."""

class RateLimitError(LumiIDError):
    """Raised when you've exceeded your API quota.""" 
