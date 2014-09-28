    var ChartData = function(history) {

        var parseDate = d3.time.format("%Y-%m-%dT%H:%M:%S.%L000").parse;

        var series = function(statistic) {
            return {
                name: statistic,
                values: history.map(function(entry) {
                    return {
                        date: parseDate(entry.datetime),
                        y: entry[statistic]
                    };
                })
            };
        };

        return {
            getSeries: function() {
                return [series('total'), series('current')];
            },
            getColorDomain: function() {
                return ['total', 'current'];
            },
            getXDomain : function() {
                var min = _.first(history).datetime;
                var max = _.last(history).datetime;
                return [parseDate(min), parseDate(max)];
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