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

        var daysBetween = function(date1, date2) {
            var difference = Math.abs(date1.getTime() - date2.getTime());
            return Math.round(difference / (1000 * 60 * 60 * 24));
        };

        return {
            getAreaSeries: function() {
                return [series('total'), series('current')];
            },
            getLinesSeries: function() {
                var first = _.first(history);
                var last = _.last(history);
                var optimal = [{
                    date: parseISODate(first.datetime),
                    y: first.current
                }, {
                    date: parseSimpleDate(dueDate),
                    y: last.total
                }, {
                    date: parseSimpleDate(dueDate),
                    y: 0
                }];
                return [optimal];
            },
            getColorDomain: function() {
                return ['total', 'current'];
            },
            getXDomain: function() {
                var min = _.first(history).datetime;
                var max = _.last(history).datetime;
                return [parseISODate(min), d3.max([parseSimpleDate(dueDate), parseISODate(max)])];
            },
            getXDaysSpan: function() {
                var domain = this.getXDomain();
                return daysBetween(domain[0], domain[1]);
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
