d3.csv("static/data/Kaggle_TwitterUSAirlineSentiment.csv", function(error, data) {
    if (error) throw error;
    console.log(data);
    data.forEach(function(d) {
        d.airline_sentiment = d.airline_sentiment;
        d.airline_sentiment_confidence = d.airline_sentiment_confidence;
        d.negativereason = d.negativereason;
        d.airline = d.airline;
        d.name = d.name;
        d.text = d.text;
        d.tweet_created = d.tweet_created;
        d.tweet_location = d.tweet_location;
    });

    // Group data by airline and sentiment
    var groupedData = d3.nest()
        .key(function(d) { return d.airline; })
        .key(function(d) { return d.airline_sentiment; })
        .rollup(function(leaves) { return leaves.length; })
        .entries(data);

    // Prepare data for bar chart
    var chartData = [];
    groupedData.forEach(function(d) {
        var airline = d.key;
        d.values.forEach(function(sentiment) {
            var sentimentValue = sentiment.key;
            var count = sentiment.value;
            chartData.push({ airline: airline, sentiment: sentimentValue, count: count });
        });
    });

    // Set up chart dimensions
    var margin = { top: 20, right: 20, bottom: 30, left: 40 };
    var width = 600 - margin.left - margin.right;
    var height = 400 - margin.top - margin.bottom;

    // Create SVG element
    var svg = d3.select("body")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // Set up scales
    var xScale = d3.scaleBand()
        .range([0, width])
        .padding(0.1)
        .domain(chartData.map(function(d) { return d.airline; }));

    var yScale = d3.scaleLinear()
        .range([height, 0])
        .domain([0, d3.max(chartData, function(d) { return d.count; })]);

    // Create bars
    svg.selectAll(".bar")
        .data(chartData)
        .enter()
        .append("rect")
        .attr("class", "bar")
        .attr("x", function(d) { return xScale(d.airline); })
        .attr("y", function(d) { return yScale(d.count); })
        .attr("width", xScale.bandwidth())
        .attr("height", function(d) { return height - yScale(d.count); })
        .attr("fill", function(d) {
            if (d.sentiment === "positive") {
                return "green";
            } else if (d.sentiment === "negative") {
                return "red";
            } else {
                return "gray";
            }
        });

    // Add x-axis
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(xScale));

    // Add y-axis
    svg.append("g")
        .call(d3.axisLeft(yScale));
});

// Add chart title
svg.append("text")
    .attr("x", (width / 2))
    .attr("y", 0 - (margin.top / 2))
    .attr("text-anchor", "middle")
    .style("font-size", "16px")
    .text("Airline Sentiment");

// Add chart legend
var legend = svg.selectAll(".legend")
    .data(chartData.map(function(d) { return d.sentiment; }))
    .enter()
    .append("g")
    .attr("class", "legend")
    .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

legend.append("rect")
    .attr("x", width - 18)
    .attr("width", 18)
    .attr("height", 18)
    .style("fill", function(d) {
        if (d === "positive") {
            return "green";
        } else if (d === "negative") {
            return "red";
        } else {
            return "gray";
        }
    });

legend.append("text")
    .attr("x", width - 24)
    .attr("y", 9)
    .attr("dy", ".35em")
    .style("text-anchor", "end")
    .text(function(d) { return d; });
