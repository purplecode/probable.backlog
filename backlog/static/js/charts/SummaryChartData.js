var SummaryChartData = function(epics) {
    this.epics = epics;
};

SummaryChartData.prototype = _.extend({}, ChartData.prototype, {
    yAxisLabels: false,
    today: new Date(),
    getAreaSeries: function() {
        return [];
    },
    getLinesSeries: function() {
        return _.pluck(this._getSeries(), 'line');
    },
    getTextSeries: function() {
        return _.pluck(this._getSeries(), 'text');
    },
    getColorDomain: function() {
        return [];
    },
    getXDomain: function() {
        var min = _.min(this.epics, function(epic) {
            return epic.dueDate.replace(/-/g, '');
        }).dueDate;
        min = this.utils.parseSimpleDate(min);
        min = d3.min([new Date(this.today), min])
        min.setDate(min.getDate() - 2);

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
        return [0, this.epics.length*2+10];
    },
    _getSeries: function() {

        var counter = 1;
        var today = {
            line: [{
                date: this.today,
                y: 2*counter
            }, {
                date: this.today,
                y: -5
            }],
            text: {
                date: this.today,
                y: 2*counter,
                text: 'Today'
            }
        };

        var epics = _.map(this.epics, function(epic) {
            counter++;
            return {
                line: [{
                    date: this.utils.parseSimpleDate(epic.dueDate),
                    y: 2*counter
                }, {
                    date: this.utils.parseSimpleDate(epic.dueDate),
                    y: -5
                }],
                text: {
                    date: this.utils.parseSimpleDate(epic.dueDate),
                    y: 2*counter,
                    text: epic.summary
                }
            };
        }, this);

        return [today].concat(epics);
    }
});
