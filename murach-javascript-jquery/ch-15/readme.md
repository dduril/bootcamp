## JavaScript and jQuery 

### Browser Objects, Cookies, and Web Storage

**About these pages:** *Notes and code samples from **[Murach's JavaScript and jQuery, 3rd Edition](https://www.murach.com/shop-books/web-development-books/murach-s-javascript-and-jquery-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**location object properties**

- `href`
- `protocol`
- `hostname`
- `port`
- `host`
- `path`
- `search`
- `hash`

**location object methods**

- `reload(force)`
- `replace(url)`

**Load a new web page**

    location.href = "http://www.google.com"
    location = "http://www.google.com"
    
**Reload a web page**

    location.reload();
    location.reload(true);
    
**Load a new web page and overwrite current history page**

    location.replace("http://www.google.com");

**history object property**

- `length`

**history object properties**

- `back()`
- `forward()`
- `go(position)`
- `go(substring)`

**Using the back() method**

    history.back();

**Using the forward() method**

    history.forward();

**Using the go() method**

    history.go(2);
    history.go(-2);
    history.go("google");

**cookie attributes**

- `max-age`
- `path`
- `domain`
- `secure`

**cookie functions**

- `encodeURIComponent(value)`
- `decodeURIComponent(value)`

**Create a session cookie**

    var cookie = "todo" + "=";
    cookie += encodeURIComponent("Update Meetups schedule\Review TED Talks");
    cookie += "; path=/";
    document.cookie = cookie;

**Create a persistent cookie**

    var cookie = "todo" + "=";
    cookie += encodeURIComponent("Update Meetups schedule\Review TED Talks");
    cookie += "; max-age=" + days * 24 * 60 * 60;
    cookie += "; path=/";
    document.cookie = cookie;

**Delete a cookie**

    var cookie = "tasks=";
    cookie += "; max-age=" + 0; 
    cookie += "; path=/";
    document.cookie = cookie;
    
**Web storage examples**

    // local storage
    localStorage.setItem("Tasks for Monday", "Update reading list");
    localStorage.getItem("Tasks for Monday");
    localStorage.removeItem("Tasks for Monday");
    localStorage.clear();
    
    // session storage
    sessionStorage.setItem("Tasks for Monday", "Update reading list");
    sessionStorage.getItem("Tasks for Monday");
    sessionStorage.removeItem("Tasks for Monday");
    sessionStorage.clear();