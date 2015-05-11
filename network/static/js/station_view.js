$(document).ready(function() {
    // Reading data for station
    var station_info = $('#station-info').data();

    // Init the map
    'use strict';

    var mapboxid = $('div#map-station').data('mapboxid');
    var mapboxtoken = $('div#map-station').data('mapboxtoken');

    L.mapbox.accessToken = mapboxtoken;
    L.mapbox.config.FORCE_HTTPS = true;
    var map = L.mapbox.map('map-station', mapboxid,{
        zoomControl: false
    }).setView([station_info.lat, station_info.lng], 6);

    // Add a marker
    L.mapbox.featureLayer({
        type: 'Feature',
        geometry: {
            type: 'Point',
            coordinates: [
              parseFloat(station_info.lng),
              parseFloat(station_info.lat)
            ]
        },
        properties: {
            title: station_info.name,
            'marker-size': 'large',
            'marker-color': '#666',
        }
    }).addTo(map);
});
