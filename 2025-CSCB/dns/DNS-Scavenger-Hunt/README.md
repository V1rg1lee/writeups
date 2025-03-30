# Challenge description

I sat up high, then took a dive,
Yet my message must survive.
Scrambled words, locked up tight,
Hidden well, out of sight.
A secret path, a site to see,
Find my letter at justnuisance.be!
Who am I?

(Note: You need to use the DNS server specified below.)

The server is listening on
dig @dns_scavenger_hunt.challenges.cybersecuritychallenge.be -p 53

# Soluce

We started by accessing the DNS server:

```sh
┌──(kali㉿kali)-[~/Downloads]
└─$ dig @dns_scavenger_hunt.challenges.cybersecuritychallenge.be -p 53 justnuisance.be ANY


; <<>> DiG 9.20.2-1-Debian <<>> @dns_scavenger_hunt.challenges.cybersecuritychallenge.be -p 53 justnuisance.be ANY
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 7918
;; flags: qr aa rd; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;justnuisance.be.               IN      ANY

;; ANSWER SECTION:
justnuisance.be.        86400   IN      SOA     ns1.justnuisance.be. what.about.txt. 17 3600 1800 2419200 600
justnuisance.be.        86400   IN      NS      ns1.justnuisance.be.
justnuisance.be.        86400   IN      TXT     "_submission._tcp"
justnuisance.be.        86400   IN      A       10.5.0.5

;; Query time: 32 msec
;; SERVER: 52.30.164.99#53(dns_scavenger_hunt.challenges.cybersecuritychallenge.be) (TCP)
;; WHEN: Fri Mar 14 20:21:25 EDT 2025
;; MSG SIZE  rcvd: 157
```

We can see differents things in the answer section:
- The server is `ns1.justnuisance.be`
- The server is listening on the port `submission`
- The IP address of the server is `52.30.164.99`

We will try to have mor informations about `_submission._tcp` with a SRV request:

```sh
┌──(kali㉿kali)-[~/Downloads]
└─$ dig @dns_scavenger_hunt.challenges.cybersecuritychallenge.be -p 53 SRV _submission._tcp.justnuisance.be


; <<>> DiG 9.20.2-1-Debian <<>> @dns_scavenger_hunt.challenges.cybersecuritychallenge.be -p 53 SRV _submission._tcp.justnuisance.be
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 33658
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;_submission._tcp.justnuisance.be. IN   SRV

;; ANSWER SECTION:
_submission._tcp.justnuisance.be. 86400 IN SRV  0 1 666 mail.justnuisance.be.

;; Query time: 32 msec
;; SERVER: 52.30.164.99#53(dns_scavenger_hunt.challenges.cybersecuritychallenge.be) (UDP)
;; WHEN: Fri Mar 14 20:34:49 EDT 2025
;; MSG SIZE  rcvd: 101
```

There is a mail server `mail.justnuisance.be` listening on the port `666`. We will try to find the mail server with a A request:

```sh
┌──(kali㉿kali)-[~/Downloads]
└─$ dig @dns_scavenger_hunt.challenges.cybersecuritychallenge.be -p 53 A mail.justnuisance.be


; <<>> DiG 9.20.2-1-Debian <<>> @dns_scavenger_hunt.challenges.cybersecuritychallenge.be -p 53 A mail.justnuisance.be
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 34522
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;mail.justnuisance.be.          IN      A

;; ANSWER SECTION:
mail.justnuisance.be.   86400   IN      A       10.5.0.8

;; Query time: 28 msec
;; SERVER: 52.30.164.99#53(dns_scavenger_hunt.challenges.cybersecuritychallenge.be) (UDP)
;; WHEN: Fri Mar 14 20:35:59 EDT 2025
;; MSG SIZE  rcvd: 65
```

We find a local address `10.5.0.8`. But remember, we have the address of the server `52.30.164.99`. We will try to connect to the server with the port `666`:

```sh
┌──(kali㉿kali)-[~]
└─$ nc 52.30.164.99 666

220 mail.juistnuisance.be CSC ESMTP You had me at EHLO
EHLO
530 5.7.0-let's switch to a secure line
250-SIZE 0
250-STARTTLS
250 ENHANCEDSTATUSCODES
```

So we need to switch to a secure line. We will use openssl with `-starttls` argument:

```sh
┌──(kali㉿kali)-[~]
└─$ openssl s_client -connect 52.30.164.99:666 -starttls smtp

Connecting to 52.30.164.99
CONNECTED(00000003)
Didn't find STARTTLS in server response, trying anyway...
Can't use SSL_get_servername
depth=0 C=BE, ST=Vlaams-Brabant, L=Leuven, O=DNS Belgium VZW, CN=mail.juistnuisance.be
verify error:num=18:self-signed certificate
verify return:1
depth=0 C=BE, ST=Vlaams-Brabant, L=Leuven, O=DNS Belgium VZW, CN=mail.juistnuisance.be
verify return:1
---
Certificate chain
 0 s:C=BE, ST=Vlaams-Brabant, L=Leuven, O=DNS Belgium VZW, CN=mail.juistnuisance.be
   i:C=BE, ST=Vlaams-Brabant, L=Leuven, O=DNS Belgium VZW, CN=mail.juistnuisance.be
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA256
   v:NotBefore: Jan 23 19:27:29 2025 GMT; NotAfter: Oct 21 19:27:29 2027 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDkTCCAnmgAwIBAgIUTBUVRNVsKFQL5EVOzpeShBEr2IowDQYJKoZIhvcNAQEL
BQAwcTELMAkGA1UEBhMCQkUxFzAVBgNVBAgMDlZsYWFtcy1CcmFiYW50MQ8wDQYD
VQQHDAZMZXV2ZW4xGDAWBgNVBAoMD0ROUyBCZWxnaXVtIFZaVzEeMBwGA1UEAwwV
bWFpbC5qdWlzdG51aXNhbmNlLmJlMB4XDTI1MDEyMzE5MjcyOVoXDTI3MTAyMTE5
MjcyOVowcTELMAkGA1UEBhMCQkUxFzAVBgNVBAgMDlZsYWFtcy1CcmFiYW50MQ8w
DQYDVQQHDAZMZXV2ZW4xGDAWBgNVBAoMD0ROUyBCZWxnaXVtIFZaVzEeMBwGA1UE
AwwVbWFpbC5qdWlzdG51aXNhbmNlLmJlMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A
MIIBCgKCAQEA1M5hE70nJfKoQpFRKY4dbMiPQ2kkMcLxAmmesa3q/arbHyi8i6DP
V8kaDoJz59ee/dUDtUntqSJg4mvygoToJ9oIks+a3zoBF8iEToNdYOkmeA5iB7BF
jTOo38wWXEEnno+umNDVZ18+4cUiB9cf6rJ+8dSpBrOhzmHZUgQKG+kIdeWbaqzn
ITVinf0hpG76jiboGPZimWdc8P42kAd5GEVg7jBpLacbvwFu5McdDdLznurtIIFY
XGX6s7e1S//PW6/mtiI+jgV+JkQKFGXWSo8sYdoAFl7VoznZ6LXg3D6hqdFY7H0H
2uXkM/8vB7uFpYtaNRemfMX2ypacZfbEXwIDAQABoyEwHzAdBgNVHQ4EFgQUbhyd
6bvGwSCRserbJ3C20JUS9+QwDQYJKoZIhvcNAQELBQADggEBAFb8/RTqfKTZ8LF2
RXXQraaRn/4gyLqp+miGJHXwgedQ6xI0ZW8WDfiUpi2U8xqjXaE7pAEGm+TSBDDJ
oBF0yYz+lXCjN6pC1tArf7jz6lUrzEdnQiVKOklM0wCHZvt/fH3AQySiMJh2zXom
6o+tpXQ8O6SQ2/IkmeWMy+t9I1y2jqaezvjSM5l7f/LxFOaYrRFwZhZwcaYtRXHE
e67iprkIdVnx5kszvXi1GSY0idDGtgt3BvkivNMnkkrH67InH0tMSxEc0Kviyo/N
mv2tlLay/Z+iXEi88wWyn67psUVty1Q2EEM12S5Zs9L/qVXEKJCGUOgVPfm63f+o
hSMP7XI=
-----END CERTIFICATE-----
subject=C=BE, ST=Vlaams-Brabant, L=Leuven, O=DNS Belgium VZW, CN=mail.juistnuisance.be
issuer=C=BE, ST=Vlaams-Brabant, L=Leuven, O=DNS Belgium VZW, CN=mail.juistnuisance.be
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1635 bytes and written 535 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_128_GCM_SHA256
Protocol: TLSv1.3
Server public key is 2048 bit
This TLS version forbids renegotiation.
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
530 5.7.0-let's switch to a secure line
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_128_GCM_SHA256
    Session-ID: F841E238E81553A2F8A9ADA222CDC2D52CDEEDE1985F0408C37979D1F85954E7
    Session-ID-ctx: 
    Resumption PSK: 1004B819F7723440186389C69A722846415BFC05F3FCA723ED46F86E538BE79F
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 604800 (seconds)
    TLS session ticket:
    0000 - 96 a9 1c 42 6c 1c bc 99-40 2e 77 20 f4 3d 60 51   ...Bl...@.w .=Q
    0010 - 6f 89 0f 91 0d 4f 74 60-87 f8 aa ed 9b 20 f1 70   o....Ot..... .p
    0020 - 83 76 91 1c 8c 50 8b c2-ba b8 56 dc f9 49 45 45   .v...P....V..IEE
    0030 - 54 3c 2e ee 0f 61 8c 3d-17 82 0a 62 42 08 a2 c6   T<...a.=...bB...
    0040 - a4 69 e4 c2 fd 6e e8 fc-45 f0 85 91 8a c7 e0 88   .i...n..E.......
    0050 - c5 43 63 df 2a 53 85 34-8e e7 75 24 db 9b 8d b2   .Cc.*S.4..u$....
    0060 - ad 37 00 cf 26 a0 24 0f-8a                        .7..&.$..

    Start Time: 1742049905
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
```

So we will send a mail:

```sh
┌──(kali㉿kali)-[~]
└─$ openssl s_client -connect 52.30.164.99:666 -starttls smtp -quiet -crlf
Connecting to 52.30.164.99
Didn't find STARTTLS in server response, trying anyway ..
Can't use SSL_get_servername
depth=0 C=BE, ST=Vlaams-Brabant, L=Leuven, O=DNS Belgium VZW, CN=mail.juistnuisance.be
verify error:num=18:self-signed certificate
verify return:1
depth=0 C=BE, ST=Vlaams-Brabant, L=Leuven, O=DNS Belgium VZW, CN=mail.juistnuisance.be
verify return:1
530 5.7.0-Let's switch to a secure line
mail from:<mail.juistnuisance.be>
250 2.1.0 Ok
rcpt to:<virgile.devolder@gmail.com>
250 2.1.5 Ok
data
354 Start mail input; end with <CR><LF>.<CR><LF>
Hello, You
250 2.0.0 Ok: queued. You passed the test, the flag is hidden in the DANE (TLSA) record for this mail submission server
```

It responds with:

```
250 2.0.0 Ok: queued. You passed the test, the flag is hidden in the DANE (TLSA) record for this mail submission server
```

We will try to get the DANE record with a TLSA request (if you want to understand TLSA, [click here](https://www.cloudns.net/wiki/article/342/)):

```sh
┌──(kali㉿kali)-[~]
└─$ dig @dns_scavenger_hunt.challenges.cybersecuritychallenge.be -p 53 TLSA _666._tcp.mail.justnuisance.be 

; <<>> DiG 9.20.2-1-Debian <<>> @dns_scavenger_hunt.challenges.cybersecuritychallenge.be -p 53 TLSA _666._tcp.mail.justnuisance.be
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 33741
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;_666._tcp.mail.justnuisance.be.        IN      TLSA

;; ANSWER SECTION:
_666._tcp.mail.justnuisance.be. 86400 IN TLSA   3 1 1 4353437B53633476336E36335F376831735F444E355F5337796C337D

;; Query time: 32 msec
;; SERVER: 52.30.164.99#53(dns_scavenger_hunt.challenges.cybersecuritychallenge.be) (UDP)
;; WHEN: Sat Mar 15 12:34:13 EDT 2025
;; MSG SIZE  rcvd: 102
```

There is a TLSA record with the value `4353437B53633476336E36335F376831735F444E355F5337796C337D`. We will decode it:

```sh                            
┌──(kali㉿kali)-[~]
└─$ echo "4353437B53633476336E36335F376831735F444E355F5337796C337D" | xxd -r -p
```

So the flag is `CSC{Sc4v3n63_7h1s_DN5_S7yl3}`.