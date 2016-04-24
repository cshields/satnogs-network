$(document).ready(function() {
    'use strict';

    var observation_start = 1000 * $('#observation-info').data('start');
    var observation_end = 1000 * $('#observation-info').data('end');

    var observation_data = [];

    var formatTime = function(timeSeconds) {
        var minute = Math.floor(timeSeconds / 60); // get minute(integer) from timeSeconds
        var tmp = Math.round(timeSeconds - (minute * 60)); // get second(integer) from timeSeconds
        var second = (tmp < 10 ? '0' : '') + tmp; // make two-figured integer if less than 10

        return String(minute + ':' + second); // combine minute and second in string
    };

    $('.observation-data').each(function( index ){
        var $this = $(this);
        var data_groundstation = $this.data('groundstation');
        var data_time_start = 1000 * $this.data('start');
        var data_time_end = 1000 * $this.data('end');
        observation_data.push({label : data_groundstation, times : [{starting_time: data_time_start, ending_time: data_time_end}]});
    });

    var chart = d3.timeline()
                  .stack()
                  .beginning(observation_start)
                  .ending(observation_end)
                  .hover(function (d, i, datum) {
                      var div = $('#hoverRes');
                      var colors = chart.colors();
                      div.find('.coloredDiv').css('background-color', colors(i));
                      div.find('#name').text(datum.label);
                  })
                  .margin({left:140, right:10, top:0, bottom:50})
                  .tickFormat({format: d3.time.format.utc("%H:%M"), tickTime: d3.time.minutes, tickInterval: 30, tickSize: 6});

    var svg_width = 1140;
    if (screen.width < 1200) { svg_width = 940; }
    if (screen.width < 992) { svg_width = 720; }
    if (screen.width < 768) { svg_width = screen.width - 30; }
    var svg = d3.select("#timeline").append("svg").attr("width", svg_width)
                .datum(observation_data).call(chart);

    // Waveform loading
    $('.wave').each(function( index ){
        var $this = $(this);
        var wid = $this.data('id');
        var wavesurfer = Object.create(WaveSurfer);
        var data_payload_url = $this.data('payload');
        var container_el = '#data-' + wid;
        var loading = '#loading';
        var $playbackTime = $('#playback-time-' + wid);

        wavesurfer.init({
          container: container_el,
          waveColor: '#bf7fbf',
          progressColor: 'purple'
        });

        wavesurfer.on('loading', function() {
            $(loading).show();
        });

        $this.parents('.observation-data').find('.playpause').click( function(){
            wavesurfer.playPause();
        });

        wavesurfer.load(data_payload_url);

        wavesurfer.on('ready', function() {
            $playbackTime.text(formatTime(wavesurfer.getCurrentTime()));

            wavesurfer.on('audioprocess', function(evt) {
                $playbackTime.text(formatTime(evt));
            });
            wavesurfer.on('seek', function(evt) {
                $playbackTime.text(formatTime(wavesurfer.getDuration() * evt));
            });
            $(loading).hide();
        });
    });

    // Delete confirmation
    var message = "Do you really want to delete this Observation?";
    var actions = $('#obs-delete');
    if (actions.length) {
        actions[0].addEventListener("click", function(e) {
            if (! confirm(message)) {
                e.preventDefault();
            }
        });
    }

    // Initialize tooltips
    $('[data-toggle="tooltip"]').tooltip();
});
