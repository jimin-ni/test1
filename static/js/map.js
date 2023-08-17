window.initMap = function () {
  const map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 37.5400456, lng: 126.9921017 },
    zoom: 5,
  });

  const infowindow = new google.maps.InfoWindow();

  var searchBox = new google.maps.places.SearchBox(
    document.getElementById("pac-input")
  );

  google.maps.event.addListener(searchBox, "places_changed", function () {
    var places = searchBox.getPlaces();
    var bounds = new google.maps.LatLngBounds();

    places.forEach(function (place) {
      if (!place.geometry) {
        console.log("Returned place contains no geometry");
        return;
      }

      if (place.geometry.viewport) {
        bounds.union(place.geometry.viewport);
      } else {
        bounds.extend(place.geometry.location);
      }
    });

    map.fitBounds(bounds);
  });

  const malls = [
    {
      label: "",
      name: "일본, 도쿄",
      lat: 35.5042949,
      lng: 138.4503955,
      pageUrl: "/japan.html",
    },
    {
      label: "",
      name: "베트남, 하노이",
      lat: 21.022802,
      lng: 105.7590216,
      pageUrl: "/vietnam.html",
    },
    {
      label: "",
      name: "미국, 워싱턴DC",
      lat: 38.8939059,
      lng: -77.1793867,
      pageUrl: "/USA.html",
    },
  ];
  malls.forEach(({ label, name, lat, lng, pageUrl }) => {
    const marker = new google.maps.Marker({
      position: { lat, lng },
      label,
      map,
    });

    marker.addListener("click", () => {
      // 해당 마커가 클릭되었을 때 해당 페이지로 넘어가는 코드 추가
      window.location.href = pageUrl;
    });
  });
};
