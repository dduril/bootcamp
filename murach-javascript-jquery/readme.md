<a name="top"></a>
# JavaScript and jQuery

Based on **[Murach's JavaScript and jQuery, 3rd Edition](https://www.murach.com/shop-books/web-design-books/murach-s-javascript-and-jquery-3rd-edition-detail)**.

The purpose of this repo is to practice coding responsive web pages using JavaScript and jQuery.

### Getting Started

- **[Google Developers](https://developers.google.com/)**
- **[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)**
- **[MDN - Mozilla Developer Network](https://developer.mozilla.org/en-US/)**
- **[Modern JavaScript Tutorial](http://javascript.info/)**

#### Editors

- **[Brackets](http://brackets.io/)**

#### Building Blocks and Language Syntax

- **[Templates](https://github.com/dduril/bootcamp/tree/master/murach-javascript-jquery#templates)**
- **[HTML5 Semantic Elements](https://github.com/dduril/bootcamp/tree/master/murach-javascript-jquery#html5-semantic-elements)**
- **[Adding JavaScript](https://github.com/dduril/bootcamp/tree/master/murach-javascript-jquery#add-javascript)**
- **[JavaScript Basics](https://github.com/dduril/bootcamp/tree/master/murach-javascript-jquery#javascript-basics)**

---

#### Templates<a name="templates"></a>
**HTML5 template using semantic tags**

	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>HTML5 Template</title>
		<link rel="stylesheet" href="style.css">
	</head>
	<body>
		<header><h1>HTML5 Template</h1></header>
		<main>
			<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
			<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
		</main>
		<footer>&copy; 2017</footer>
	</body>
	</html>
 
**HTML template using `div` tags**

	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>HTML5 Template</title>
		<link rel="stylesheet" href="style.css">
	</head>
	<body>
		<div class="header"><h1>HTML5 Template</h1></div>
		<div class="main">
			<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
			<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
		</div>
		<div class="footer">&copy; 2017</div>
	</body>
	</html>

[[Top]](https://github.com/dduril/bootcamp/tree/master/murach-javascript-jquery#top)


#### HTML5 Semantic Elements<a name="html5-semantic-elements"></a>
- **`header`**
- **`main`**
- **`section`**
- **`article`**
- **`aside`**
- **`nav`**
- **`figure`**
- **`footer`**

[[Top]](https://github.com/dduril/bootcamp/tree/master/murach-javascript-jquery#top)


#### Adding JavaScript<a name="add-javascript"></a>

**Linking external JavaScript to the head section**

	<script src="calculate_mpg.js"></script>

**Embedding JavaScript to the head section**

	<script>
		alert("Calculate MPG");
		var miles = prompt("Enter miles driven");
		miles = parseFloat(miles);
		var gallons = prompt("Enter gallons of gas used");
		gallons = parseFloat(gallons);
		var mpg = miles/gallons;
		alert("Miles per gallon: " + mpg); 
	</script>

**Adding JavaScript to the body section**

	<head>
	...
		<script>
			var today = new Date();
			document.write("Current date: " );
			document.write(today.toDdateString());
		</script>
	</head>

[[Top]](https://github.com/dduril/bootcamp/tree/master/murach-javascript-jquery#top)


#### JavaScript Basics<a name="javascript-basics"></a>

Comments

	/* multi-line comments...
	 * ...comments continue on next line...
	 */

	// single-line comment... 

JavaScript primitive types
	
	Number		10, -5, 25.8
	String		"JavaScript", 'jQuery'
	Boolean		true/false 

Declare and assign a value to a variable

	var num1;
	num1 = 10;

	var a, b;
	var x = 5, y = 10;

	var name = "John Smith";

	var isValid = true;

Concatenate strings

	var first_name = "John";
	var last_name = "Smith";
	var full_name = first_name + " " + last_name; 

	var months = 12;
	var message = "Months: ";
	message = message + months;

Using parseInt() and parseFloat()

	var years = document.getElementById("years").value;
	years = parseInt(years);

	var price = document.getElementById("price").value;
	price = parseFloat(price);

	var entry = document.getElementById("entry").value;	// entry = "hello"
	entry = parseInt(entry);							
	alert(entry);										// displays NaN

Using write() and writeln()

    <script>
		var today = new Date();
		document.write("Today's date: " + today.toDateString());
		document.write("<br>");

		document.writeln("Today's date: ");
		document.writeln(today.toDateString());
        document.write("<br>");
        
		document.writeln("<pre>Welcome to our site!");
		document.writeln("Today is Friday.</pre>");
	</script>

**Control statements**

if - else if - else

	if ( score >= 75 ) {
		alert("Pass.");
	} else {
		alert("Please review the material and try again.");
	}

	if ( score >= 90 ) {
		alert("You scored an A.");
	} else if ( score >= 80) {
		alert("You scored a B.");
	} else if ( score >= 70) {
		alert("You scored a C.");
	} else {
		alert("Please review the material and try again.");
	}

while loop

	var sum = 0;
	var loops = 10;
	var counter = 1;
	while (counter <= loops) {
		sum += counter;
		counter++;
	}
	alert(sum);

do-while loop

	var sum = 0;
	var loops = 10;
	var counter = 1;
	do {
		sum += counter;
		counter++;
	} while (counter <= loops);
	alert(sum);

for loops

	var sum = 0;
	var loops = 10;
	for (var counter = 1; counter <= loops; counter++) {
		sum += counter;
	}
	alert(sum);

[[Top]](https://github.com/dduril/bootcamp/tree/master/murach-javascript-jquery#top)