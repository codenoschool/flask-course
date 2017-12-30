$(document).ready(function(){
    console.log('I am ready.');
    // get current URL path and assign 'active' class
    var pathname = window.location.pathname;
    $('.navbar-nav > li > a[href="'+pathname+'"]').parent().addClass('active');

    setTimeout(
        function(){
            $(".alert-success").alert('close');
        }, 2500
    );
    //$(".alert").alert('close');
});