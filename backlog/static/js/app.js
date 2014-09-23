App = Ember.Application.create({});

App.Router.map(function() {
    this.resource('projects', function() {
        this.resource('project', {
            path: ':project_id'
        }, function() {
            this.route('table');
            this.route('charts');
        });
    });
});

App.IndexRoute = Ember.Route.extend({
    beforeModel: function() {
        this.transitionTo('projects');
    }
});

