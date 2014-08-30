
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

Ember.Handlebars.helper('format-float', function(number) {
    return (Math.round(number * 100) / 100).toFixed(2);
});
