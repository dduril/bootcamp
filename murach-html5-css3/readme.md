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

**External Style Sheet**

	<link rel="stylesheet" href="assets/styles/custom.css">

**Embedded Styles**

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

**Inline Styles**

	<h2 style="font-size: 125%; color: blue; padding-bottom: .5em;">Meeting Agenda</h2>

[[Top]](https://github.com/dduril/bootcamp/tree/master/murach-html5-css3#top)

#### HTML Basics<a name="html-basics"></a>

**Headings and Paragraphs**

- `h1` - Content in bold at 200% of the base font size
- `h2` - Content in bold at 150% of the base font size
- `h3` - Content in bold at 117% of the base font size
- `h4` - Content in bold at 100% of the base font size
- `h5` - Content in bold at 83% of the base font size
- `h6` - Content in bold at 67% of the base font size
- `p` - Paragraph of text at 100% of the base font size

**Ordered Lists**

**Unordered Lists**


[[Top]](https://github.com/dduril/bootcamp/tree/master/murach-html5-css3#top)