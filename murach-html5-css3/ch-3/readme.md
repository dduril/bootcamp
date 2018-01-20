## HTML5 and CSS3 

#### Structuring an HTML5 Page

Example making use of some of the HTML5 semantic elements: 

- `header`, `main`, `footer` 
- Ordered (`<ol>`) and unordered (`<ul>`) lists
- Hyperlinks (`<a href="">`)
- Basic styling 

#### Markup

	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <title>HTML5 : Sample Page</title>
	    <meta charset="UTF-8">
	    <meta name="description" content="A yearly meetup for front end developers">
	    <meta name="keywords" content="Angular, React, HTML5, CSS3, Bootstrap">
	    <link rel="stylesheet" href="style.css">
	</head>
	<body>
	    <header>
	        <h1>Silicon Valley Meetup | Front End Developers</h1>
	    </header>
	
	    <main>   
	        <h2>Introduction to HTML5 and CSS3</h2>
	        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vero fuga illum natus ex tempore esse aliquam architecto consequuntur molestiae facere!</p>
	        <ul>
	            <li>HTML5 Basics and Structure</li>
	            <li>CSS3 and Media Queries</li>
	            <li>Bootstrap Introduction</li>
	        </ul>
	        
	        <h2>Using Bootstrap 4 for Mobile-First Design</h2>
	        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nulla adipisci harum praesentium. Quam, optio totam magni facere, inventore natus nulla, deserunt unde incidunt deleniti possimus!</p>
	        <ol>
	            <li>Installing Node.js and npm</li>
	            <li>Using Templates and Themes</li>
	            <li>Quick Tour of the Brackets and VS Code Editors</li>
	        </ol>
	        <p>
	            This year's event will take place on: <time datetime="2017-12-15">December 15th</time>
	        </p>
	        
	        <p>Check out some of our other <a href="#">events</a>.</p>
	        <p>Read about the <a href="#">services we provide</a>.</p>
	    </main>
	    
	    <footer>
	        &copy; 2018
	    </footer> 
	</body>
	</html>
