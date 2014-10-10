var ChartData = function() {};

ChartData.prototype = {
    xAxisLabels: true,
    yAxisLabels: true,
    utils: {
        parseSimpleDate: d3.time.format("%Y-%m-%d").parse,
        parseISODate: d3.time.format("%Y-%m-%dT%H:%M:%S.%L000").parse,
        daysBetween: function(date1, date2) {
            var difference = Math.abs(date1.getTime() - date2.getTime());
            return Math.round(difference / (1000 * 60 * 60 * 24));
        },
        series: function(timeseries, statistic) {
            return {
                name: statistic,
                values: timeseries.map(function(entry) {
                    return {
                        date: this.parseISODate(entry.datetime),
                        y: entry[statistic]
                    };
                }, this)
            };
        }
    },
    getAreaSeries: function() {
        return [];
    },
    getLinesSeries: function() {
        return [];
    },
    getTextSeries: function() {
        return [];
    },
    getColorDomain: function() {
        return [];
    },
    getXDomain: function() {
        return [];
    },
    getXDaysSpan: function() {
        return 1;
    },
    getYDomain: function() {
        return [0, 1];
    }
};
