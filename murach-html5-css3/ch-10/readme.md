## HTML5 and CSS3

### Tables

**About these pages:** *Notes and code samples from **[Murach's HTML5 and CSS3, 3rd Edition](https://www.murach.com/shop/murachs-html5-and-css3-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**Table Elements**

- `<table>`
- `<tr>`
- `<th>`
- `<td>`

**Example**

	<table>
        <tr>
            <th>Title</th>
            <th>Released</th>
            <th>Runtime</th>
        </tr>   
        <tr>
            <td>Marvel's The Avengers</td>
            <td>2012</td>
            <td>143</td>
        </tr>
		...
	</table>

**Elements for header, bodt, and footer**

- `<thead>`
- `<tbody>`
- `<tfoot>`

**Example**

	<table>
		<thead>
			<tr>
				<th>Title</th>
				<th>Released</th>
				<th>Runtime</th>
				<th>US Gross</th>
			</tr>   
		</thead>
		<tbody>
			<tr>
				<td>Marvel's The Avengers</td>
				<td>2012</td>
				<td>143</td>
				<td>623,279,547</td>
			</tr>
			...    
		</tbody>
		<tfoot>
			<tr>
				<td>Total US Domestic Gross</td>
				<td>&nbsp;</td>
				<td>&nbsp;</td>
				<td>1,908,636,637</td>
			</tr>
		</tfoot>
	</table>

**Formatting Tables**

- `border-collapse`
- `border-spacing`
- `padding`
- `text-align`
- `vertical-align`

**CSS Example**

	table {
		border: 1px solid darkgray;
		border-collapse: collapse;
	}
	th, td {
		border: 1px solid darkgray;
		padding: .3em .5em;
		text-align: center;
	}
	th.left, td.left { text-align: left; }
	thead, tfoot { background-color: #eee; }
	tfoot { font-weight: bold; }

