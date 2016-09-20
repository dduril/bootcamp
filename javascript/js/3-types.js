// array
var arr = [];
arr[0] = 1;
arr[1] = 2;
arr[2] = 3;
arr[3] = 4;
arr[4] = 5;
console.log(arr[0]);

// array shorthand
var arr2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144];
console.log(arr2);

// array longhand
var arr3 = new Array();
var arr4 = Array();
var arr5 = Array(5);

// array properties
var nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log(nums.length);

// array methods
var reversedNums = nums.reverse();
console.log(reversedNums);

// numbers - stored as 64-bit floating point numbers
var x = 200;
var y = 200.5;

// addition versus concatenation
var foo = 5;
var bar = 5;
console.log(foo + bar);

var foo = "5";
var bar = "5";
console.log(foo + bar);

var foo = 5;
var bar = "5";
console.log(foo + bar);

var foo = 5;
var bar = "5";
console.log(foo * bar);

var foo = "55";
var myNumber = Number(foo);

// double negative - if NOT NOT a number
if (!isNaN(myNumber)) {
    console.log("It IS a number.");   
}

// Math object
var x = 200.78;
console.log(x);
var y = Math.round(x);
console.log(y);

var a = 200, b = 5000, c = 5;
var biggest = Math.max(a, b, c);
console.log(biggest);
var smallest = Math.min(a, b, c);
console.log(smallest);

console.log(Math.PI);
console.log(Math.random());
console.log(Math.sqrt(a));

// Strings
var greeting = "Hello World!";
console.log(greeting);
console.log(greeting.length);
console.log(greeting.toLowerCase);
console.log(greeting.toUpperCase);

var words = greeting.split(" ");
console.log(words);

var phrase = "A long time ago, in a galaxy far, far away...";
console.log(phrase);

// indexOf
var indx = phrase.indexOf("far");
console.log(indx);

// slice
var segment = phrase.slice(0, 15);
console.log(segment);

// substring(start, end)

// substr(start, length)

// string comparison
var str1 = "Hello";
var str2 = "hello";
if (str1.toLowerCase() == str2.toLowerCase()) {
    console.log("Equal");   
}

var str1 = "aardvark";
var str2 = "Badger";
if (str1.toLowerCase() < str2.toLowerCase()) {
    console.log("Less than");   
}

// Dates
var today = new Date();
console.log(today);
console.log(today.getMonth());          // returns 0-11
console.log(today.getFullYear());       // YYYY
console.log(today.getDate());           // 1-31 day of month
console.log(today.getDay());            // 0-6 day of week
console.log(today.getHours());          // 0-23
console.log(today.getMinutes());        
console.log(today.getSeconds());
console.log(today.getMilliseconds());
console.log(today.getTime());           // milliseconds since 1/1/1970

var myDate = new Date(2016, 8, 19, 0, 0, 0);
console.log(myDate);

// can also use set methods
var today = new Date();
today.setMonth(8);
today.setFullYear(2016);
today.setDate(19);
console.log(today);

// comparing dates
var date1 = new Date(2016, 8, 19, 0, 0, 0);
var date2 = new Date(2016, 8, 20, 0, 0, 0);

if ( date1.getTime() == date2.getTime() ) {
    console.log("Equal");   
} else {
    console.log("Not Equal");   
}

// Objects
var employee = new Object();
employee.empNum = 100;
employee.firstName = "John";
employee.lastName = "Smith";
employee.department = "Engineering";
employee.startDate = new Date();

console.log(employee);
console.log(employee.empNum);
console.log(employee.firstName + " " + employee.lastName);

// shorthand
var employee1 = { 
    empNum: 100, 
    firstName: "John", 
    lastName: "Smith", 
    department: "Engineering", 
    startDate: new Date()
};

function employeeDetails() {
    console.log("Employee Details:");
    console.log(this.empNum);
    console.log(this.firstName + " " + this.lastName);
    console.log(this.department);
    console.log(this.startDate);
}

employee1.logDetails = employeeDetails;

employee1.logDetails();


























