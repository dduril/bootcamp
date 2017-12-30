"use strict";
$(document).ready(function() {
    $("#lists h2").click(function(evt) {
        $(this).toggleClass("minus");
        if ($(this).attr("class") !== "minus") {
            $(this).next().hide();
        }
        else {
            $(this).next().show();
        }
        evt.preventDefault();
    }); // end click
    //$("#lists").find("a:first").focus();
}); // end ready