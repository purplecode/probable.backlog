App.ProjectsRoute = Ember.Route.extend({
    model: function() {
        return App.Rest.get('/backlog/api/projects');
    },
    afterModel: function(projects, transition) {
        this.transitionTo('project.table', projects.get('firstObject').key);
    }
});

App.ProjectRoute = Ember.Route.extend({
    model: function(params) {
        var model = {
            project: App.Rest.get('/backlog/api/projects/' + params.project_id),
            epics: App.Rest.post('/backlog/api/epics', {
                sorting: {
                    order: 1
                },
                filtering: {
                    project_key: params.project_id
                }
            })
        };
        return Ember.RSVP.hash(model).then(function(model) {
            model.epics.index = lunr(function() {
                this.field('summary', {
                    boost: 10
                });
                this.field('description');
                this.ref('key');
            });
            _.each(model.epics, model.epics.index.add, model.epics.index);
            return model;
        });
    },
    afterModel: function(model) {
        this.transitionTo('project.table');
    }
});

App.ProjectController = Ember.Controller.extend({
    search: '',
    filteredEpics: function() {
        var keys = _.pluck(this.get('model.epics').index.search(this.search), 'ref');
        var epics = this.get('model.epics');
        return this.search ? _.filter(epics, function(epic) {
            return _.contains(keys, epic.key) || epic.summary.indexOf(this.search) >= 0;
        }, this) : epics;
    }.property('model.epics', 'search')
});

var modalActions = function(scope) {
    return {
        openModal: function(modalName, model) {
            this.controllerFor(modalName).set('model', model);
            return this.render(modalName, {
                into: 'project/' + scope,
                outlet: 'modal'
            });
        },
        closeModal: function() {
            return this.disconnectOutlet({
                outlet: 'modal',
                parentView: 'project.' + scope
            });
        }
    };
};

App.ProjectTableRoute = Ember.Route.extend({
    actions: modalActions('table')
});

App.ProjectTableController = Ember.Controller.extend({
    needs: "project",
    filteredEpics: Ember.computed.alias('controllers.project.filteredEpics')
});

App.ProjectTableView = Ember.View.extend({
    url: function() {
        return 'https://jira3.inside.nsn.com/browse/' + this.get('controller.model').project.key;
    }.property()
});

App.BacklogItemView = Ember.View.extend({
    templateName: 'backlog-item',
    classNames: 'backlog-item',
    labelClass: function() {
        var status = this.get('data').status;
        var classes = {
            'In Progress': 'label-success',
            'Open': 'label-info'
        };
        return classes[status] || 'label-default';
    }.property()
});

App.ProjectChartsRoute = Ember.Route.extend({
    actions: modalActions('charts')
});

App.ProjectChartsController = Ember.Controller.extend({
    needs: "project",
    filteredEpics: Ember.computed.alias('controllers.project.filteredEpics')
});

App.ProjectSummaryController = Ember.Controller.extend({});

App.ProgressBarGraph = Ember.View.extend({

    classNames: ['chart'],

    didInsertElement: function() {
        Ember.run.once(this, 'updateChart');
    },

    updateChart: function() {
        var $el = this.$()[0];
        var data = this.get('data');
        var history = data.history;
        if (!_.isEmpty(history) && history.length > 1 && data.status != 'Open') {
            var dueDate = data.dueDate;
            var chartData = new ProgressChartData(history, dueDate);
            var chart = new AreaChart($el, $($el).width());
            chart.draw(chartData);
        }
    }

});

App.SummaryGraph = Ember.View.extend({

    classNames: ['chart'],

    didInsertElement: function() {
        Ember.run.once(this, 'updateChart');
    },

    updateChart: function() {
        var $el = this.$()[0];
        var data = this.get('data');
        var epics = _.filter(data.epics, function(epic) {
            return !_.isEmpty(epic.dueDate);
        });
        var chartData = new SummaryChartData(epics);
        var chart = new AreaChart($el, $($el).width(), 600);
        chart.draw(chartData);
    }

});
