from wsgiref.simple_server import make_server
import json

def run(routes={}, port=8000):
    def manager(env, response):
        path, method = env["PATH_INFO"], env["REQUEST_METHOD"]
        code, body = "200 OK", ""

        if path in routes: body = routes[path](env)
        elif method+" "+path in routes: body = routes[method+" "+path](env)
        else: code = "404 Not found"

        response(code, [("Content-type", "text/plain; charset=utf-8")])
        if type(body) is dict: body = json.dumps(body)
        return [body.encode()]

    with make_server("", port, manager) as httpd:
        print("Serving on port "+str(port)+"...")
        httpd.serve_forever()
