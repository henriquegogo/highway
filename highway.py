from wsgiref.simple_server import make_server
from urllib.parse import parse_qsl
import json

def run(routes={}, port=8000):
    def request_manager(env, response):
        path, method, code, body = env["PATH_INFO"], env["REQUEST_METHOD"], "404 Not Found", ""
        if method + " " + path in routes:
            request = { "query_string": dict(parse_qsl(env["QUERY_STRING"])), "data": json.loads(env["wsgi.input"].read(int(env["CONTENT_LENGTH"])).decode()) if env["CONTENT_LENGTH"] else {} }
            code, body = "200 OK", json.dumps(routes[method + " " + path](request))
        response(code, [("Content-type", "text/plain; charset=utf-8")])
        return [body.encode()]

    with make_server("", port, request_manager) as httpd:
        print("Serving on port "+str(port)+"...")
        httpd.serve_forever()
