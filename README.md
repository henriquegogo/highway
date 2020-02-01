# Highway
Micro framework to handle routes and requests

## How to use
```python
import highway

def home(req):
    return { "pages": ["/", "/user"] }

def user(req):
    return { "name": "henriquegogo" }

def create_user(req):
    return { "name": req["data"]["name"], "status": "created" }

highway.run({
    "GET /": home,
    "GET /user": user,
    "POST /user": create_user
})
```

## License
MIT
