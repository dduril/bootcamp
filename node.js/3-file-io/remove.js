var fs = require("fs");

// remove the file we renamed
try {
    fs.unlinkSync("./lib/test-1a.md");
} catch (err) {
    console.log(err);  
}

// remove the file we moved
fs.unlink("test-2.txt", function(err) {
   
    if (err) {
        console.log(err);    
    } else {
        console.log("test-2.txt successfully removed");
    }
    
});