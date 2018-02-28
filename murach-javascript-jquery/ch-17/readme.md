## JavaScript and jQuery 

### Custom Objects

**About these pages:** *Notes and code samples from **[Murach's JavaScript and jQuery, 3rd Edition](https://www.murach.com/shop-books/web-development-books/murach-s-javascript-and-jquery-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**Create object examples**

    //Date type
    var today = new Date();
    
    // String type
    var name = "John Smith";
    
    // Number type
    var sales_price = 12.95;
    
    // Boolean type
    var valid_flag = true;
    
    // Array type
    var movies = [];
    
    // Function type
    var add_numbers = function(x, y) {
        return x + y;
    }
    
**Initialize a new object with a property**

    var invoice = { tax_rate: 0.0975; }

**Initialize a new object with a method**

    var invoice = {
        getTotal: function(sub_total, sales_tax) {
            return sub_total + sales_tax;
        }
        
    }

**Initialize a new object with properties and methods**

    var invoice = {
        tax_rate: 0.0975;
        getSalesTax: function(sub_total) {
            return (sub_total * this.tax_rate; )
        }
        getTotal: function(sub_total) {
            return sub_total + this.getSalesTax(sub_total);
        }
    }
    
    // usage
    console.log(invoice.tax_rate);
    var salesTax = invoice.getSalesTax(200);
    var invoice_total = invoice.getTotal(200);
    
**JavaScript library example**

    // library file (library_mpg.js)
    "use strict";
    var mpg = {
        miles: 0,
        gallons: 0,
        isValid: function() {
            if ( isNaN(this.miles) || isNaN(this.gallons) ) {
                return false;
            } else if ( this.miles <= 0 || this.gallons <= 0 ) {
                return false;
            } else {
                return true;
            }
        },
        calculate: function() {
            var mpg = this.miles / this.gallons;
            return mpg.toFixed(1);
        }
    };
    
    
    // include js library in index.html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Calculate MPG</title>
        <link rel="stylesheet" href="mpg.css">
        <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
        <script type="text/javascript" src="library_mpg.js"></script>
        <script type="text/javascript" src="main.js"></script>
    </head>
    <body>
        <main>
            <h1>Calculate Miles Per Gallon</h1>
            <label for="miles">Miles Driven:</label>
                <input type="text" id="miles"><br>
            <label for="gallons">Gallons of Gas Used:</label>
                <input type="text" id="gallons"><br>
            <label for="mpg">Miles Per Gallon</label>
                <input type="text" id="mpg" disabled><br>

            <input type="button" id="calculate" value="Calculate MPG">
            <input type="button" id="clear" value="Clear">
        </main>
    </body>
    </html>
    
    // using js library in main.js
    "use strict";
    $( document ).ready(function() {
        $("#calculate").click( function() {
            mpg.miles = parseFloat( $("#miles").val() );
            mpg.gallons = parseFloat( $("#gallons").val() );
            if ( !mpg.isValid() ) {
                alert("Both entries must be numeric and greater than zero");
            } else {
               $("#mpg").val( mpg.calculate() ); 
               $("#miles").select();
            }
        });

        $("#clear").click( function() {
            $("#miles").val( "" );
            $("#gallons").val( "" );
            $("#mpg").val( "" );

            $("#miles").focus();
        });

        $("#miles").focus();
    });