var API_BASE_URL = "/api/report/";
var INITIAL_POSITION = [-31.4167753,-63.61836007];
var INITIAL_ZOOM = 10;
var MAP_OPTIONS = {};

var map, marker, postData={};

var setupMap = function () {
    map = L.map('map', MAP_OPTIONS).setView(INITIAL_POSITION, INITIAL_ZOOM);            
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, '
            +' <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, '
            +'Imagery © <a href="http://mapbox.com">Mapbox</a>',
    }).addTo(map);
};


var queryNominatim = function () {

    // Reverse streen and house number for OSM
    var value = $("#address").val()
    var re = /(.*)\s+([0-9]+)/;
    var data = re.exec(value);
    var street = data[1];
    var houseNumber = data[2];

    // Setup query
    var street = houseNumber + " " + street;
    var neighborhood = $("#neighborhood").val();
    var city = "Córdoba";
    var country = "Argentina";

    // Send to OSM
    var baseUrl = "http://nominatim.openstreetmap.org/?format=json&limit=1";
    var url = baseUrl + "&addressdetails=1" + "&street=" + street + "&city=" + neighborhood + " " + city + "&country=" + country;
    return $.getJSON(url, nominatimResponseReceived);
};


var nominatimResponseReceived = function (data) {
    var osmData = data[0];
    if (osmData) {
        setMapCenter(osmData.lat, osmData.lon, osmData.type);
        setMarker(osmData.lat, osmData.lon);
        postData.position = [osmData.lat, osmData.lon];
    }
};


var setMapCenter = function (lat, lng, type) {
    var latlng = new L.LatLng(lat, lng);
    map.panTo(latlng);
    if (type == "city" || type == "administrative") {
        map.setZoom(10);
    } 
    else {
        map.setZoom(15);
    }
};


var setMarker = function (lat, lng) {
    var latlng = new L.LatLng(lat, lng);
    if (!marker) {
        marker = L.marker(latlng).addTo(map);
    }
    else {
        marker.setLatLng(latlng);
    }
};


