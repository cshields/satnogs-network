$(function () {
    var minstart = $('#datetimepicker-start').data('date-minstart');
    var maxrange = $('#datetimepicker-end').data('date-maxrange');
    $('#datetimepicker-start').datetimepicker();
    $('#datetimepicker-start').data('DateTimePicker').minDate(moment.utc().add(minstart,'m'));
    $('#datetimepicker-end').datetimepicker();
    $('#datetimepicker-end').data('DateTimePicker').minDate(moment.utc().add(minstart,'m'));
    $("#datetimepicker-start").on('dp.change',function (e) {
        //Setting default, minimum and maximum for end
        $('#datetimepicker-end').data('DateTimePicker').defaultDate(moment.utc(e.date).add(60, 'm'));
        $('#datetimepicker-end').data('DateTimePicker').minDate(e.date);
        $('#datetimepicker-end').data('DateTimePicker').maxDate(moment.utc(e.date).add(maxrange, 'm'));
    });

    $('#satellite-selection').change( function() {
        var norad = $(this).find(':selected').data('norad');
        $('#transmitter-selection').prop('disabled', false);
        $('#transmitter-selection option').hide();
        $('#transmitter-selection option[data-satellite="'+norad+'"]').show().prop('selected', true);
    });
});

$( document ).ready( function(){
    $('#calculate-observation').click( function(){
        $('.calculation-result').show();
        $('#timeline').empty();
        $('#hoverRes').hide();
        $('#windows-data').empty();
        var satellite = $('#satellite-selection').val();
        var start_time = $('#datetimepicker-start input').val();
        var end_time = $('#datetimepicker-end input').val();

        $.ajax({
            url: '/prediction_windows/' + satellite + '/' + start_time + '/' + end_time + '/',
            beforeSend: function() { $('#loading').show(); }
        }).done(function(data) {
            $('#loading').hide();
            if (data['error']) {
                var error_msg = data['error'];
                $('#windows-data').html('<span class="text-danger">' + error_msg + '</span>');
            } else {
                var dc = 0; //Data counter
                var suggested_data = [];
                $('#windows-data').empty();
                $.each(data, function( i,k ){
                    label = k.id + ' - ' + k.name;
                    var times = [];
                    $.each(k.window, function( m,n ){
                        var starting_time = moment.utc(n.start).valueOf();
                        var ending_time = moment.utc(n.end).valueOf();
                        console.log(starting_time + '-' + ending_time);
                        $('#windows-data').append('<input type="hidden" name="'+dc+'-starting_time" value="'+n.start+'">');
                        $('#windows-data').append('<input type="hidden" name="'+dc+'-ending_time" value="'+n.end+'">');
                        $('#windows-data').append('<input type="hidden" name="'+dc+'-station" value="'+k.id+'">');
                        times.push({starting_time: starting_time, ending_time: ending_time})
                        dc = dc + 1;
                    });
                    suggested_data.push({label : label, times : times});
                });

                $('#windows-data').append('<input type="hidden" name="total" value="'+dc+'">');
                if (dc > 0) {
                    timeline_init(start_time, end_time, suggested_data);
                } else {
                    var error_msg = 'No Ground Station available for this observation window';
                    $('#windows-data').html('<span class="text-danger">' + error_msg + '</span>');
                }
            }
        });
    });
});

function timeline_init( start, end, payload ){
    var start_time_timeline = moment.utc(start).valueOf();
    var end_time_timeline = moment.utc(end).valueOf();

    $('#timeline').empty();
    $('.coloredDiv').css('background-color', 'transparent');
    $('#name').empty();

    var chart = d3.timeline()
                  .stack()
                  .beginning(start_time_timeline)
                  .ending(end_time_timeline)
                  .hover(function (d, i, datum) {
                      var div = $('#hoverRes');
                      var colors = chart.colors();
                      div.find('.coloredDiv').css('background-color', colors(i))
                      div.find('#name').text(datum.label);
                  })
                  .margin({left:140, right:10, top:0, bottom:50})
                  .tickFormat({format: d3.time.format('%H:%M'), tickTime: d3.time.minutes, tickInterval: 30, tickSize: 6});

    var svg = d3.select('#timeline').append('svg').attr('width', 1140)
                .datum(payload).call(chart);

    $('#hoverRes').show();
    $('#schedule-observation').removeAttr('disabled');
}
