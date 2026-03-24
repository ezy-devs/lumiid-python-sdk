from lumiid import LumiID, LumiIDError, AuthenticationError

client = LumiID(api_key="your_api_key_here")

try:
    result = client.verify(id_type="CAC", id_number="RC1234567")
    print("Success:", result)
except AuthenticationError:
    print("Bad API key")
except LumiIDError as e:
    print(f"Status code: {e.status_code}")
    print(f"Full response: {e.response}")  # <-- this will show the real error message
except ValueError as e:
    print(f"Validation Error: {e}")