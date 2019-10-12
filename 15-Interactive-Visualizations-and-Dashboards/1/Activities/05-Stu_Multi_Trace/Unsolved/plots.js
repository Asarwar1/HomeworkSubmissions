// console.log(data);
var trace1 = {
    x: data.map(row => row.pair),
    y: data.map(row => row.greekSearchResults),
    text: data.map(row => row.greekName),
    name: "Greek",
    type: " bar"
};

var trace2 = {
    x: data.map(row => row.pair),
    y: data.map(row.romanSearchResults),
    text: data.map(row => row.romanName),
    name: "Roman",
    type: "bar"
};

// Combining them 
var data = [trace1, trace2];

// Barmode application
var layout = {
    title: "Greek VS Roman Gods Search Results",
    barmode: "group"
};

Plotly.newPlot("plot", data, layout);

