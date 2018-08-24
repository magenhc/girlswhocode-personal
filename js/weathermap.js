// 1 declare map as a global variable so you can reference it later on.
// 2 moody location variable
// 3 view of home
var map;
var moodys = ol.proj.fromLonLat([-74.012, 40.713428]);
var homeView = new ol.View({
  center: ol.proj.fromLonLat([-74.012, 40.713428]),
  zoom: 15,
});


function moveToCountry(){
  var countryName = document.getElementById("country-name").value;
  console.log(document);
  console.log(document.getElementById("country-name"));
  console.log(document.getElementById("country-name").value);

// triple equal sign
  if(countryName === ""){
    panHome();
    return;
  }

}
/*
info for the home location
7 World Trade Center, New York, NY 10006, USA
latitude: 40.713428 | longitude: -74.012
*/

function panHome(){
  homeView.animate({
        center: moodys,
        duration: 2000
  });
}

function init() {
    map = new ol.Map({
          target: 'map',
          layers: [
            new ol.layer.Tile({
              source: new ol.source.OSM()
            })
          ],
          loadTilesWhileAnimating:true,
          view: homeView,
        });
}





window.onload = init;
