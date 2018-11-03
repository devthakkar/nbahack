$(document).ready(function(){
    var player = "Kevin Durant";
   // $("#player").text(player);
   // $("#player-img").attr('src','./img/player-img/kevin-durant.png');
});

function getLB() {
    $.get("/LebronJames", function(data){
        $("#player").text(data.name);
        $("#player-img").attr('src',data.image);
    });
}