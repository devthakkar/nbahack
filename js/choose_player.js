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
});

