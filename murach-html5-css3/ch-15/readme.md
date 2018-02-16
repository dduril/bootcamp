## HTML5 and CSS3

### JavaScript and jQuery

**About these pages:** *Notes and code samples from **[Murach's HTML5 and CSS3, 3rd Edition](https://www.murach.com/shop/murachs-html5-and-css3-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**External JavaScript in the head section**

    <script src="assets/js/register_form.js"></script>

**JavaScript embedded in the head**

    <script>
        var today = new Date();
        document.write("The current date is: " + today.toDateString());
    </script>

**JavaScript embedded in the body**

    <p>
        <script>
            var today = new Date();
            document.write("The current date is: " + today.toDateString());
        </script>
    </p>
    
**DOM nodes**

- `Element`
- `Attr`
- `Text`


**Document object methods**

- `getElementById(id)`
- `write(string)`

**Example**

    var firstName = document.getElementById("first_name");

**DOM properties for scripting

- `value`
- `firstChild`
- `nodeValue`

**Example**

    var $ = function(id) {
        return document.getElementById(id);    
    }
    
    var firstName = $("first_name").value;
    
    $("first_name_error").firstChild.nodeValue = "Please enter first name.";
    
