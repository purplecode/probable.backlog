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
        .scale(x).ticks(d3.time.days, 1)
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

    var stack = d3.layout.stack()
        .values(function(d) {
            return d.values;
        });


    var chart = {

        draw: function(data) {

            var svg = d3.select(selection).append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
                .append("g")
                .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

            var parseDate = d3.time.format("%Y-%m-%d").parse;


            var t1 = "2011-01-01";
            var t2 = "2011-01-02";
            var t3 = "2011-01-03";
            var t4 = "2011-01-04";

            var data = [{
                name: 'A',
                values: [{
                    date: parseDate(t1),
                    y: 0.2
                }, {
                    date: parseDate(t2),
                    y: 0.4
                }, {
                    date: parseDate(t3),
                    y: 3
                }, {
                    date: parseDate(t4),
                    y: 3
                }]
            }, {
                name: 'B',
                values: [{
                    date: parseDate(t1),
                    y: 0.1
                }, {
                    date: parseDate(t2),
                    y: 0.3
                }, {
                    date: parseDate(t3),
                    y: 4
                }, {
                    date: parseDate(t4),
                    y: 4
                }]
            }];

            color.domain(['A', 'B']);

            x.domain([parseDate(t1), parseDate(t4)]);

            var browser = svg.selectAll(".browser")
                .data(data)
                .enter().append("g")
                .attr("class", "browser");

            browser.append("path")
                .attr("class", "area")
                .attr("d", function(d) {
                    return area(d.values);
                })
                .style("fill", function(d) {
                    return color(d.name);
                });

            // browser.append("text")
            //     .datum(function(d) {
            //         return {
            //             name: d.name,
            //             value: d.values[d.values.length - 1]
            //         };
            //     })
            //     .attr("transform", function(d) {
            //         return "translate(" + x(d.value.date) + "," + y(d.value.y0 + d.value.y / 2) + ")";
            //     })
            //     .attr("x", -6)
            //     .attr("dy", ".35em")
            //     .text(function(d) {
            //         return d.name;
            //     });


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
        }
    };


    return chart;
}
