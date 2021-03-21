$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.slider').slider();
    $('.datepicker').datepicker({
        format: "mmmm, dd, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
});
