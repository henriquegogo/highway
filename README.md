# Highway
Micro framework to handle routes and requests in python

## How to use
```python
from highway import run

def home(env):
    return { 'page': 'Home' }

def about(env):
    return 'About page'

run({
    '/': home,
    'GET /about': about
})
```

## License
MIT
