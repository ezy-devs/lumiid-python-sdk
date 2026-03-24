# LumiID Python SDK

A clean, simple Python SDK for the [LumiID](https://lumiid.com) Identity Verification API. Supports NIN, BVN, CAC, TIN, and NUBAN verification for Nigeria.

---

## Installation

```bash
pip install lumiid
```

---

## Quick Start

```python
from lumiid import LumiID

client = LumiID(api_key="your_api_key_here")

result = client.verify(id_type="NIN", id_number="12345678901")
print(result)
```

---

## Authentication

Get your API key from your [LumiID dashboard](https://lumiid.com). Pass it when creating the client:

```python
from lumiid import LumiID

client = LumiID(api_key="your_api_key_here")
```

We recommend storing your API key in an environment variable rather than hardcoding it:

```python
import os
from lumiid import LumiID

client = LumiID(api_key=os.getenv("LUMIID_API_KEY"))
```

---

## Usage

### NIN — National Identification Number

```python
# Basic verification
result = client.verify(id_type="NIN", id_number="12345678901")
print(result)

# Advanced/premium verification
result = client.verify(id_type="NIN", id_number="12345678901", advance=True)
print(result)
```

---

### BVN — Bank Verification Number

```python
# Basic verification
result = client.verify(id_type="BVN", id_number="12345678901")
print(result)

# Advanced/premium verification
result = client.verify(id_type="BVN", id_number="12345678901", advance=True)
print(result)
```

---

### CAC — Corporate Affairs Commission

```python
# Basic verification
result = client.verify(id_type="CAC", id_number="RC1234567")
print(result)

# Advanced/premium verification
result = client.verify(id_type="CAC", id_number="RC1234567", advance=True)
print(result)
```

---

### TIN — Tax Identification Number

```python
result = client.verify(id_type="TIN", id_number="12345678-0001")
print(result)
```

---

### NUBAN — Nigerian Uniform Bank Account Number

```python
result = client.verify(id_type="NUBAN", id_number="1234567890")
print(result)
```

---

## Error Handling

The SDK raises specific exceptions so you can handle each case precisely:

```python
from lumiid import (
    LumiID,
    LumiIDError,
    AuthenticationError,
    ValidationError,
    RateLimitError,
)

client = LumiID(api_key=os.getenv("LUMIID_API_KEY"))

try:
    result = client.verify(id_type="NIN", id_number="12345678901")
    print(result)

except AuthenticationError:
    # Invalid or missing API key
    print("Check your API key.")

except ValidationError as e:
    # API rejected the input data
    print(f"Validation failed: {e}")

except RateLimitError:
    # You have exceeded your API quota
    print("Rate limit exceeded. Check your LumiID wallet balance.")

except LumiIDError as e:
    # General API or network error
    print(f"API error {e.status_code}: {e}")
    print(f"Full response: {e.response}")

except ValueError as e:
    # Invalid input format e.g. NIN is not 11 digits
    print(f"Invalid input: {e}")
```

---

## Supported ID Types

| ID Type | Description | Supports `advance` |
|---------|-------------|-------------------|
| `NIN` | National Identification Number | ✅ |
| `BVN` | Bank Verification Number | ✅ |
| `CAC` | Corporate Affairs Commission | ✅ |
| `TIN` | Tax Identification Number | ❌ |
| `NUBAN` | Nigerian Uniform Bank Account Number | ❌ |

---

## Configuration

You can customize the request timeout (default is 30 seconds):

```python
client = LumiID(api_key="your_api_key_here", timeout=60)
```

---

## Requirements

- Python 3.8+
- `requests >= 2.28.0`

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/add-passport-verification`)
3. Commit your changes (`git commit -m 'feat: add passport verification'`)
4. Push to the branch (`git push origin feature/add-passport-verification`)
5. Open a Pull Request

---

## License

[MIT](LICENSE)

---

## Links

- [PyPI](https://pypi.org/project/lumiid/)
- [GitHub](https://github.com/ezy-devs/lumiid-python-sdk)
- [LumiID API](https://lumiid.com)