# Highway
Micro framework to handle routes and requests

## How to use
```python
def route_function(request):
    # request.params -> Everything after router. /route/[firstname/secondname]
    # request.query_srtring -> The query string. /route?firsname=foo&secondname=bar
    # request.data -> POST data
    return { "return": "Any python dict will be converted to json" }

run({
    "METHOD /route": route_function
})
```

## Example
```python
import highway

def home(req):
    return { "pages": ["/", "/user"] }

def user(req):
    return { "name": req.params[0] if len(req.params) > 0 else "" }

def create_user(req):
    return { "name": req.data["name"], "status": "created" }

highway.run({
    "GET /": home,
    "GET /user": user,
    "POST /user": create_user
})
```

## License
MIT
