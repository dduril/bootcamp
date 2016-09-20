alert("Hello World!");

var month = 9, day = 19, year = 2016;
console.log("Today's date: " + month + "/" + day + "/" + year);

// variable declarations
var x = 100;
var y = 200;
var str = "Hello World!";
var flag = true;

// conditional code
if (x > 100) {
    console.log("x is greater than 100.");
} else if (x < 100)  {
    console.log("x is less than 100.");
} else {
    console.log("x is equal to 100.");
}   

// assignment
var a = 10;
var b = 25;
var result = a + b;
console.log("result: " + result);

// equality check, same value
console.log("equality check");
var a = 10;
var b = "10";

if (a == b) {
    console.log("true");
} else {
    console.log("false");
}

// strict equality check, same value and same type
console.log("strict equality check");
if (a === b) {
    console.log("true");
} else {
    console.log("false");
}

// logical and / or
console.log("logical and / or");
var a = 5;
var b = 5;
var c = 8;
var d = 8;
if ((a === b) && (c === d)) {
    console.log("true");
} else {
    console.log("false");   
}

a = 4;
d = 7;
if ((a === b) || (c === d)) {
    console.log("true");
} else {
    console.log("false");   
}

// ternary operator
console.log("ternary operator");
var x = 400;
var y = 500;
(x > y) ? console.log("x > y") : console.log("x < y");

var highest = (x > y) ? x : y;
console.log(highest)

// console output options
console.log("Log");
console.info("Info");
console.warn("Warn");
console.error("Error");

// loops

// while loop
console.log("while example");
var a = 1;
while (a <= 10) {
    console.log(a); 
    a++;
}

// do while loop - always executes at least once
console.log("do while example");
var a = 10;
do {
    console.log(a); 
    a--;
} while (a >= 1);

// for loop
console.log("for loop example");
for (var i = 1; i <= 10; i++) {
    console.log(i); 
}

// break
console.log("break example");
for (var i = 1; i <= 10; i++) { 
    if (i == 5) {
        break;   
    }
    console.log(i);
}

//continue
console.log("continue example");
for (var i = 1; i <= 10; i++) {
    if (i % 2 == 0) {
        continue;   
    }
    console.log(i); 
}

// functions
function createMessage(firstName, lastName) {
    console.log("Greetings! " + firstName + " " + lastName); 
}

function createGreeting(firstName, lastName) {
    return "Greetings! " + firstName + " " + lastName;
}

createMessage("John", "Smith");

greeting = createGreeting("Lisa", "Jones");
console.log(greeting);