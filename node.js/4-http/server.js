var http = require("http");

var server = http.createServer(function(req, res) {
 
    res.writeHead(200, {"Content-Type" : "text/html"});
    
    res.end(`
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>HTML Response</title>
        </head>
        <body>
            <h1>Serving HTML</h1>
            <p>${req.url}</p>
            <p>${req.method}</p>
        </body>
        </html>
    `);
    
});

server.listen(3000);

console.log("Server listening on port 3000");


/*
//plain text version

var server = http.createServer(function(req, res) {
 
    res.writeHead(200, {"Content-Type" : "text/plain"});
    
    res.end("Hello World");
    
});

server.listen(3000);

console.log("Server listening on port 3000");
*/