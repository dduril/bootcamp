## JavaScript and jQuery 

### jQuery Plugins

**About these pages:** *Notes and code samples from **[Murach's JavaScript and jQuery, 3rd Edition](https://www.murach.com/shop-books/web-development-books/murach-s-javascript-and-jquery-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**Resources**

- **[jQuery UI](https://jqueryui.com/)**
- **[jQuery UI Plugins](http://plugins.jquery.com/tag/ui/)**

**jQuery UI Features**

- Widgets
    - Accordion
    - Autocomplete
    - Button
    - Checkboxradio
    - Controlgroup
    - Datepicker
    - Dialog
    - Menu
    - Progressbar
    - Selectmenu
    - Slider
    - Spinner
    - Tabs
    - Tooltip
- Themes
    - ThemeRoller
- Interactions
    - Draggable
    - Droppable
    - Resizable
    - Selectable
    - Sortable
- Effects
    - Add Class
    - Color Animation
    - Easing
    - Effect
    - Hide
    - Remove Class
    - Show
    - Switch Class
    - Toggle
    - Toggle Class
    
**How to include jQuery and jQuery UI**

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>jQuery : jQuery UI - Accordion</title>
        
        <link rel="stylesheet" href="assets/styles/normalize.css">
        <link rel="stylesheet" href="style.css">
        <link rel="stylesheet" href="assets/styles/jquery-ui.min.css">

        <script src="assets/scripts/jquery-3.2.1.min.js"></script>
        <script src="assets/scripts/jquery-ui.min.js"></script>
        
        <script>
            $(document).ready(function() {
                $("#accordion").accordion(
                    { 
                    event: "mouseover",
                    heightStyle: "content",
                    collapsible: true 
                    });
            });
        </script>
    </head>