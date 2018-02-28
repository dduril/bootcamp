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

**Using push() and pop()**

    var names = ["HTML", "CSS", "JavaScript"];
    names.push("jQuery", "Bootstrap");
    var removed_name = names.pop();
    console.log(names.join());
    

**Using slice() and concat()**

    var names = ["HTML", "CSS", "JavaScript"];
    var name_slice = names.slice(0, 2);
    console.log(names.join(", "));
    
    var names_concat = names.concat(name_slice);
    console.log(names.concat.join());

**Using join() and toString()**

    var names = ["HTML", "CSS", "JavaScript", "Angular", "React"];
    console.log(names.join());
    console.log(names.join(", "));
    console.log(names.toString());
    
**Using the sort() method**

    var names = ["HTML", "CSS", "JavaScript", "Angular", "React"];
    names.sort();

**Using the map() method**

    var numbers = [1, 4, 9, 16, 25];
    var squared = numbers.map(function(value) {
        return value * value;
    });
    var root = numbers.map(Math.sqrt);
    

**Using the filter() method**

    var numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];
    var check_prime = function(value) {
        var is_prime = true;
        for (var i = 2; i < value; i++) {
            if (value % i === 0) {
                is_prime = false;
                break;
            }
        }
        return is_prime;
    };
    var prime = numbers.filter(check_prime);

**Using the split() method**

    var date = "3-1-2018";
    var date_parts = date.split("-");
    console.log(date_parts.length());
    console.log(date_parts.join("/"));

