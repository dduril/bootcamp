/* javascript */
var $ = function(id) {
    return document.getElementById(id);
};

var calcMPG = function() {
    var miles = parseFloat($("miles").value);
    var gallons = parseFloat($("gallons").value);
    
    var mpg = miles/gallons;
    
    if (isNaN(mpg)){
        alert("Please enter valid numbers for values.")
        resetForm();
    } else {
        alert("Miles per gallon = " + mpg);
        resetForm();
    }
    
};

function resetForm() {
    $("miles").value = "";
    $("gallons").value = "";
    $("miles").focus();
}

window.onload = function() {
    $("calc_mpg").onclick = calcMPG;
    $("miles").focus();
};
