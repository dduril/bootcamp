var path = require("path");

// write Hello World to console
console.log("Hello World");

// create a string variable
var hello = "Hello World from Node.js";
console.log(hello);

// slice off 17 characters and assign to justNode variable
var justNode = hello.slice(17);

console.log(justNode);
console.log(`Rock on World from ${justNode}`);

// get directory and file paths
console.log(__dirname);
console.log(__filename);
console.log(path.basename(__filename));