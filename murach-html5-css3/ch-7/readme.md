## HTML5 and CSS3

### Lists and Links

**About these pages:** *Notes and code samples from **[Murach's HTML5 and CSS3, 3rd Edition](https://www.murach.com/shop/murachs-html5-and-css3-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**Unordered lists**

- `ul`
- `list-style-type` properties
	- `disc`
	- `circle`
	- `square`
	- `none`
- `li`

**Example**

	<ul class="square">
		<li>Animal</li>
		<li>Vegetable</li>
		<li>Mineral</li>
	</ul>

	ul.square {
		list-style-type: square;
	}

**Ordered lists**

- `ol`
- `list-style-type` properties
	- `decimal`
	- `decimal-leading-zero`
	- `lower-alpha`
	- `upper-alpha`
	- `lower-roman`
	- `upper-roman`
- `li`

**Example**

	<ol class="lower_roman">
		<li>Crack eggs</li>
		<li>Scramble</li>
		<li>Mix-in toppings</li>
	</ol>

	ol.lower_roman {
		list-style-type: lower-roman;
	}

**Description lists**

- `dl`
- `dt`
- `dd`

**Example**

	<h2>Front End Development</h2>
	<dl>
		<dt>JavaScript</dt>
		<dd>Core language for web development and providing interactive UI and effects.</dd>
	</dl>

**`<a>` element**

- `href`
- `title`
- `tabindex`
- `accesskey`

**Example**

	<a href="https://jquery.com/" title="jQuery">jQuery</a>

**CSS pseudo-classes to format links**

- `link`
- `visited`
- `hover`
- `focus`
- `active`

**Example**

	a:link {
		color: darkgreen;
	}
	a:hover, a:focus {
		text-decoration: none;
		color: navy;
		font-weight: bold;
	}

**Removing underlines and borders**

- `text-decoration`
- `border-style`

