## HTML5 and CSS3

#### CSS for Page Layouts

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
