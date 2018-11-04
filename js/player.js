function getUrlParameter(sParam) {
    var sPageURL = window.location.search.substring(1),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
        }
    }
};

$(document).ready(function(){
    var player = getUrlParameter('playerName');
    console.log(player);
    $("#player").text(player);
    var nameArr = player.split(" ");
    $("#player-img").attr('src','./img/player-img/'+nameArr[0].toLowerCase()+'-'+nameArr[1].toLowerCase()+'.png');
    $.post("/player", {"name" : player}, function(data){
        var performances = data["Values"];
        var age = data["Age"];
        var weight = data["Weight"];
        var height = data["Height"];
        $("#info").text('Age: '+ age + ' | Weight: ' + weight + ' | Height: ' + height);
        var ctx = document.getElementById("myChart");
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ["10/24", "10/26", "10/28", "10/30", "11/1"], //TODO: Add dates here 
                datasets: [{
                    label: 'Stock Value',
                    data: performances, //TODO: Add array here 
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255,99,132,1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero:true
                        }
                    }]
                }
            }
        });
    }); // GET request
});
