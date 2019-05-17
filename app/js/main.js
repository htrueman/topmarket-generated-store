"use strict";

$('.main-slider').slick({
    arrows: true,
});



$(document).ready(function($) {
    $('#accordion').find('.accordion-toggle').click(function(){

        //Expand or collapse this panel
        $(this).next().slideToggle('fast');

        //Hide the other panels
        $(".accordion-content").not($(this).next()).slideUp('fast');

    });
});

/* Cart - modal */


var modal = $('.modal');
$('.show-modal').click(function() {
    modal.fadeIn();
});

$('.close-modal').click(function() {
    modal.fadeOut();
});

/* Amount counter */

var numberSpinner = (function() {
    $('.number-spinner>.ns-btn>a').click(function() {
        var btn = $(this),
            oldValue = btn.closest('.number-spinner').find('input').val().trim(),
            newVal = 0;

        if (btn.attr('data-dir') === 'up') {
            newVal = parseInt(oldValue) + 1;
            console.log(oldValue);
        } else {
            if (oldValue > 1) {
                newVal = parseInt(oldValue) - 1;
                console.log(oldValue);
            } else {
                newVal = 1;
            }
        }
        btn.closest('.number-spinner').find('input').val(newVal);
    });
    $('.number-spinner>input').keypress(function(evt) {
        evt = (evt) ? evt : window.event;
        var charCode = (evt.which) ? evt.which : evt.keyCode;
        if (charCode > 31 && (charCode < 48 || charCode > 57)) {
            return false;
        }
        return true;
    });
})();

$('.delete').click(function() {
    console.log('here');
    $(this).closest('.cart-item').remove();
});

$('.delete').click(function() {
    console.log('here');
    $(this).closest('.cart-product-item').remove();
});


