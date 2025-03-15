# Challenge description

Only whitelisted clients are allowed to connect to the web server!
Read the source code of the server and send the correct fingerprints.

# Soluce

### **Analyse of server (`server.go`)**
By analyzing `server.go`, we see that the server **verifies four main elements** in incoming requests:
1. **User-Agent** → Must be `Chrome 131.0.0.0`
2. **JA4 fingerprint** → Must match the **expected value stored in the server**
3. **JA4H_a fingerprint** → Must match the **expected value stored in the server**
4. **HTTP/2 fingerprint** → Must match the **expected value stored in the server**

If **any of these values are incorrect**, the server returns **`403 Forbidden`**.

---

### **Spoofing the Correct Fingerprints**
To **bypass these checks**, we need to send a request that perfectly matches the server's expected values.

**Manually crafting a request with the exact TLS parameters is difficult**, but there is a Python library that allows us to **simulate a browser with a specific TLS configuration**: [`tls-client`](https://github.com/FlorianREGAZ/tls-client).

With [this script](passwordless_authentication.py), we were able to send a request **matching all required fingerprints**.

---

### **Running the Exploit**
```bash
┌──(.venv)─(kali㉿kali)-[~/Downloads/challenge_files_passwordless_authentication]
└─$ uv run python passwordless_authentication.py
raw request bytes sent over wire: 429 (0 kb)
headers on request:
map[Accept:[*/*] Accept-Encoding:[gzip, deflate, br] Accept-Language:[en-US,en;q=0.5] Connection:[keep-alive] Cookie:[session=123456] Header-Order::[] Referer:[https://passwordless_authentication.challenges.cybersecuritychallenge.be/] User-Agent:[Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36]]
cookies on request:
[session=123456]
headers on response:
map[Content-Length:[30] Content-Type:[text/plain; charset=utf-8] Date:[Sat, 15 Mar 2025 17:11:32 GMT]]
cookies on response:
[]
requested https://passwordless_authentication.challenges.cybersecuritychallenge.be/ : status 200
response body payload: CSC{y0uf0und4llmyf1n63rpr1n75}
raw response bytes received over wire: 97 (0 kb)
get cookies for url: https://passwordless_authentication.challenges.cybersecuritychallenge.be/
Status Code: 200
Response: CSC{y0uf0und4llmyf1n63rpr1n75}
```