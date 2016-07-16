var http = require("http");
var data = require("./data/star-wars");

http.createServer(function(req, res) {
    
    res.writeHead(200, {"Content-Type" : "text/json"});
    
    res.end(JSON.stringify(data));
    
}).listen(3000);

console.log("Server listening on port 3000");