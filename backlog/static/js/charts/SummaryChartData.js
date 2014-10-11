var SummaryChartData = function(epics) {
    this.epics = epics;
};

SummaryChartData.prototype = _.extend({}, ChartData.prototype, {
    yAxisLabels: false,
    showLegend: false,
    today: new Date(),
    getAreaSeries: function() {
        var domain = this.getXDomain();

        var first = _.first(domain);
        var last = _.last(domain);
        var timeseries = [];

        var currentDate = new Date(first.getFullYear(), first.getMonth() + 1, 1);

        timeseries.push([_.first(domain), currentDate]);
        while (currentDate < last) {
            var start = new Date(currentDate);
            currentDate = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 1);
            timeseries.push([start, currentDate]);
        }
        _.last(timeseries)[1] = last;


        var yDomain = this.getYDomain();
        return _.map(timeseries, function(interval) {
            return {
                name: moment(interval[0]).format('MMMM'),
                values: interval.map(function(entry) {
                    return {
                        date: entry,
                        y: yDomain[1]
                    };
                }, this)
            }
        });
    },
    getLinesSeries: function() {
        return _.pluck(this._getSeries(), 'line');
    },
    getTextSeries: function() {
        return _.pluck(this._getSeries(), 'text');
    },
    getColor: function(entry) {
        var month = new Date(Date.parse(entry +" 1, 2012")).getMonth()+1
       return (month % 2 == 1) ? 'rgba(31, 119, 180, 0.2)' : 'rgba(174, 199, 232, 0.2)';
    },
    getXDomain: function() {
        var min = _.min(this.epics, function(epic) {
            return epic.dueDate.replace(/-/g, '');
        }).dueDate;
        min = this.utils.parseDate(min);
        min = d3.min([new Date(this.today), min])
        min.setDate(min.getDate() - 2);

        var max = _.max(this.epics, function(epic) {
            return epic.dueDate.replace(/-/g, '');
        }).dueDate;
        max = this.utils.parseDate(max);
        max.setDate(max.getDate() + 7);
        return [min, max];
    },
    getXDaysSpan: function() {
        var domain = this.getXDomain();
        return this.utils.daysBetween(domain[0], domain[1]);
    },
    getYDomain: function() {
        return [0, this.epics.length * 2 + 10];
    },
    _getSeries: function() {

        var counter = 1;
        var today = {
            line: {
                color: 'red',
                points: [{
                    date: this.today,
                    y: 2 * counter
                }, {
                    date: this.today,
                    y: -5
                }]
            },
            text: {
                date: this.today,
                y: 2 * counter,
                text: 'Today'
            }
        };

        var epics = _.map(this.epics, function(epic) {
            counter++;
            return {
                line: {
                    color: "#2C3E50",
                    points: [{
                        date: this.utils.parseDate(epic.dueDate),
                        y: 2 * counter
                    }, {
                        date: this.utils.parseDate(epic.dueDate),
                        y: -5
                    }]
                },
                text: {
                    date: this.utils.parseDate(epic.dueDate),
                    y: 2 * counter,
                    text: epic.summary
                }
            };
        }, this);

        return [today].concat(epics);
    }
});
