# Challenge description

We've retrieved a set of AWS credentials from one of Cipher's soldiers. He told us they could be used to access an S3 bucket called "secret-messages" on us-west-2. We tried accessing the bucket but can't figure out what to do with its contents. Help us retrieve the secret message.

# Soluce

We start by configuring the AWS CLI with the provided credentials:

```sh
export AWS_ACCESS_KEY_ID="REDACTED"
export AWS_SECRET_ACCESS_KEY="REDACTED"
export AWS_DEFAULT_REGION="REDACTED"
```

We can now list the contents of the "secret-messages" bucket:

```sh
┌──(virgile㉿localhost)-[~/Téléchargements]
└─$ aws s3 ls s3://secret-messages/                                                                                                                                                                                                        
2025-03-17 10:27:53       1510 20250301.msg.enc
```

Now we can download the encrypted message:

```sh
aws s3 cp s3://secret-messages/20250301.msg.enc .
```

We analyze the file:

```sh
┌──(virgile㉿localhost)-[~/Téléchargements]
└─$ file 20250301.msg.enc                                                                                                                                                                                                                  
20250301.msg.enc: JSON text data

┌──(virgile㉿localhost)-[~/Téléchargements]
└─$ cat 20250301.msg.enc                                                                                                                                                                                                                   
{
    "CiphertextBlob": "AQICAHiRefyqdd9pxM2Aq1I0DJhHPH2ySQ1xLKMiWr9h8LHTjwHUJLxfxuK9KK+SPLYApHM2AAADsTCCA60GCSqGSIb3DQEHBqCCA54wggOaAgEAMIIDkwYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAytaKub7KcmaE79aAgCARCAggNkvNoABrJ009jrn+j065jaUP7ABSahYUWVCtYVKoTAmlfh01L7szyf6pEn/yz09iq2LLcu9ndGT6DHEL/Ctzw7MB/5QFr0eWUYGxASZm79JvCH1bSwQR7XeNHQDHjdGg1X6LJO8GwyihEfGzs7XOdtFysWXHTEK3nBphQy0GDmPNMUg27Jhayk4jSL4c3ezk0GX21YelNWNExJmOQMPkPjErlPt/0oK7DGmLd3qwcc/X6iIxeW4CsAx4zIP3hQVOSFrUfZNuGNr/4JSH3ZhgxJRbB0DUk3ibaM4uQxGs2wi1N1zG1fjd86d7a9Rk29Zk+7m8EOtboDGf6rSVNXh/VMjeKFFmsIzQiiA2Z8FixDW530qgFFiUmOuuTJaVbS70ktXXYJcOsW6cfl2n45BxMcgDGuSGQSORHddijJY3o/7Si0MadR7dM3SNkxTT6HoRu0/5Rr2vVd8VBEU6bLCacWoWhLA18poYO9oI+Q1SaPmK+1zPL51ZBYvEcZ2jQov1olEcm/lpym1+HpAOdO9RLvTDjhnpT7/4+AVbkB2yhIdZvRk3x0GNMCtyNw76PpN4UH+CegZ7QTvXO7B5iLKWmb8Zdx9sRI4e0QzmpxPlCEiGCXotsQ+jW/sDcrrbwbEw+3XKtuge2+NRUhIWoG7++yWELf+SPheMEJ4RH+Ikz6rl0Z4J/BtN9eefiP62gEV2eY+RkJXh3Ox41S/P0yiiNh/t62Gq8SPgvEeCF6lwRA3gGchjI86mJdmUdhG1mFf+8/FDRCJ7mi1AoEOXVUJyNh9+MaOPp7fhwxYG/ZQZ2Mx51UX3nYCbU2aa4FUWMEM6I83ZEnxKV4qVyTTRV5PkZx3B7r1heJVsV9zi01OZBPPY1yyW6Xr+Pvmegv6k8PYFO88TcFDiaAlA1ZtTRPFfZ8fEiNysx6t1WAKSTim7SmyHDNoPJvFSUZhosoEArNY3pxgra2LzM8LwNTE+X6c0oqp4Ts4cQOOy+95AlpT8OcVWQV2VhZGObDYImQIc/IXogOWS6xlcSwln5XcB+R/JjsEBxxiZcaASa2P1JY03SQRBz9NpLqMa92PgDDy97lf9xd1M18svoSjsugDURIr7NoEwIJyAAQonrkLjyRZ84WPRBfohDIgKOqMEG4eW+aOoLpLeWTXA==",
    "KeyId": "arn:aws:kms:us-west-2:332173347248:key/b7a11be8-2a95-429e-978c-36a18a0d3e81",
    "EncryptionAlgorithm": "SYMMETRIC_DEFAULT"
}
```

We don't have the permission to decrypt the message or to access the key. We will list the roles:

```sh
aws iam list-roles > roles.json
```

By analyzing the roles, we find a role named "crypto-master" that can encrypt and decrypt messages for Cipher.

```json
{
    "RoleName": "crypto-master",
    "Arn": "arn:aws:iam::332173347248:role/crypto-master",
    "Description": "Can encrypt and decrypt messages for Cipher",
    "AssumeRolePolicyDocument": {
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "AWS": "arn:aws:iam::332173347248:user/user1"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }
}
```

We can assume the role "crypto-master" to decrypt the message:

```sh
┌──(virgile㉿localhost)-[~]
└─$ aws sts assume-role --role-arn arn:aws:iam::332173347248:role/crypto-master --role-session-name decryptSession                                                                                                                         
{
    "Credentials": {
        "AccessKeyId": "ASIAU2VYTBGYHVMAPZTF",
        "SecretAccessKey": "REDACTED",
        "SessionToken": "REDACTED==",
        "Expiration": "2025-03-19T14:26:32+00:00"
    },
    "AssumedRoleUser": {
        "AssumedRoleId": "AROAU2VYTBGYKCB3S25MX:decryptSession",
        "Arn": "arn:aws:sts::332173347248:assumed-role/crypto-master/decryptSession"
    }
}
```

Let's now connect to the role:

```sh
┌──(virgile㉿localhost)-[~]
└─$ export AWS_ACCESS_KEY_ID="ASIAU2VYTBGYHVMAPZTF"
export AWS_SECRET_ACCESS_KEY="REDACTED"
export AWS_SESSION_TOKEN="REDACTED=="
```

Now we can decrypt the message:

```sh
┌──(virgile㉿localhost)-[~/Téléchargements]
└─$ cat 20250301.msg.enc | jq -r '.CiphertextBlob' | base64 --decode > ciphertext.bin
```

We use the AWS KMS service to decrypt the message:

```sh
┌──(virgile㉿localhost)-[~/Téléchargements]
└─$ aws kms decrypt --ciphertext-blob fileb://ciphertext.bin --output text --query Plaintext | base64 --decode
To Cipher,

I trust this letter finds you in the usual manner — lurking in the shadows, plotting your next grand scheme. Though we are well aware of your notorious abilities, it seems there is still much potential for even greater power at your fingertips.

I am writing to you, Cipher, not only to acknowledge your skills but to propose an alliance of sorts. Your penchant for manipulation of digital systems and mine for delving into the very fabric of reality itself could culminate in a masterpiece of absolute control.

I have discovered the key to hacking time itself — a process far beyond the scope of mere algorithms. The foundation lies in manipulating the quantum fabric and exploiting the synchronization of universal chronal waves. Once we control this frequency, we can write our own timeline.

THM{crypto_cloud_conundrum}
```

So the flag is `THM{crypto_cloud_conundrum}`.