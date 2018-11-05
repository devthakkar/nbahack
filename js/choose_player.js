$(document).ready(function(){
    var choosePlayer = function(data) {
        var player = data.target.innerHTML;
        let url = `./player.html?playerName=${player}`
        window.location = url;
    };
    var spanSelector= document.querySelectorAll('#button');
    for (var i = 0; i <  spanSelector.length;  i++) {
        spanSelector[i].onclick= choosePlayer;
    }
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

