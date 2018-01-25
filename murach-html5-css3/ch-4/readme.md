## HTML5 and CSS3 

### Formatting Web Pages with CSS

**About these pages:** *Notes and code samples from **[Murach's HTML5 and CSS3, 3rd Edition](https://www.murach.com/shop/murachs-html5-and-css3-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**External style sheet**

	<link rel="stylesheet" href="assets/css/custom.css">

**Embedded styles**

	<style>
		body {
			font-family: Arial, sans-serif;
			font-size: 100%;
			width: 90%;
    		margin: 0 auto;
    		padding: 1em;
		}
	</style>

**Inline styles applied to a single element**

	<h1 style="font-size: 250%; color: #999;">Front End Developers</h1>

**Using more than one external CSS file**

	<head>
	    <meta charset="UTF-8">
	    <title>HTML5/CSS3 Examples</title>
	    <link rel="stylesheet" href="assets/css/normalize.css">
	    <link rel="stylesheet" href="assets/css/style.css">
	</head>

**Selecting by element type, id, and class**

**Type** - using element name

	body {
		font-family: Arial, sans-serif;
		font-size: 100%;
		width: 90%;
    	margin: 0 auto;
    	padding: 1em;
	}

**ID** - using hash character

	#main_div {
		font-size: .9em;
		text-align: left;
	}

**Class** - using dot character

	.bordered_nav {
		border: 1px solid #999;
	}

**CSS pseudo-classes**

- `:link`
- `:visited`
- `:active`
- `:hover`
- `:focus`
- `:first-child`
- `:last-child`
- `:only-child`
- `::first-letter`
- `::first-line`

**Examples**

	a:link { color: blue; }
	a:hover, a:focus { color: green; }
	main p:first-child { font-weight: bold; }
	main.first-child::first-letter { font-size: 120%; }

**Make a rule important**

	.highlight {
		font-weight: bold !important;
	}

**Styline fonts**

- `font-style` - normal, italic, oblique
- `font-weight` - normal, bold, bolder, lighter
- `font-variant` - normal or small caps
- `line-height`
- `text-indent`
- `text-align` - left, center, right, justify
- `vertical-align`
- `text-decoration` - underline, overline, line-through, none