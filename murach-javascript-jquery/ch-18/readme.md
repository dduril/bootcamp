## JavaScript and jQuery 

### Closures, IIFEs, Module Pattern, and Plugins

**About these pages:** *Notes and code samples from **[Murach's JavaScript and jQuery, 3rd Edition](https://www.murach.com/shop-books/web-development-books/murach-s-javascript-and-jquery-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**Closure example**

    $(document).ready(function(){
        var createClickCounter = function() {
            var count = 0;
        
            var clickCounter = function() {
                count++;
                console.log(this.id + " count is " + count);
            };
        
            return clickCounter;
        };
        
        $("#first_button").click(createClickCounter());
        $("#second_button").click(createClickCounter());
    });
    
    

**Immediately invoked function expression (IIFE))**

    // function expression defined and then invoked
    var sayHelloWorld = function() {
        console.log("Hello World!");
    };
    
    sayHelloWorld();
    
    // immediately invoked function expression
    (function() {
        console.log("Hello World!");
    })();

**Module pattern example**

    // create the namespace used by the application
    var myapp = myapp || {};

    // create the slideshow object and add it to the namespace
    myapp.slideshow = (function() {
        .
        .
        .
    })(); // Invoke the IIFE
