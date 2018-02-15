## JavaScript and jQuery 

### Ajax and JSON

**About these pages:** *Notes and code samples from **[Murach's JavaScript and jQuery, 3rd Edition](https://www.murach.com/shop-books/web-development-books/murach-s-javascript-and-jquery-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**Ajax data formats**

- HTML
- XML
- JSON

**XML data**

    <?xml version="1.0" encoding="utf-8"?>
    <movies>
        <movie>
            <title>Akira</title>
            <released>1987</released>
            <rating>R</rating>
            <runTime>124</runTime>
        </movie>
    </movies>

**JSON data**

    {"Marvel Cinematic Universe":[
        {
        "title" : "Iron Man",
        "phase" : "Phase One: Avengers Assembled",
        "runtime" : 126,
        "rating" : "PG-13",
        "release_date" : "May 2, 2008"
        }
    ]}