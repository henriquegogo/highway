from wsgiref import simple_server, util
from urllib.parse import parse_qsl
import os, mimetypes, json

def run(routes={}, port=8000):
    def request_manager(env, response):
        path, method, code, body = env["PATH_INFO"], env["REQUEST_METHOD"], "404 Not Found", ""
        route, params, static = path.split("/")[1], path.split("/")[2:], "public/index.html" if path == "/" else "public" + path

        if method + " /" + route in routes:
            request = type("", (object,), {
                "params": params,
                "query_string": type("", (object,), dict(parse_qsl(env["QUERY_STRING"])))(),
                "data": json.loads(env["wsgi.input"].read(int(env["CONTENT_LENGTH"])).decode()) if env["CONTENT_LENGTH"] else {}
            })()
            code, body = "200 OK", json.dumps(routes[method + " /" + route](request))
        elif os.path.exists(static):
            response("200 OK", [("Content-type", mimetypes.guess_type(static)[0])])
            return util.FileWrapper(open(static, "rb"))

        response(code, [("Content-type", "text/plain; charset=utf-8")])
        return [body.encode()]

    with simple_server.make_server("", port, request_manager) as httpd:
        print("Serving on port "+str(port)+"...")
        httpd.serve_forever()
