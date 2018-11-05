$(document).ready(function(){
    $.get("/allplayers", function(data) {
        var names = [];
        for (var i = 0; i < data.length; i++) {
            names.push(data[i]["full_name"]);
        }
        $(".search").autocomplete({
            source: function(request, response) {
                var results = $.ui.autocomplete.filter(names, request.term);
                
                response(results.slice(0, 10));
            },
            select: function(event, ui) {
                let url = `./player.html?playerName=${ui.item.value}`
                window.location = url;
             }    
        });
        
    });
    
});

