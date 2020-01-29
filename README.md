# Highway
Micro framework to handle routes and requests

## How to use
```python
# Python
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
```javascript
# JavaScript
const { run } = require("./highway.js")

function home(req) {
  return { 'page': 'Home' }
}

function about(req) {
  return 'About page'
}

run({
  '/': home,
  'GET /about': about
})
```

## License
MIT
