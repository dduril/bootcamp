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