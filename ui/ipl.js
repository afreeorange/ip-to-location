$(document).ready(function() {

    var api_endpoint = 'https://nikhil.io/ip';
    var ips = window.location.href.split('?')[1];
    var url = ips ? api_endpoint + '/' + ips : api_endpoint;

    var overlay = Handlebars.compile($('#overlay-template').html());
    var overlay_info = Handlebars.compile($('#overlay-info-template').html());

    var lat_long_bounds = [];
    var map = new GMaps({
        div: '#map',
        lat: 0,
        lng: 0,
        zoom: 2
    });

    $.ajax({
            url: url
        })
        .done(function(response) {

            // Filter out valid IPs from response. $.grep() only works on lists
            for (ip in response) {
                if (response[ip].hasOwnProperty('error')) {
                    delete response[ip];
                }
            }

            // Check if there's anything to display
            if (Object.keys(response).length == 0) {
                $('#loading').text('nothing to show :(');
                $('#map').fadeTo('fast', 0.5);
                return false;
            }

            // Draw IPs on map
            for (ip in response) {
                var data_point = new google.maps.LatLng(response[ip].latitude,
                    response[ip].longitude
                );
                lat_long_bounds.push(data_point);

                map.drawOverlay({
                    lat: response[ip].latitude,
                    lng: response[ip].longitude,
                    content: overlay({
                        'ip': ip
                    }),
                    layer: 'overlayMouseTarget',
                    click: (function(ip) {
                            return function() {
                                $('#overlay-info').html(overlay_info(response[ip]));
                            }
                        })(ip) // Remember IP address at creation time
                });

                map.fitLatLngBounds(lat_long_bounds);
            }

            $('#loading').fadeOut();
        })
        .fail(function() {
            $('#loading').text('failed :(');
            $('#map').fadeTo('fast', 0.5);
        });
});
