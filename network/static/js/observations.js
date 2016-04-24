$(document).ready(function() {
    'use strict';

    // Satellite Filters
    $('#satellite-selection').bind('keyup change', function() {
        $('#satellite-filter').submit();
    });
    if ($('#satellite-selection').val()) {

        $('#collapseFilters').show();
    }

    // Data Filters
    var button = $('#collapseFilters button');
    $(button).click(function() {
        $(this).toggleClass('active');
        check_collapse($(this).attr('aria-controls'));
    });


});
