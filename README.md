# Highway
Micro framework to handle routes and requests

## How to use
```python
def route_function(*params, post_data, query_string):
    return { "return": "Any python dict will be converted to json" }

run({
    "METHOD /route": route_function
})
```

## Static folder
./public

## Example
```python
import highway

def home():
    return { "pages": ["/", "/user"] }

def user(name="", query_string={}):
    return { "name": name, "age": query_string.get("age", "") }

def create_user(data):
    return { "name": data.get("name"), "status": "created" }

highway.run({
    "GET /": home,
    "GET /user": user,
    "POST /user": create_user
})
```

## License
MIT
