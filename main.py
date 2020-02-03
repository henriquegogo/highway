#!/usr/bin/env python3

import highway

def home(req):
    return { "pages": ["/", "/user"] }

def user(req):
    return { "name": req["params"][0] if len(req["params"]) > 0 else "" }

def create_user(req):
    return { "name": req["data"]["name"], "status": "created" }

highway.run({
    "GET /": home,
    "GET /user": user,
    "POST /user": create_user
})
