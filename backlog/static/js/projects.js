
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
    }
});

App.ProjectTableRoute = Ember.Route.extend({
    actions: {
        openModal: function(modalName, model) {
            this.controllerFor(modalName).set('model', model);
            return this.render(modalName, {
                into: 'project/table',
                outlet: 'modal'
            });
        },
        closeModal: function() {
            return this.disconnectOutlet({
                outlet: 'modal',
                parentView: 'project'
            });
        }
    }
});

App.ProjectTableView = Ember.View.extend({
    url: function() {
        return 'https://jira3.inside.nsn.com/browse/' + this.get('controller.model').project.key;
    }.property()
});

App.ProjectChartsRoute = Ember.Route.extend({


});

App.ProjectChartsView = Ember.View.extend({

});