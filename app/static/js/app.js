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
