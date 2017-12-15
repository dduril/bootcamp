/* javascript */
"use strict";

var $ = function(id) {
    return document.getElementById(id);
};

var joinList = function() {
    var emailAddress1 = $("email_address1").value;
    var emailAddress2 = $("email_address2").value;
    var firstName = $("first_name").value;
    var lastName = $("last_name").value;
    var errorMessage = "";
    
    if (emailAddress1 == "") {
        errorMessage = "First email address is required.";
        $("email_address1").focus();
    } 
    else if (emailAddress2 == "") {
        errorMessage = "Second email address is required.";
        $("email_address2").focus();
    }
    else if (emailAddress2 != emailAddress1) {
        errorMessage = "Email addresses must match.";
        $("email_address2").focus();
    } 
    else if (firstName == "") {
        errorMessage = "First name is required.";
        $("first_name").focus();
    }
    else if (lastName == "") {
        errorMessage = "Last name is required.";
        $("last_name").focus();
    }
    
    if (errorMessage == "") {
        // submit the form if all entries are valid
        $("email_form").submit();
    } else {
        alert(errorMessage);
    }
};

window.onload = function() {
    $("join_list").onclick = joinList;
    $("email_address1").focus();
};