## JavaScript and jQuery 

### Getting Started with jQuery

**About these pages:** *Notes and code samples from **[Murach's JavaScript and jQuery, 3rd Edition](https://www.murach.com/shop-books/web-development-books/murach-s-javascript-and-jquery-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**jQuery Frameworks/Libraries**

- **[jQuery](https://jquery.com/)** - JavaScript library
- **[jQuery UI](http://jqueryui.com/)** - Collection of widgets, themes built on top of jQuery
- **[jQuery Mobile](http://jquerymobile.com/)** - jQuery framework for mobile-accessible web applications
- **[QUnit](http://qunitjs.com/)** - JavaScript unit testing framework

**Basic jQuery Selector**

	$("selector")

	// element type
	$("a")

	// id
	$("#menu")
	
	// class
	$(".highlight")

**Common jQuery Methods**

- `val()`
- `val(value)`
- `text()`
- `text(value)`
- `next([type])`
- `submit()`
- `focus()`

**Examples**

	// get value from a textbox
	var first_name = $("#first_name").val();

	// set the value for an input element
	$("#first_name").val("");

	// set text
	$("#first_name").text("First name is a required field.");

	// submit a form
	$("#application").submit();

	// set focus
	$("#first_name").focus();

**Document Ready Event**

	$(document).ready(function() {
		alert("The DOM is ready.");
	});

**Click Event Handler in Ready Event Handler**

	$(document).ready(function() {
		$("h1").click(function() {
			alert("Heading clicked.");
		}); // click event handler
	});	// ready event handler

**Useful jQuery Selectors**

- `contains(text)`
- `empty`
- `eq(n)`
- `even`
- `first`
- `first-child`
- `gt`
- `has(selector)`
- `last`
- `last-child`
- `lt(n)`
- `not(selector)`
- `nth-child`
- `odd`
- `only-child`
- `parent`
- `text`

**Examples**

	// li elements that are first children
	$("li:first-child")

	// even tr elements in a table
	$("table > tr:even)

	// select second li in menu element
	$("menu li:eq(1)")

**Useful jQuery Methods**

- `next([selector])`
- `prev([selector])`
- `find(selector)`
- `attr(attributeName)`
- `css(propertyName, value)`
- `addClass(className)`
- `removeClass(className)`
- `toggleClass(className)`
- `html(htmlString)`
- `hide([duration])`
- `show([duration])`
- `each(function)`

**Examples**

	// value of the title attribute of a link
	$("#link").attr("title");

	// set the value of the color property for an h2 element
	$("h2").css("color", "darkgreen");

	// add a class to h2 descendents of the menu element
	$("#menu h2").addClass("highlight");

	// add html content to an article element
	$("article").html("<h2>Agenda</h2>");

	// run a function for each <a> element of the menu element
	$("#menu a").each(function() {
		// statements...
	}); 

**jQuery Event Methods**

- `ready()(handler)`
- `click()(handler)`
- `dblclick(handler)`
- `mouseenter(handler)`
- `mouseover(handler)`
- `mouseout(handler)`
- `hover(handlerIn, handlerOut)`
- `event.preventDefault()`

**Examples**

	// hover event handler
	$("#gallery img").hover(
		function() {
			alert("hovering...");
		},
		function() {
			alert("not hovering...");
		}
	);

	// preventDefault method
	$("#menu a").click(function(evt) {
		evt.preventDefault();
	});