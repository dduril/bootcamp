$(document).ready(function () {

    $.getJSON('/movie-api', printTerms);
    $('form').submit(function (e) {
        e.preventDefault();
        $.post('/movie-api', {Title: $('#Title').val(), Year : $('#Year').val()}, printTerms);
        this.reset();
    });

});


function printTerms(terms) {
    $('body>dl').empty();
    $.each(terms, function () {
        $('<dt>').text(this.Title).appendTo('body>dl');
        $('<dd>').text(this.Year).appendTo('body>dl');
    });
    $('dt').off('dblclick').dblclick(function() {
        $.ajax({
            url: '/movie-api/' + $(this).text(),
            type: 'DELETE',
            success: printTerms
        });
    });
}
