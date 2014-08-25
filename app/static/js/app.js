App = Ember.Application.create({});

App.Router.map(function() {
  this.resource('about');
  this.resource('projects', function() {
    this.resource('project', { path: ':project_id' });
  });
});

App.ProjectsRoute = Ember.Route.extend({
  model: function() {
    return $.getJSON('/app/api/projects').then(function(data) {
        return data;
    });
  }
});

App.ProjectRoute = Ember.Route.extend({
  model: function(params) {
    var model = Ember.RSVP.hash(
      {
        project: $.getJSON('/app/api/projects/'+params.project_id).then(function(data) {
            return data;
        }),
        epics: $.getJSON('/app/api/epics').then(function(data) {
            return data;
        })
      });
    return model;
  }
});

var showdown = new Showdown.converter();

Ember.Handlebars.helper('format-markdown', function(input) {
  return new Handlebars.SafeString(showdown.makeHtml(input||""));
});

Ember.Handlebars.helper('format-date', function(date) {
  return moment(date).fromNow();
});