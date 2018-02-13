## HTML5 and CSS3

### Fonts and Printing

**About these pages:** *Notes and code samples from **[Murach's HTML5 and CSS3, 3rd Edition](https://www.murach.com/shop/murachs-html5-and-css3-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**Add css file with print styles**

    <link rel="stylesheet" href="assets/css/custom.css">
    <link rel="stylesheet" href="assets/css/print.css" media="print">
    
**Example**

    body {
        font-family: "Times New Roman", Times, serif;
        width: auto;
    }
    h1, h2 {
        font-family: Verdana, Arial, Helvetica, sans-serif;
    }
    /* navigation bar */
    #nav_menu {
        display: none;
    }
    /* sidebar */
    aside {
        display: none;
    }
    /* article */
    article {
        width: auto;
    }
    /* headers */
    header { 
        border-bottom: 2px solid black;
    }
    header h2 {
        color: black;
        font-size: 180%;
    }
    header h3 {
        color: black;
        font-size: 120%;
    }
    /* footer */
    footer {
        border-top: 2px solid black;
    }