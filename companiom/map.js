let map;

function initMap() {
  const center = { lat: 40.7128, lng: -74.0060 };

  map = new google.maps.Map(document.getElementById("map"), {
    center: center,
    zoom: 12,
  });

  let marker = new google.maps.Marker({
    position: center,
    map: map,
    title: "Campus Location",
  });
}