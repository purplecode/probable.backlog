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
        var model = Ember.RSVP.hash({
            project: App.Rest.get('/backlog/api/projects/' + params.project_id),
            epics: App.Rest.post('/backlog/api/epics', {
                sorting: {
                    order: 1
                },
                filtering: {
                    project_key: params.project_id
                }
            })
        });
        return model;
    },
    afterModel: function() {
        this.transitionTo('project.table');
    }
});

var modalActions = function(scope) {
    return {
        openModal: function(modalName, model) {
            this.controllerFor(modalName).set('model', model);
            return this.render(modalName, {
                into: 'project/'+scope,
                outlet: 'modal'
            });
        },
        closeModal: function() {
            return this.disconnectOutlet({
                outlet: 'modal',
                parentView: 'project.'+scope
            });
        }
    };
};

App.ProjectTableRoute = Ember.Route.extend({
    actions: modalActions('table')
});

App.ProjectChartsRoute = Ember.Route.extend({
    actions: modalActions('charts')
});

App.ProjectTableView = Ember.View.extend({
    url: function() {
        return 'https://jira3.inside.nsn.com/browse/' + this.get('controller.model').project.key;
    }.property()
});

App.ProjectChartsController = Ember.Controller.extend({});

App.BarGraph = Ember.View.extend({

    classNames: ['chart'],

    didInsertElement: function() {
        Ember.run.once(this, 'updateChart');
    },

    updateChart: function() {
        var $el = this.$()[0];
        var data = this.get('data');
        var history = data.history;
        if(!_.isEmpty(history) && history.length > 1 && data.status != 'Open') {
            var dueDate = data.dueDate;
            var chartData = new ChartData(history, dueDate);
            var chart = new AreaChart($el);
            chart.draw(chartData);
        }
    }

});
