App = Ember.Application.create({});

App.Router.map(function() {
    this.resource('charts', function() {
        this.resource('project', {
            path: ':project_id'
        });
    });
    this.resource('projects', function() {
        this.resource('project', {
            path: ':project_id'
        });
    });
});

App.IndexRoute = Ember.Route.extend({
    beforeModel: function() {
        this.transitionTo('projects');
    }
});

