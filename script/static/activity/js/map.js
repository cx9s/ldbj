mapboxgl.accessToken = 'pk.eyJ1Ijoia3lvMTE2IiwiYSI6IkN5QVlHVjAifQ.jxSEL4lJ0RbCSXmBg4cDZw';

var filterGroup = document.getElementById('filter-group');
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/basic-v9',
    center: [-30, 40],
    zoom: 1
});

// shared doms
//var slider = document.getElementById('slider');
var yearSelect = document.getElementById('year');
var monthSelect = document.getElementById('month');
var switchB = document.getElementById('switch');
var filterGroup = document.getElementById('legend-group');
var template = document.querySelector('#legend');
var label = template.content.querySelector('label');
var input = template.content.querySelector('input');
var span = template.content.querySelector('span');
var bar = template.content.querySelector('.bar');

var color;
var iniYear = 2015;
var iniMonth = 12;

//set time selection
var iyear = 2000,
    imonth = 1;
for (iyear; iyear < 2016; iyear++){
    var opt = document.createElement('option');
    opt.id = 'year' + iyear;
    opt.value = opt.text = iyear;
    yearSelect.appendChild(opt);
}
for (imonth; imonth < 13; imonth++){
    var opt = document.createElement('option');
    opt.id = 'month' + imonth;
    opt.value = opt.text = imonth;
    monthSelect.appendChild(opt);
}
document.getElementById('year'+iniYear).setAttribute('selected',true);
document.getElementById('month'+iniMonth).setAttribute('selected',true);

// render map
map.on('load', function () {
    // color generator
    color = new Color();
    // Here we're using d3 to help us make the ajax request but you can use
    // Any request method (library or otherwise) you wish.
        d3.json('https://raw.githubusercontent.com/cx9s/innovation_data/master/res1.geojson?token=AVlBMbAK1mABkUWKvkEgQw0pQUtWpXUYks5ZsmuRwA%3D%3D  ', function (err, data) {
        //if (err) throw err;
        // Create a month property value based on time
        // used to filter against.
        //                data.features = data.features.map(function (d) {
        //                    d.properties.year = new Date(d.properties.time).getFullYear();
        //                    return d;
        //                });

        map.addSource('places', {
            'type': 'geojson',
            'data': data
        });

        data.features.forEach(function (feature) {
            var symbol = feature.properties['funding_round_type'];
            //console.log(symbol);
            var circleLayerId = symbol + '-circles',
                labelLayerId = symbol + '-labels';

            // Add a layer for this symbol type if it hasn't been added already.
            if (!map.getLayer(circleLayerId)) {
                //console.log(symbol);
                renderLayer(symbol);
                addControl(symbol);
            }
        });

        componentHandler.upgradeDom();

    });
});

function renderLayer(symbol) {

    var circleLayerId = symbol + '-circles';
        //labelLayerId = symbol + '-labels';

    map.addLayer({
        'id': circleLayerId,
        'type': 'circle',
        'source': 'places',
        'paint': {
            'circle-color': {
                property: 'funding_round_type',
                type: 'categorical',
                stops: [
                    ['venture', '#fbb03b'],
                    ['seed', '#16A085'],
                    ['debt_financing', '#e55e5e'],
                    ['angel', '#4776E6'],
                    ['others', '#333333']]
            },
            'circle-opacity': 0.75,
            /**'circle-radius': {
                base: 2,
                stops: [
                    [1, 5],
                    [5, 30]
                ]
            }**/
            'circle-radius': {
                property: "raised_amount_usd",
                type: "exponential",
                base: 2,
                stops:[
                    [{zoom: 1, value: 10000}, 4],
                    [{zoom: 1, value: 100000000}, 35],
                    [{zoom: 5, value: 10000}, 16],
                    [{zoom: 5, value: 100000000}, 140]
                ]
            }
        },
        "filter": ["all", ["==", "funding_round_type", symbol]]
    });

    /**map.addLayer({
        'id': labelLayerId,
        'type': 'symbol',
        'source': 'places',
        'layout': {
            'text-field': amount/1000+'',
            'text-font': ['Open Sans Bold', 'Arial Unicode MS Bold'],
            'text-size': 12
        },
        'paint': {
            'text-color': 'rgba(0,0,0,0.5)'
        },
        "filter": ["all", ["==", "funding_round_type", symbol]]
    });**/


    // When a click event occurs on a feature in the places layer, open a popup at the
    // location of the feature, with description HTML from its properties.
    map.on('click', circleLayerId, function (e) {
        new mapboxgl.Popup()
            .setLngLat(e.features[0].geometry.coordinates)
            .setHTML(
                '<b>Company:</b> ' + e.features[0].properties.company_name + '</br>' +
                //'<b>category:</b> ' + e.features[0].properties.company_category_list + '</br>' +
                '<b>City: </b>' + e.features[0].properties.company_city + ' ('+ e.features[0].properties.company_country_code+ ')</br>' +
                '<b>Amount ($): </b>' + (e.features[0].properties.raised_amount_usd)/1000 + 'K'
            )
            .addTo(map);
    });

    // Change the cursor to a pointer when the mouse is over the places layer.
    map.on('mouseenter', circleLayerId, function () {
        map.getCanvas().style.cursor = 'pointer';
    });

    // Change it back to a pointer when it leaves.
    map.on('mouseleave', circleLayerId, function () {
        map.getCanvas().style.cursor = '';
    });


    // Set filter to first month of the year
    // 0 = January
    filterBy(iniYear, iniMonth, symbol);
}

function addControl(symbol) {

    var circleLayerId = symbol + '-circles',
        labelLayerId = symbol + '-labels';

    switchB.addEventListener('click', function (e) {
        filterBy(yearSelect.value, monthSelect.value, symbol);
    });

    // Add checkbox and label elements for the layer.
    label.for = input.id = symbol;
    span.textContent = span.id = symbol;
    filterGroup.appendChild(document.importNode(template.content, true));
    // When the checkbox changes, update the visibility of the layer.
    document.getElementById(symbol).addEventListener('change', function (e) {
        map.setLayoutProperty(circleLayerId, 'visibility',
            e.target.checked ? 'visible' : 'none');
        //map.setLayoutProperty(labelLayerId, 'visibility',
        //    e.target.checked ? 'visible' : 'none');
    });

}

function filterBy(year, month, symbol) {
    var yearfilter = ['==', 'funded_at', year + "-" + month];
    var filters = map.getFilter(symbol + '-circles');
    filters[2] = yearfilter;
    map.setFilter(symbol + '-circles', filters);
    //map.setFilter(symbol + '-labels', filters);

    // Set the label to the month
    //document.getElementById('year').textContent = parseInt(year + 2000) + "-" + parseInt(month);
}

map.addControl(new mapboxgl.FullscreenControl());

//pop up a click tips
var popup = new mapboxgl.Popup()
    .setLngLat([-74.00390625,40.71395582628605])
    .setHTML('<b>Company:</b> Peloton</br><b>City:</b> New York (USA)</br><b>Amount ($):</b> 75000K')
    .addTo(map);