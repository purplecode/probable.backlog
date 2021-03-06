function AreaChart(selection, width, height) {

    var margin = {
            top: 30,
            right: 100,
            bottom: 50,
            left: 50
        },
        width = (width || 800) - margin.left - margin.right,
        height = (height || 300) - margin.top - margin.bottom;

    var x = d3.time.scale()
        .range([0, width]);

    var y = d3.scale.linear()
        .range([height, 0]);

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
                    return chartData.getColor(d.name);
                })
                .attr("class", "series");

            series.append("path")
                .attr("class", "area")
                .attr("d", function(d) {
                    return area(d.values);
                })
                .style("fill", function(d) {
                    return chartData.getColor(d.name);
                });

            _.each(chartData.getLinesSeries(), function(series) {
                svg.append("path")
                    .datum(series.points)
                    .attr("class", "line")
                    .attr("d", line)
                    .style("fill", "transparent")
                    .style("stroke-dasharray", ("10, 5"))
                    .style("stroke", series.color || "#2C3E50")
                    .style("stroke-width", 3);
            });

            _.each(chartData.getTextSeries(), function(series) {
                svg.append("text")
                    .style("font-size", "20px")
                    .attr("dy", ".35em")
                    .attr("text-anchor", "begin")
                    .attr("transform", "translate("+(x(series.date)+3)+","+(y(series.y)-10)+") rotate(-30)")
                    .text(series.text);
            });

            if (chartData.xAxisLabels) {
                svg.append("g")
                    .attr("class", "x axis")
                    .attr("transform", "translate(0," + height + ")")
                    .call(xAxis).selectAll("text")
                    .attr("y", 10)
                    .attr("x", 9)
                    .attr("dy", ".35em")
                    .attr("transform", "rotate(30)")
                    .style("text-anchor", "start");
            }

            if (chartData.yAxisLabels) {
                svg.append("g")
                    .attr("class", "y axis")
                    .call(yAxis);
            }

            if(chartData.showLegend) {
                svg.append("g")
                    .attr("class", "legend")
                    .attr("transform", "translate(" + (width - 100) + ",0)")
                    .style("font-size", "1.2em")
                    .call(d3.legend);
            }
        }
    };


    return chart;
}
