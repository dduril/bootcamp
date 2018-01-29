## JavaScript and jQuery 

### Getting Started with JavaScript

**About these pages:** *Notes and code samples from **[Murach's JavaScript and jQuery, 3rd Edition](https://www.murach.com/shop-books/web-development-books/murach-s-javascript-and-jquery-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**Script Element*

	<script src="scripts/app.js" type="text/javascript"></script>

**Basic syntax rules**

- JavaScript is case-sensitive
- JavaScript statements end with a semicolon
- JavaScript ignores whitespace within statements

**Notation**

- Camel casing - **firstName**
- Underscore - **first_name**
	- use lowercase for all letters

**Comments**

- Block comments begin with /* and end with */
- Single-line comments begin with two forward slashes //

**JavaScript Primitive Types**

- Number
- String
- Boolean

**Assignment**

	var count = 0;
	var first_name = "John";
	var is_valid = true;

**Compound Assignment**

	var counter = 0;
	counter += 1;

	var price = 10;
	price *= .75;

**Concatenation**

	var first_name = "John";
	var last_name = "Smith";
	var full_name = first_name + " " + last_name;

**Window Object Methods**

- alert(string)
- prompt(string, default)
- confirm(string)
- print()
- parseInt(string)
- parseFloat(string)

**Document Object Methods**

- getElementById(id)
- write(string)
- writeln(string)


---

### MPG Calculate Application

**Form**

![Example](/murach-javascript-jquery/ch-2/ch-2-screenshot-1.png "MPG Calculate Form")

**Results**

![Example](/murach-javascript-jquery/ch-2/ch-2-screenshot-2.png "MPG Calculate Results")





