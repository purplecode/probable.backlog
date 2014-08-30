
App.ProjectsRoute = Ember.Route.extend({
    model: function() {
        return $.getJSON('/app/api/projects').then(function(data) {
            return data;
        });
    },
    afterModel: function(projects, transition) {
      this.transitionTo('project', projects.get('firstObject').key);
  }
});

App.ProjectRoute = Ember.Route.extend({
    actions: {
        openModal: function(modalName, model) {
            this.controllerFor(modalName).set('model', model);
            return this.render(modalName, {
                into: 'project',
                outlet: 'modal'
            });
        },

        closeModal: function() {
            return this.disconnectOutlet({
                outlet: 'modal',
                parentView: 'project'
            });
        }
    },
    model: function(params) {
        var model = Ember.RSVP.hash({
            project: $.getJSON('/app/api/projects/' + params.project_id).then(function(data) {
                return data;
            }),
            epics: App.Rest.post('/app/api/epics', {
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

App.ProjectView = Ember.View.extend({
    url: function() {
        return 'https://jira3.inside.nsn.com/browse/' + this.get('controller.model').project.key;
    }.property()
});