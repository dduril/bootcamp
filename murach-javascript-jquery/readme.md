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

Working with arrays

    var genres = [];
	genres[0] = "Comedy";
	genres[1] = "Drama";
	genres[2] = "Horror";
	genres[3] = "Musical";
	genres[4] = "Science Fiction";
	var count = genres.length;		// 5

	genres_string = "";
	for (var i = 0; i < genres.length; i++) {
		genres_string += "- " + genres[i] + "\n";
	}
	alert("Our Genres include:\n\n" + genres_string);

JavaScript Objects

	var entry = document.getElementById("entry");

	document.write("Today's date: " + today.toDateString() + "<br>");

Using Textbox and Number objects

	// assuming these HTML tags:
	// <input type="text" id="first_name">
	// <input type="text" id="price">

	var firstName = document.getElementById("first_name");
	firstName = firstName.value;

	var price = document.getElementById("price");
	price = price.value;
	price = parseFloat("price").toFixed(2);

	// same example using chaining
	var price = parseFloat(document.getElementById("price").value).toFixed(2);

	// a few more examples
	document.getElementById("first_name").value = "";
	document.getElementById("first_name").focus();

Date object

	var myDate = new Date();
	document.write(myDate.toDateString() + "<br>");
	document.write(myDate.getFullYear() + "<br>");
	document.write(myDate.getDate() + "<br>");
	document.write(myDate.getMonth() + "<br>");

String object

	var fullName = "John Smith";
	var nameUpper = fullName.toUpperCase();
	var nameLower = fullName.toLowerCase();
	var nameLength = fullName.length;

Function expressions

	// example 1
	var $ = function(id) {
		return document.getElementById(id);
	};

	var firstName = $("first_name").value;

	// example 2
	var calcPerimeter = function(l, w) {
		var perimeter = 2(l + w);
		return perimeter;
	};

	var sideLength = 10;
	var sideWidth = 5;
	var perimeter = calcPerimeter(sideLength, sideWidth);
	document.write("Perimeter: " + perimeter + "<br>");

Function declarations

	// example 1
	function $(id) {
		return document.getElementById(id);
	}

	var firstName = $("first_name").value;	

	// example 2
	function calcPerimeter(l, w) {
		var perimeter = 2(l + w);
		return perimeter;
	};

	var sideLength = 10;
	var sideWidth = 5;
	var perimeter = calcPerimeter(sideLength, sideWidth);
	document.write("Perimeter: " + perimeter + "<br>");

**Scripting the DOM with JavaScript**

Get the text of an HTML element with "first_name" as its id

	var firstName = document.getElementById("first_name").firstChild.nodeValue;

Set the text of an HTML element with "first_name" as its id

	document.getElementById("first_name").firstChild.nodeValue = "John Smith";

Create an array of all `p` tags in a document

	var paragraphs = document.getElementsByTagName("p");

Create an array of all `li` tags within an `ul` element

	var list = document.getElementById("content_list");
	var items = list.document.getElementsByTagName("li");

Test for and get an attribute

	var list = document.getElementById("content_list");
	if (list.hasAttribute("class")) {
		var classAttribute = list.getAttribute("class");
	}

Set an attribute

	var list = document.getElementById("content_list");
	list.setAttribute("class", "highlight");

Remove an attribute

	var list = document.getElementById("content_list");
	list.removeAttribute("class");

Retrieving values from a text box, text area and select list

	function $(id) {
		return document.getElementById(id);
	}

	var first_name = $("first_name").value;
	var comments = $("comments").value

	if ( first_name.length == 0 ) { alert("Please enter your name."); }
	if ( comments.length == 0 ) { alert("Please enter a comment."); }

	var location = $("location").value;
	if ( location == "CA" ) { /* CA processing */ }
	else if ( location == "OR" ) { /* OR processing */ }
	else if ( location == "WA" ) { /* WA processing */ }

	// reset values
	$("first_name").value = "";
	$("comments").value = "";
	$("location").value = "";

Retrieving values from radio buttons and check boxes

	function $(id) {
		return document.getElementById(id);
	}

	var contactType;
	if ( $("text").checked )  { contactType = $("text").value; }
	if ( $("email").checked ) { contactType = $("email").value; }

	if ( contactType == "text" ) { /* text processing */}
	else if ( contactType == "email" ) { /* email processing */ }
	else { alert("Please select a contact type."); }

	var accept = $("accept").checked;
	if ( accept ) {
		/* accept processing */
	} else { alert("Please accept the agreement to proceed."); }

	// reset values
	$("text").checked = false;
	$("email").checked = false;
	$("accept").checked = true;

Using onload event handler to assign event handlers to events

	"use strict";
	var $ = function(id) { return document.getElementById(id); };
	
	var processForm = function() {
		/* form processing logic */
	};

	var resetForm = function() {
		/* form reset logic
	};
	
	window.onload = function() {
		$("register").onclick = processForm;
		$("reset_form").onclick = resetForm;    
		$("first_name").focus();
	};

[[Top]](https://github.com/dduril/bootcamp/tree/master/murach-javascript-jquery#top)