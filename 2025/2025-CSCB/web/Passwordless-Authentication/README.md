# Challenge description

Only whitelisted clients are allowed to connect to the web server!
Read the source code of the server and send the correct fingerprints.

# Soluce

When we open the website, it says that we are not allowed to access the website. We need to find a way to bypass the server's checks.

Here is the code of the server:

```go
package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"

	"github.com/wi1dcard/fingerproxy/pkg/metadata"
)

func flagServer(w http.ResponseWriter, req *http.Request) {
	// JA4_r = t13d1516h2_002f,0035,009c,009d,1301,1302,1303,c013,c014,c02b,c02c,c02f,c030,cca8,cca9_0005,000a,000b,000d,0012,0017,001b,0023,002b,002d,0033,4469,fe0d,ff01_0403,0804,0401,0503,0805,0501,0806,0601
	// JA4_ro = t13d1516h2_c030,1302,002f,009d,c014,1301,0035,1303,009c,c013,cca8,c02b,cca9,c02f,c02c_000b,001b,000d,002d,002b,0033,0012,0017,ff01,4469,0005,fe0d,000a,0023,0010,0000_0403,0804,0401,0503,0805,0501,0806,0601
	// JA4_o = t13d1516h2_c20d6050442c_97f7806fcdbe
	ja4FpToFind := "t13d1516h2_8daaf6152771_02713d6af862"
	ja4hFpToFindFirstCut := "ge20cr05enus"
	http2FpToFind := "1:65536;2:0;4:6291456;6:262144|15663105|1:1:0:256|m,a,s,p"
	userAgentToFind := "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

	_, verbosePresent := os.LookupEnv("VERBOSE")

	if verbosePresent {
		fmt.Printf("[client %s]", req.RemoteAddr)
	}

	data, ok := metadata.FromContext(req.Context())
	if !ok {
		if verbosePresent {
			fmt.Printf("failed to get context\n")
		}
		http.Error(w, "failed to get context", http.StatusInternalServerError)
		return
	}

	ja3Fp, err := fingerprintJA3(data)

	if err != nil {
		if verbosePresent {
			fmt.Printf("%s", err.Error())
		}
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	ja4Fp, err := fingerprintJA4(data)

	if err != nil {
		if verbosePresent {
			fmt.Printf("%s", err.Error())
		}
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	http2Fp := fingerprintHTTP2(data)

	JA4H_a := fingerprintJA4H_a(req)

	if verbosePresent {
		detail, _ := json.Marshal(data)
		fmt.Printf("detail: %s", detail)
		fmt.Printf("User-Agent: %s\n", req.UserAgent())
		fmt.Printf("JA3 fingerprint: %s\n", ja3Fp)
		fmt.Printf("JA4 fingerprint: %s\n", ja4Fp)
		fmt.Printf("HTTP2 fingerprint: %s\n", http2Fp)
		fmt.Printf("JA4H_a fingerprint: %s\n", JA4H_a)
	}

	if ja4Fp == ja4FpToFind && JA4H_a == ja4hFpToFindFirstCut &&
		http2Fp == http2FpToFind && req.UserAgent() == userAgentToFind {
		w.WriteHeader(http.StatusOK)
		fmt.Fprintf(w, "%s", getEnv("FLAG", "NFL{THIS_IS_NOT_THE_REAL_FLAG__EXPLOIT_THE_SERVER}"))
		return
	} else {
		w.WriteHeader(http.StatusForbidden)
		fmt.Fprintf(w, "Access denied")
		return
	}
}
```

### **Analyse of server (`server.go`)**
By analyzing `server.go`, we see that the server **verifies four main elements** in incoming requests:
1. **User-Agent** → Must be `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36`
2. **JA4 fingerprint** → Must match: `t13d1516h2_8daaf6152771_02713d6af862`
3. **JA4H_a fingerprint** → Must match: `ge20cr05enus`
4. **HTTP/2 fingerprint** → Must match: `1:65536;2:0;4:6291456;6:262144|15663105|1:1:0:256|m,a,s,p`

If **any of these values are incorrect**, the server returns **`403 Forbidden`**.

So we need to send a request like a Chrome 131 browser on Windows 10, with the correct fingerprints.
---

### **Spoofing the Correct Fingerprints**
To **bypass these checks**, we need to send a request that perfectly matches the server's expected values.

**Manually crafting a request with the exact TLS parameters is difficult**, but there is a Python library that allows us to **simulate a browser with a specific TLS configuration**: [`tls-client`](https://github.com/FlorianREGAZ/Python-Tls-Client).

With [this script](code/passwordless_authentication.py), we were able to send a request **matching all required fingerprints**.

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

So the flag is `CSC{y0uf0und4llmyf1n63rpr1n75}`.