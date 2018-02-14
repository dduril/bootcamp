## JavaScript and jQuery 

### Forms and Data Validation

**About these pages:** *Notes and code samples from **[Murach's JavaScript and jQuery, 3rd Edition](https://www.murach.com/shop-books/web-development-books/murach-s-javascript-and-jquery-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**Form attributes**

- `name`
- `action`
- `method` - get or post

**HTML5 controls**

- `email`
- `url`
- `tel`
- `number`
- `range`
- `date`
- `time`

**HTML5 attributes**

- `autofocus`
- `placeholder`

**HTML5 data validation attributes**

- `required`
- `title`
- `pattern`
- `novalidate`
- `autocomplete`

**HTML form example**

    <form name="register" action="register.php" method="post">
	<fieldset>
		<legend>Account Information</legend>
        
		<label for="first_name">First Name:</label>
		<input type="text" name="first_name" id="first_name" autofocus required><br>
		
        <label for="last_name">Last Name:</label>
		<input type="text" name="last_name" id="last_name" required><br>
        
        <input type="submit" name="submit" id="register" value="Register">&nbsp;
        <input type="reset" name="reset" id="reset" value="Reset">
	</fieldset>
	</form>
    
**jQuery examples**

Get numeric value from text box

    var price = parseFloat($("#price").val());

Trim the value from a text box

    var firstName = $("#first_name").val().trim();

Get the value of a checked radio button

    var choice = $("input[name='contact_by]:checked").val();

Get an array of selected options from a list

    var selectOptions = [];
    selectOptions = $("select_list :selected");
