"use strict";
$( document ).ready(function() {
    // create the slideshow object 
    var slideshow = myapp.slideshow; // use an alias to make code shorter
    
    var slides = [
        {href:"barrels.jpg", title:"Barrels"}, 
        {href:"flowers.jpg", title:"Flowers"}, 
        {href:"fountain.jpg", title:"Fountain"},
        {href:"tractor.jpg", title:"Tractor"},
        {href:"winery.jpg", title:"Winery"}  
    ];
    
    $("#play_pause").click( slideshow.createToggleHandler() );  
    $("#change_speed").click( function() {
        var ms = prompt( "Current speed is " 
            + slideshow.interval + " milliseconds.\n"
            + "Please enter a new speed in milliseconds."
       , 2000 );
        slideshow.changeSpeed(ms).startSlideShow();
    });
    $("#view_slides").click( function() {
        alert( slideshow.displaySlides() );
    });
    
    slideshow.loadImages(slides).startSlideShow( $("#image"), $("#caption") );
});