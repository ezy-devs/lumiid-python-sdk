import responses
import pytest
from lumiid import LumiID, LumiIDError

@responses.activate
def test_verify_nin_success():
    responses.add(
        responses.POST,
        "https://api.lumiid.com/v1/ng/nin-basic/",
        json={"nin": "12345678901"},
        status=200,
    )
    client = LumiID(api_key="test_key")
    result = client.verify(id_type="NIN", id_number="12345678901")

@responses.activate
def test_verify_nin_advance_success():
    responses.add(
        responses.POST,
        "https://api.lumiid.com/v1/ng/nin-premium/",
        json={"nin": "12345678901"},
        status=200,
    )
    client = LumiID(api_key="test_key")
    result = client.verify(id_type="NIN", id_number="12345678901", advance=True)

def test_invalid_nin_raises():
    client = LumiID(api_key="test_key")
    with pytest.raises(ValueError):
        client.verify(id_type="NIN", id_number="123")  # too short

def test_unsupported_id_type_raises():
    client = LumiID(api_key="test_key")
    with pytest.raises(LumiIDError):
        client.verify(id_type="PASSPORT", id_number="12345678901")

def test_missing_api_key_raises():
    with pytest.raises(ValueError):
        LumiID(api_key="")