<a name="top"></a>
# HTML5 and CSS3

Based on **[Murach's HTML5 and CSS3, 3rd Edition](https://www.murach.com/shop/murachs-html5-and-css3-3rd-edition-detail)**.

The purpose of this repo is to practice coding responsive web pages using HTML5 and CSS3.

### Getting Started

- **[HTML5 Test](https://html5test.com/)**
- **[W3C](https://www.w3.org/)**
- **[W3C HTML Validator](https://validator.w3.org/)**
- **[W3C CSS Validator](https://jigsaw.w3.org/css-validator/)**

#### Editors

- **[Brackets](http://brackets.io/)**

#### Building Blocks and Language Syntax

- **[Template](https://github.com/dduril/bootcamp/tree/master/murach-html5-css3#template)**
- **[Including Metadata](https://github.com/dduril/bootcamp/tree/master/murach-html5-css3#metadata)**
- **[Adding Styles](https://github.com/dduril/bootcamp/tree/master/murach-html5-css3#css)**
- **[HTML Basics](https://github.com/dduril/bootcamp/tree/master/murach-html5-css3#html-basics)**

---

#### Template<a name="template"></a>
**HTML5 template**

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

**Basic CSS example**

	body {
	    font-family: Arial, Helvetica, sans-serif;
	    font-size: 100%;
	    width: 680px;
	    margin: 0 auto;
	    padding: 1em;
	}
	main {
	    display: block; 
		padding: 1em;
	    margin-bottom: 1em;    
	}
	h1 {
	    margin: 0;
	    padding: .25em;
	    font-size: 200%;
	}
	p {
	    margin: 0;
	    padding-bottom: .5em;
	}
	footer {
	    text-align: left;
	    font-size: .8em;
	}

[[Top]](https://github.com/dduril/bootcamp/tree/master/murach-html5-css3#top)


#### Including Metadata<a name="metadata"></a>

	<head>
    	<meta charset="UTF-8">
		<meta name="description" content="HTML5 template for modern web pages">
		<meta name="keywords" content="HTML5, CSS3, responsive web design, semantic, cutting edge">
    	<title>HTML5 Template</title>
	</head>

[[Top]](https://github.com/dduril/bootcamp/tree/master/murach-html5-css3#top)


#### Adding Styles<a name="css"></a>

**External style sheet**

	<link rel="stylesheet" href="assets/styles/custom.css">

**Embedded styles**

	<head>
	...
		<style>
			body {
			    font-family: Arial, Helvetica, sans-serif;
			    font-size: 100%;
			    margin: 0 auto;
			}
			h1 { font-size: 200%;
			}
		</style>
	</head>

**Inline styles**

	<h2 style="font-size: 125%; color: blue; padding-bottom: .5em;">Meeting Agenda</h2>

**CSS Selectors**

All elements

	* { margin: 0; padding: 0; } 

Selecting elements by type

	body {
    	font-size: 100%;
    	margin-left: 2em;
    	margin-right: 2em;
	}

	header {
    	padding-bottom: .75em;
    	border-bottom: 2px solid black;
    	margin-bottom: 0;
	}

	h1, h2, h3 {
		color: navy;
	}

Selecting element by ID (Unique Identifier)

	#footer {
		padding: 10px;
		background: #fff;
		border-top: 1px solid #ddd;
		color: #999;
		font-size: .875em;
		}

Elements by class (One or more)

	.list {
		font: 0.875em/1.8em Arial, Verdana, sans-serif;
		line-height: 1.8em;
		list-style-type: square;
		text-indent: 2em;
	}

[[Top]](https://github.com/dduril/bootcamp/tree/master/murach-html5-css3#top)

#### HTML Basics<a name="html-basics"></a>

**Headings and paragraphs**

- `h1` - Content in bold at 200% of the base font size
- `h2` - Content in bold at 150% of the base font size
- `h3` - Content in bold at 117% of the base font size
- `h4` - Content in bold at 100% of the base font size
- `h5` - Content in bold at 83% of the base font size
- `h6` - Content in bold at 67% of the base font size
- `p` - Paragraph of text at 100% of the base font size

**Formatting code**

	<pre>
		var today = new Date();
	    document.write("Today's date: " + today.toDateString());
	    document.write("<br>");
	</pre>

**Primary HTML5 elements**

- **`header`**
- **`main`**
- **`section`**
- **`article`**
- **`aside`**
- **`nav`**
- **`footer`**

Example:

	<!DOCTYPE html>
	<html lang="en">
		<head>
			<meta charset="UTF-8">
			<title>Web Development</title>
		</head>
		<body>
			<header>
				<h1>Web Development</h1>
			</header>
			<main>
				<h2>Courses</h2>
				<nav>
					<ul>
						<li>HTML5 and CSS3</li>
						<li>JavaScript and jQuery</li>
						<li>Responsive Web Design</li>
					</ul>
				</nav>
			</main>  
			<footer>
				&copy; Copyright 2017
			</footer>
		</body>
	</html>

**Ordered lists**

	<ol>
		<li>Create Account</li>
		<li>Select Products</li>
		<li>Proceed to Checkout</li>
	</ol>

**Unordered lists**

	<ul>
		<li>HTML5</li>
		<li>jQuery</li>
		<li>Bootstrap</li>
	</ul>

[[Top]](https://github.com/dduril/bootcamp/tree/master/murach-html5-css3#top)