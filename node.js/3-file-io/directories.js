var fs = require("fs");

// remove files in logs directory
fs.readdirSync("./logs").forEach(function(fileName) {
   
    fs.unlinkSync("./logs/" + fileName);
    
});

// remove logs directory - now empty
fs.rmdir("./logs", function(err) {
   
    if (err) {
        throw err;    
    }
    
    console.log("Logs directory removed");
    
});