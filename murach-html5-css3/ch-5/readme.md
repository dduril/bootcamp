## HTML5 and CSS3

### CSS Box Model

**About these pages:** *Notes and code samples from **[Murach's HTML5 and CSS3, 3rd Edition](https://www.murach.com/shop/murachs-html5-and-css3-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**Setting heights and widths**

- `width`
- `height`
- `min-width`
- `max-width`
- `min-height`
- `max-height`

**Example**

	body {
		width: 90%;
	}

**Setting margins**

- `margin-top`
- `margin-right`
- `margin-bottom`
- `margin-left`
- `margin`

**Example**

	.container {
		margin-top: .5em;
		margin-right: 1em;
		margin-bottom: .5em;
		margin-left: 1em;
	}
	
	.container {
		margin: .5em 1em .5em 1em;
	}

**Setting padding**

- `padding-top`
- `padding-right`
- `padding-bottom`
- `padding-left`
- `padding`

**Example**

	.container {
		padding-top: .75em;
		padding-right: 1em;
		padding-bottom: .5em;
		padding-left: 1em;
	}
	
	.container {
		padding: .75em 1em .5em 1em;
	}

**Setting borders**

- `border`
- `border-side`
- `border-width`
- `border-style`
- `border-color`
- `border-side-width`
- `border-side-style`
- `border-side-color`

**Example**

	.border {
		border: 1px solid #999;
	}

**Setting background color and image**

- `background`
- `background-color`
- `background-image`
- `background-repeat`
- `background-attachment`
- `background-position`

**Example**

	.background {
		backgroun-image: #ddd url("../assets/images/header.png") no-repeat scroll center top;
	}
