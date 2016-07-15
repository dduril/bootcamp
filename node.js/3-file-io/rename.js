var fs = require("fs");

// rename file
fs.renameSync("./lib/test1.txt", "./lib/test-1a.md");

console.log("test1 txt file renamed");

// move file to another directory
fs.rename("./lib/test2.txt", "./test-2.txt", function(err) {
   
    if (err) {
        console.log(err);    
    } else {
        console.log("test2.txt moved successfully");
    }
    
});