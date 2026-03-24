# LumiID Python SDK

Python SDK for the [LumiID](https://lumiid.com) Identity Verification API.

## Installation

pip install lumiid

## Usage

from lumiid import LumiID

client = LumiID(api_key="your_api_key")
result = client.verify_nin_basic("12345678901")
print(result)

## Errors

from lumiid import LumiIDError, AuthenticationError

try:
    result = client.verify_nin_basic("12345678901")
except AuthenticationError:
    print("Invalid API key")
except LumiIDError as e:
    print(f"Error {e.status_code}: {e}") 
