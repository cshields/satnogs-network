$(document).ready(function() {
    'use strict';

    var mapboxid = $('div#map').data('mapboxid');
    var mapboxtoken = $('div#map').data('mapboxtoken');

    L.mapbox.accessToken = mapboxtoken;
    L.mapbox.config.FORCE_HTTPS = true;
    var map = L.mapbox.map('map', mapboxid, {
        zoomControl: false
    }).setView([40, 0], 3);
    var LocLayer = L.mapbox.featureLayer().addTo(map);

    $('#successful a.toggle').click(function (e) {
        e.preventDefault();
        $(this).tab('show');
    })

    $.ajax({
        url: '/api/stations/?format=json'
    }).done(function(data) {
        data.forEach(function(m) {
            L.mapbox.featureLayer({
                type: 'Feature',
                geometry: {
                    type: 'Point',
                    coordinates: [
                      parseFloat(m.lng),
                      parseFloat(m.lat)
                    ]
                },
                properties: {
                    title: m.name,
                    'marker-size': 'large',
                    'marker-color': '#666',
                }
            }).addTo(map);
        });
    });
});
