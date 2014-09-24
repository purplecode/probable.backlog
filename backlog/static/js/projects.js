
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
                parentView: 'project.table'
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

App.ProjectChartsController = Ember.Controller.extend({
  content: [
    {
        "label": "Equity",
        "value": 12935781.176999997,
        "type": "money"
    },
    {
        "label": "Real Assets",
        "value": 10475849.276172025,
        "type": "money"
    },
    {
        "label": "Fixed Income",
        "value": 8231078.16438347,
        "type": "money"
    },
    {
        "label": "Cash & Cash Equivalent",
        "value": 5403418.115000006,
        "type": "money"
    },
    {
        "label": "Hedge Fund",
        "value": 1621341.246006786,
        "type": "money"
    },
    {
        "label": "Private Equity",
        "value": 1574677.59,
        "type": "money"
    }
  ]
});