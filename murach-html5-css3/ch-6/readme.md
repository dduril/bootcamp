## HTML5 and CSS3

### CSS Page Layouts

**About these pages:** *Notes and code samples from **[Murach's HTML5 and CSS3, 3rd Edition](https://www.murach.com/shop/murachs-html5-and-css3-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**Floating and clearing elements**

- `float`
- `clear`

**Example**

	<style>
		* { margin: 0; padding: 0; }
        body {
            width: 90%;
            background-color: white;
            margin: 15px auto;
            border: 1px solid black;
        }
        main {
            height: 400px;
            width: 66%;
            float: left;
            border-right: 2px solid darkgray;
        }
        aside {
            width: 33%;
            float: right;
        }
        footer {
            clear: both;
            border-top: 2px solid darkgray;
        }
    </style>

**Positioning elements**

- `position`
	- `static`
	- `absolute`
	- `fixed`
	- `relative`
- `top`
- `bottom`
- `left`
- `right`
- `z-index`
