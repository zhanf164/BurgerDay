var map = L.map('map', {center: L.latLng(40.74, -73.98), zoom: 12});

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {maxZoom: 18, attribution: '© OpenStreetMap'}).addTo(map);

//var Emily = L.marker([40.7294, -74.0039]).addTo(map);

//var PLuger = L.marker([40.7099, -73.9625]).addTo(map);

//var PJ = L.marker([40.75898, -73.96823]).addTo(map);


var markers = [{pos: [40.7294, -74.0039], popup: "Emily: West Village"}, 
                {pos: [40.6836, -73.9664], popup: "Emily: Clinton Hill (Brooklyn)"},
               {pos: [40.7099, -73.9625], popup: "Peter Luger's"},
               {pos:[40.75898, -73.96823], popup: "P.J. Clark's" }
]

markers.forEach(function (obj) {
    var m = L.marker(obj.pos).addTo(map),
    p = new L.Popup({autoClose: false, closeOnClick: false}).setContent(obj.popup).setLatLng(obj.pos);
    m.bindPopup(p).openPopup();
});


//Emily.bindPopup("Emily: West Village").openPopup();
//PLuger.bindPopup("Peter Lugers").openPopup();
//PJ.bindPopup("P.J. Clark's").openPopup();