const http = require('http')

function run(routes={}, port=8000) {
  function manager(req, res) {
    const path = req.url, method = req.method
    let body = ""

    if (Object.keys(routes).includes(path)) body = routes[path](req)
    else if (Object.keys(routes).includes(method+" "+path)) body = routes[method+" "+path](req)

    if (typeof body == "object") body = JSON.stringify(body)
    res.end(body)
  }

  http.createServer(manager).listen(port, "", () => {
    console.log("Serving on port " + port + "...")
  })
}

module.exports = { run }
