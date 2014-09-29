function AreaChart(selection) {

    var margin = {
            top: 20,
            right: 50,
            bottom: 50,
            left: 50
        },
        width = 800 - margin.left - margin.right,
        height = 300 - margin.top - margin.bottom;

    var x = d3.time.scale()
        .range([0, width]);

    var y = d3.scale.linear()
        .range([height, 0]);

    var color = d3.scale.category20();

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left");

    var area = d3.svg.area()
        .x(function(d) {
            return x(d.date);
        })
        .y0(function(d) {
            return y(0);
        })
        .y1(function(d) {
            return y(0 + d.y);
        });

    var line = d3.svg.line()
        .x(function(d) {
            return x(d.date);
        })
        .y(function(d) {
            return y(d.y);
        });

    var stack = d3.layout.stack()
        .values(function(d) {
            return d.values;
        });

    var adjustXAxis = function(daysSpan) {
        if (daysSpan <= 7) {
            xAxis.ticks(d3.time.days, 1)
        } else if (daysSpan <= 4 * 7) {
            xAxis.ticks(d3.time.days, 3)
        } else {
            xAxis.ticks(d3.time.weeks, 1)
        }
    };

    var chart = {

        draw: function(chartData) {

            var svg = d3.select(selection).append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
                .append("g")
                .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

            color.domain(chartData.getColorDomain());

            x.domain(chartData.getXDomain());

            y.domain(chartData.getYDomain());

            adjustXAxis(chartData.getXDaysSpan());

            var series = svg.selectAll(".series")
                .data(chartData.getAreaSeries())
                .enter().append("g")
                .attr("data-legend", function(d) {
                    return d.name;
                })
                .attr("data-legend-color", function(d) {
                    return color(d.name);
                })
                .attr("class", "series");

            series.append("path")
                .attr("class", "area")
                .attr("d", function(d) {
                    return area(d.values);
                })
                .style("fill", function(d) {
                    return color(d.name);
                });

            svg.append("path")
                .datum(chartData.getLineSeries())
                .attr("class", "line")
                .attr("d", line)
                .style("stroke-dasharray", ("10, 5"))
                .style("stroke", "#2C3E50")
                .style("stroke-width", 3);

            svg.append("g")
                .attr("class", "x axis")
                .attr("transform", "translate(0," + height + ")")
                .call(xAxis).selectAll("text")
                .attr("y", 10)
                .attr("x", 9)
                .attr("dy", ".35em")
                .attr("transform", "rotate(30)")
                .style("text-anchor", "start");

            svg.append("g")
                .attr("class", "y axis")
                .call(yAxis);

            svg.append("g")
                .attr("class", "legend")
                .attr("transform", "translate(" + (width - 100) + ",0)")
                .style("font-size", "1.2em")
                .call(d3.legend);
        }
    };


    return chart;
}
