#!/usr/bin/env python3

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
