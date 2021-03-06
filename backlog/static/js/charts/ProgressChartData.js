var ProgressChartData = function(history, dueDate) {
    this.history = history;
    this.dueDate = dueDate;
};

ProgressChartData.prototype = _.extend({}, ChartData.prototype, {
    getAreaSeries: function() {
        return [this.utils.series(this.history, 'total'), this.utils.series(this.history, 'current')];
    },
    getLinesSeries: function() {
        var first = _.first(this.history);
        var last = _.last(this.history);
        var points = [{
            date: this.utils.parseDate(first.datetime),
            y: first.current
        }, {
            date: this.utils.parseDate(this.dueDate),
            y: last.total
        }, {
            date: this.utils.parseDate(this.dueDate),
            y: 0
        }];
        return [{
            points: points
        }];
    },
    getXDomain: function() {
        var min = this.utils.parseDate(_.first(this.history).datetime);
        var max = this.utils.parseDate(_.last(this.history).datetime);
        if(this.dueDate) {
            max = d3.max([this.utils.parseDate(this.dueDate), max])
        }
        return [min, max];
    },
    getXDaysSpan: function() {
        var domain = this.getXDomain();
        return this.utils.daysBetween(domain[0], domain[1]);
    },
    getYDomain: function() {
        var min = 0;
        var max = _.max(this.history, function(entry) {
            return entry.total;
        }).total;
        return [min, max];
    }
});
