## HTML5 and CSS3

### Images

**About these pages:** *Notes and code samples from **[Murach's HTML5 and CSS3, 3rd Edition](https://www.murach.com/shop/murachs-html5-and-css3-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**Image Types**

- JPEG - (Joint Photographic Experts Group) 
- GIF - (Graphic Interchange Format)
- PNG - (Portable Network Graphics)

**`<img>` attributes**

- `src`
- `alt`
- `height`
- `width`

**Example**

	<img src="/images/ceo.png" 
		alt="Chief Executive Office"
		height="400"
		width="400">

**Aligning images vertically**

- `vertical-align`
- Keywords for `vertical-align` property
	- `bottom`
	- `middle`
	- `top`
	- `text-bottom`
	- `text-top`

**Example**

	<p>
		<img src="/images/apple.png" alt="Apple">Apple
	</p>

	//css
	img {
		vertical-align: middle;
		margin-right: 10px;
	}

**Properties for floating images**

- `float`
- `clear`

**Example**

	<img src="/images/elephant.png" alt="Elephant">
	<p class="last">...</p>

	//css
	img {
		float: left;
		margin-top: 8px;
		margin-bottom: 12px;
	}
	.last {
		clear: left;
	}

