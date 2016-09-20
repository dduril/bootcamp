// working with the DOM
var myElement = document.getElementById("myFirstList");
console.log("This is an element of type: " + myElement.nodeType);
console.log("This is an element of type: " + myElement.nodeName);
console.log("Th inner HTML is: " + myElement.innerHTML);
console.log("Child nodes: " + myElement.childNodes.length);

var myListItems = document.getElementsByTagName("li");
console.log("List items: " + myListItems.length);

var mySecondList = document.getElementById("mySecondList");
var myListItems = mySecondList.getElementsByTagName("li");
console.log("List items: " + myListItems.length);


// changing DOM content
header = document.getElementById("header");
console.log(header.innerHTML);

header.innerHTML = "Working with the DOM";

myListItems[0].innerHTML = "Apples";
myListItems[1].innerHTML = "Bananas";
myListItems[2].innerHTML = "Cherries";


// creating DOM content - example 1
var myNewElement = document.createElement("li");
var myText = document.createTextNode("List item 4");
myNewElement.appendChild(myText);
myFirstList.appendChild(myNewElement);


// creating DOM content - example 2
// create the elements
var newHeading = document.createElement("h2");
var newParagraph = document.createElement("p");

// create child nodes
var h2Text = document.createTextNode("New Section");
var paraText = document.createTextNode("This is some new content added to the DOM.");

// add child nodes to the new elements
newHeading.appendChild(h2Text);
newParagraph.appendChild(paraText);

// attach new elements to the document
document.getElementById("mainContent").appendChild(newHeading);
document.getElementById("mainContent").appendChild(newParagraph);


// creating DOM content - example 3
// create element, child node and append child node to element
var myNewElement = document.createElement("li");
var liText = document.createTextNode("List item 1.5");
myNewElement.appendChild(liText);

// get a handle on the second item in the first list
var secondItem = myFirstList.getElementsByTagName("li")[1];

// insert the new list element before the second item
myElement.insertBefore(myNewElement, secondItem);