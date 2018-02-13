## HTML5 and CSS3

### Forms

**About these pages:** *Notes and code samples from **[Murach's HTML5 and CSS3, 3rd Edition](https://www.murach.com/shop/murachs-html5-and-css3-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**Form Element Attributes**

- `name`
- `action`
- `method`
- `target`

**Input Element Attributes**

- `type`
- `name`
- `disabled`
- `readonly`

**Examples**

Simple Form

	<form name="registration_form" action="register.php" method="post">
		<p>Name: <input type="text" name="name"></p>
		<p>
			<input type="submit" name="submit" value="Register">&nbsp;
			<input type="reset" name="reset" value="Reset">
		</p>
	</form>

Login Form

	<form name="login_form" action="login.php" method="post">
		<p>Username: <input type="text" name="user_name" autofocus></p>
		<p>Password: <input type="password" name="pass_word" placeholder="Enter your password" maxlength="12"></p>
		<p>
			<input type="submit" name="submit" value="Register">&nbsp;
			<input type="reset" name="reset" value="Reset">
		</p>
	</form>

Radio buttons

	Framework:<br>
		<input type="radio" name="framework" value="AngularJS">AngularJS<br>
		<input type="radio" name="framework" value="ReactJS">ReactJS<br>
		<input type="radio" name="framework" value="Vue.js">Vue.js<br><br>
	

Check boxes

	Database:<br>
		<input type="checkbox" name="database1" value="Cassandra">Cassandra<br>
		<input type="checkbox" name="database2" value="MongoDB">MongoDB<br>
		<input type="checkbox" name="database3" value="Redis">Redis<br><br>

Drop-down list

	Language:<br>
		<select name="programming_language">
			<option value="Java">Java</option>
			<option value="Python">Python</option>
			<option value="Ruby">Ruby</option>
		</select>

List box

	<select name="interests" size="5" multiple>
		<option value="Big Data">Big Data</option>
		<option value="Cloud">Cloud</option>
		<option value="Internet of Things">Internet of Things</option>
		<option value="Mobile">Mobile</option>
		<option value="Social Media">Social Media</option>
	</select>

Text area

	Comments:<br>
	<textarea name="comments"
		placeholder="Please leave your comments.">
	</textarea>

Using label elements

	<label for="first_name">First Name:</label>
	<input type="text" name="first_name" id="first_name"><br>
	<label for="last_name">Last Name:</label>
	<input type="text" name="last_name" id="last_name"><br>

Using fieldset and legend

	<form name="register" action="register.php" method="post">
	<fieldset>
		<legend>Account Information</legend>
		<label for="first_name">First Name:</label>
		<input type="text" name="first_name" id="first_name"><br>
		<label for="last_name">Last Name:</label>
		<input type="text" name="last_name" id="last_name"><br>
	</fieldset>
	</form>



