/* jshint esnext: true */

var http = require("http");

http.createServer(function(req, res) {
 
    res.writeHead(200, {"Content-Type" : "text/html"});
    
    res.end(`
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>web Server</title>
        </head>
        <body>
            <h1>Hello World</h1>
        </body>
        </html>
    `);
    
}).listen(3000);

console.log("Web Server running at http://localhost:3000");