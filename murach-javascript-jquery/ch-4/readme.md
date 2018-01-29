## JavaScript and jQuery 

### JavaScript Objects, Functions, and Events

**About these pages:** *Notes and code samples from **[Murach's JavaScript and jQuery, 3rd Edition](https://www.murach.com/shop-books/web-development-books/murach-s-javascript-and-jquery-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

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

**Examples**

	// retrieve values from textbox
	var firstName = document.getElementById("first_name").value;
	var lastName = document.getElementById("last_name").value;

	document.write("Name: " + firstName + " " + lastName);

	// use parseFloat
	var salesAmount = document.getElementById("sales_amount");
	salesAmount = salesAmount.value;	
	salesAmount = parseFloat(salesAmount);

	// use chaining
	var salesAmount = 
		parseFloat(document.getElementById("sales_amount").value).toFixed(2);

**Textbox Object**

- focus()

**Number Object**

- toFixed(digits)

**Date Object**

- toDateString()
- getFullyear()
- getDate()
- getMonth()

**String Object**

- indexOf(search, position)
- substr(start, length)
- substring(start, stop)
- toLowerCase()
- toUpperCase()

**Function Expressions**

	var $ = function(id) {
		return document.getElementById(id);
	}

	var addNumbers = function(x, y) {
		return x + y;
	}

	var a = 10;
	var b = 5;
	var total = addNumbers(a, b);

**Function Declarations**

	function addNumbers(x, y) {
		return x + y;
	}

	var a = 10;
	var b = 5;
	var total = addNumbers(a, b);



