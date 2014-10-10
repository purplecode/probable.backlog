var SummaryChartData = function(epics) {
    this.epics = epics;
};

SummaryChartData.prototype = _.extend({}, ChartData.prototype, {
    yAxisLabels : false,
    getAreaSeries: function() {
        return [];
    },
    getLinesSeries: function() {
        return _.map(this.epics, function(epic) {
            return [{
                date: this.utils.parseSimpleDate(epic.dueDate),
                y: 10
            }, {
                date: this.utils.parseSimpleDate(epic.dueDate),
                y: 0
            }];
        }, this);
    },
    getColorDomain: function() {
        return [];
    },
    getXDomain: function() {
        var min = new Date();
        var max = _.max(this.epics, function(epic) {
            return epic.dueDate.replace(/-/g, '');
        }).dueDate;
        max = this.utils.parseSimpleDate(max);
        max.setDate(max.getDate() + 7);
        return [min, max];
    },
    getXDaysSpan: function() {
        var domain = this.getXDomain();
        return this.utils.daysBetween(domain[0], domain[1]);
    },
    getYDomain: function() {
        return [0, 10];
    }
});
