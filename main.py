#!/usr/bin/python3

from highway import run

def home(env):
    return { 'page': 'Home' }

def about(env):
    return 'About page'

run({
    '/': home,
    'GET /about': about
})
