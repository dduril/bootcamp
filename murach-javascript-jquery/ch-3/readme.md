## JavaScript and jQuery 

### JavaScript Statements

**About these pages:** *Notes and code samples from **[Murach's JavaScript and jQuery, 3rd Edition](https://www.murach.com/shop-books/web-development-books/murach-s-javascript-and-jquery-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**Relational Operators**

- `===`
- `==`
- `!=`
- `>`
- `<`
- `>=`
- `<=`

**Logical Operators**

- `&&`
- `||`
- `!`

**Examples**

	score >= 80 && score < 90

	isNaN(rate) || rate < 0

	!isValid

**if Statements**

	if (isValid) {
		alert("Access granted.");
	}
	
	
	if (isValid) {
		alert("Access granted.");
	} 
	else {
		alert("Please contact administration.");
	}


	if (score > 90) {
		alert("A");
	} else if (score > 80) {
		alert("B");
	} else if (score > 70) {
		alert("C");
	} else if (score > 60) {
		alert("D");
	} else {
		alert("No pass.");
	}

**while Loop**

	var sum = 0;
	var num = 10;
	var counter = 1;
	while (counter <= num) {
		sum += counter;
		counter++;
	}
	return sum;

**do-while Loop**

	var sum = 0;
	var num = 10;
	var counter = 1;
	do {
		sum += counter;
		counter++;
	} while (counter <= num);
	return sum;

**for Loop**

	var sum = 0;
	var num = 10;
	for (var i = 0; i < num; i++) {
		sum += i;
	}
	return sum;


	