App = Ember.Application.create({});

App.Router.map(function() {
    this.resource('about');
    this.resource('projects', function() {
        this.resource('project', {
            path: ':project_id'
        });
    });
});

App.Rest = {
    post: function(url, payload) {
        return $.ajax('/app/api/epics', {
            type: 'POST',
            dataType: 'JSON',
            data: JSON.stringify(payload),
            success: function(data, textStatus, jqXHR) {
                return data;
            },
            error: function(jqXHR, textStatus, errorThrown) {
                window.console.log(jqXHR);
            }
        });
    }

};

App.ProjectsRoute = Ember.Route.extend({
    model: function() {
        return $.getJSON('/app/api/projects').then(function(data) {
            return data;
        });
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

App.ModalController = Ember.ObjectController.extend({
    actions: {
        close: function() {
            return this.send('closeModal');
        }
    }
});

App.ModalDialogComponent = Ember.Component.extend({
    actions: {
        close: function() {
            return this.sendAction();
        }
    }
});

var showdown = new Showdown.converter();

Ember.Handlebars.helper('format-markdown', function(input) {
    return new Handlebars.SafeString(showdown.makeHtml(input || ""));
});

Ember.Handlebars.helper('format-date', function(date) {
    return date ? moment(date).fromNow() : 'N/A';
});

Ember.Handlebars.helper('format-displayname', function(name) {
    return name.replace(/\(.*\)/, '');
});

Ember.Handlebars.helper('format-percent', function(number) {
    return (Math.round(number * 100) / 100).toFixed(2) + '%';
});
