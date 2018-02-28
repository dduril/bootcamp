"use strict";
$( document ).ready(function() {
    // create the slideshow object 
    var slideshow = createSlideshow();
    
    var slides = [
        {href:"barrels.jpg", title:"Barrels"}, 
        {href:"flowers.jpg", title:"Flowers"}, 
        {href:"fountain.jpg", title:"Fountain"},
        {href:"tractor.jpg", title:"Tractor"},
        {href:"winery.jpg", title:"Winery"}    
    ];
    
    $("#play_pause").click( slideshow.createToggleHandler() );  
    
    slideshow.loadImages(slides).startSlideShow( $("#image"), $("#caption") );
});