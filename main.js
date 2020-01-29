#!/usr/bin/env node

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
