## JavaScript and jQuery 

### Arrays

**About these pages:** *Notes and code samples from **[Murach's JavaScript and jQuery, 3rd Edition](https://www.murach.com/shop-books/web-development-books/murach-s-javascript-and-jquery-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**Create an array**

    var product_codes = new Array(8, 15, 23, 34, 45);
    var departments = ["Accounting", "Human Resources", "Engineering"];
    
    var rates = new Array[4];
    rates[0] = 12.95;
    rates[1] = 18.35;
    rates[2] = 23.45;
    rates[3] = 30.15;
    
    var languages = [];
    names[0] = "HTML";
    names[1] = "CSS";
    names[2] = "JavaScript";
    names[3] = "jQuery";
    
**Working with array elements**

    // add an element to the end of an array
    var nums = [1, 3, 5, 7];
    numbers[numbers.length] = 9;
    
    // add an element to a specific index
    var nums = [1, 2, 3, 4];
    nums[4] = 5;
    
    // delete an element at a specific index
    var nums = [1, 2, 3, 4, 5];
    delete nums[2];
    
    // remove all elements from an array
    var nums = [2, 4, 6, 8, 10];
    nums.length = 0;
    
**Looping through an array with a for loop**

    // put the numbers 1 through 10 into an array
    var nums = [];
    for (var i = 0; i < 10; i++) {
        nums[i] = i + 1;
    }
    
    // display the nums array
    var num_string = "";
    for (var i = 0; i < nums.length, i ++) {
        num_string += nums[i] + " ";
    }
    document.write("nums array: " + num_string);
    
**Using a for-in loop**

    var nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    var num_string = "";
    for (var index in nums) {
        num_string += nums[i] + " ";
    }
    document.write("nums array: " + num_string);
    
**Array object methods**

- `push(element_list)`
- `pop()`
- `unshift(element_list)`
- `shift()`
- `reverse()`
- `splice(start, number)`
- `splice(start, number, element_list)`
- `slice(start, number)`
- `concat(array_list)`
- `join([separator])`
- `toString()`
- `toLocaleString()`
- `isArray(object)`
- `indexOf(value, start)`
- `lastIndexOf(value, start)`

**Array object methods that accept functions as parameters**

- `sort([comparison_function])`
- `forEach(function, this)`
- `every(function, this)`
- `some(function, this)`
- `map(function, this)`
- `filter(function, this)`
- `reduce(function, init)`
- `reduceRight(function init)`

