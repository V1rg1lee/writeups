import tls_client

session = tls_client.Session(
    client_identifier="chrome_131",
    random_tls_extension_order=True,
    debug=True
)

response = session.get(
    "https://passwordless_authentication.challenges.cybersecuritychallenge.be/",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://passwordless_authentication.challenges.cybersecuritychallenge.be/",
        "Cookie": "session=123456",
    },
    insecure_skip_verify=True
)

print("Status Code:", response.status_code)
print("Response:", response.text)
