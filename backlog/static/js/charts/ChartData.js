    var ChartData = function(history, dueDate) {

        var parseISODate = d3.time.format("%Y-%m-%dT%H:%M:%S.%L000").parse;
        var parseSimpleDate = d3.time.format("%Y-%m-%d").parse;

        var series = function(statistic) {
            return {
                name: statistic,
                values: history.map(function(entry) {
                    return {
                        date: parseISODate(entry.datetime),
                        y: entry[statistic]
                    };
                })
            };
        };

        return {
            getAreaSeries: function() {
                return [series('total'), series('current')];
            },
            getLineSeries: function() {
                var first = _.first(history);
                var last = _.last(history);
                return [{
                    date: parseISODate(first.datetime),
                    y: first.current
                }, {
                    date: parseSimpleDate(dueDate),
                    y: last.total
                }];
            },
            getColorDomain: function() {
                return ['total', 'current'];
            },
            getXDomain : function() {
                var min = _.first(history).datetime;
                var max = _.last(history).datetime;
                return [parseISODate(min), d3.max([parseSimpleDate(dueDate), parseISODate(max)])];
            },
            getYDomain: function() {
                var min = 0;
                var max = _.max(history, function(entry) {
                    return entry.total;
                }).total;
                return [min, max];
            }
        };
    };