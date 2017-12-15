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

**Adding JavaScript to head section**

	<script src="calculate_mpg.js"></script>

**Embedding JavaScript in head section**

	<script>
		alert("Calculate MPG");
		var miles = prompt("Enter miles driven");
		miles = parseFloat(miles);
		var gallons = prompt("Enter gallons of gas used");
		gallons = parseFloat(gallons);
		var mpg = miles/gallons;
		alert("Miles per gallon: " + mpg); 
	</script>

**JavaScript in the body section**
	<script>
		var today = new Date();
		document.write("Current date: " );
		document.write(today.toDdateString());
	</script>
[[Top]](https://github.com/dduril/bootcamp/tree/master/murach-javascript-jquery#top)


