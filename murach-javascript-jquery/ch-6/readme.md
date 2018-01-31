## JavaScript and jQuery 

### DOM Scripting with JavaScript

**About these pages:** *Notes and code samples from **[Murach's JavaScript and jQuery, 3rd Edition](https://www.murach.com/shop-books/web-development-books/murach-s-javascript-and-jquery-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**DOM** - Document Object Model

**Document and Element Interface Methods**

- `getElementsByTagName(tagName)`
- `getElementsByName(name)`
- `getElementsByClassName(classNames)`
- `getElementById(id)`
- `hasAttribute(name)`
- `getAttribute(name)`
- `setAttribute(name, value)`
- `removeAttribute(name)`

**Examples**

	// create an array of <a> tags in document
	var links = document.getElementsByTagName("a");

	// create an array of <li> tags within <ul> list
	var list = document.getElementsById("photo_list");
	var items = list.getElementsByTagName("li");

	// test for an attribute
	var list = document.getElementsById("photo_list");
	if (list.hasAttribute("class") ) {
		var classAttribute = list.getAttribute("class");
	}
	
	// set an attribute
	var list = document.getElementsById("photo_list");
	list.setAttribute("class", "expand");

	// remove an attribute
	var list = document.getElementsById("photo_list");
	list.removeAttribute("class");
