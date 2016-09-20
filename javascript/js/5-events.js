function prepareEventHandlers() {
    
    var myListItem1 = document.getElementById("item1");
    myListItem1.onclick = function() {
    console.log("You clicked list item 1.");
    }

    var myListItem2 = document.getElementById("item2");
    myListItem2.onclick = function() {
    console.log("You clicked list item 2.");
    }
}

window.onload = function() {
    // prep anything we need to
    prepareEventHandlers();
}