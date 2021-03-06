## JavaScript and jQuery 

### Working with Links, Images, and Timers

**About these pages:** *Notes and code samples from **[Murach's JavaScript and jQuery, 3rd Edition](https://www.murach.com/shop-books/web-development-books/murach-s-javascript-and-jquery-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**Event Object - Default Action**

	var eventHandler = function(evt) {
		evt.preventDefault();
	}

**Image Preloading**

	var links = document.getElementsByTagName("a");
	var i, link, image;
	for (i = 0; i < links.length; i++) {
		link = links[i];
		image = new Image();
		image.src = link.href;
	}

**Anonymous Function**

	var timer;
	var counter = 0;
	window.onload = function() {
		timer = setInterval( function() {
			counter++;
			$("counter").firstChild.nodeValue = counter;
		},
		1000 );
	};