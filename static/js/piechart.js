d3.csv("static/data/Kaggle_TwitterUSAirlineSentiment.csv", function(error, data) {
    if (error) throw error;
    console.log(data);

    // Group the data by airline
    var airlineCount = d3.nest()
        .key(function(d) { return d.airline; })
        .rollup(function(v) { return v.length; })
        .entries(data);

    // Create an array of airline names and counts
    var airlines = airlineCount.map(function(d) { return d.key; });
    var counts = airlineCount.map(function(d) { return d.value; });

    // Set up the dimensions and radius of the pie chart
    var width = 400;
    var height = 400;
    var radius = Math.min(width, height) / 2;

    // Create the SVG element
    var svg = d3.select("body")
        .append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

    // Define the color scale
    var color = d3.scaleOrdinal(d3.schemeCategory10);

    // Create the pie layout
    var pie = d3.pie()
        .value(function(d) { return d; });

    // Generate the arcs
    var arc = d3.arc()
        .innerRadius(0)
        .outerRadius(radius);

    // Create the pie chart
    var arcs = svg.selectAll("arc")
        .data(pie(counts))
        .enter()
        .append("g");

    // Add the arcs
    arcs.append("path")
        .attr("d", arc)
        .attr("fill", function(d, i) { return color(i); });

    // Add the labels
    arcs.append("text")
        .attr("transform", function(d) { return "translate(" + arc.centroid(d) + ")"; })
        .attr("text-anchor", "middle")
        .text(function(d, i) { return airlines[i]; });
});

