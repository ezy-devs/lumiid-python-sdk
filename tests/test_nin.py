 
import responses
import pytest
from lumiid import LumiID, LumiIDError

@responses.activate
def test_verify_nin_success():
    responses.add(
        responses.POST,
        "https://api.lumiid.com/v1/ng/nin-basic/",
        json={"nin": "12345678901", "first_name": "JOHN", "last_name": "DOE"},
        status=200,
    )
    client = LumiID(api_key="test_key")
    result = client.verify_nin_basic("12345678901")
    assert result["first_name"] == "JOHN"

def test_invalid_nin_raises():
    client = LumiID(api_key="test_key")
    with pytest.raises(ValueError):
        client.verify_nin_basic("123")  # too short