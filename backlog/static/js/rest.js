App.Rest = {
    post: function(url, payload) {
        return $.ajax(url, {
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
    },
    get: function(url) {
        return $.getJSON(url);
    }

};