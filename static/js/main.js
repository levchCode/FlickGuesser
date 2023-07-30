let newMarker = {}
let lat = 0;
let lng = 0;

const map = L.map('map').setView([0, 0], 1);
const markerUrl = 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png'
    
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

map.on('click', function(e){
    var coord = e.latlng;
    lat = coord.lat;
    lng = coord.lng;
    
    if (newMarker != {}) {
        map.removeLayer(newMarker);
    }
    newMarker = new L.marker(e.latlng).addTo(map);
});

async function postData(url = '', data = {}) {

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    return response.json(); 
}

function guess() {
    postData('/guess', {}).then(data => {
        const greenIcon = new L.Icon({
            iconUrl: markerUrl,
            iconSize: [25, 41],
            iconAnchor: [12, 41],
            popupAnchor: [1, -34],
            shadowSize: [41, 41]
        });

        L.marker([data.coords.latitude, data.coords.longitude], {icon: greenIcon}).addTo(map);
    });
}