var socket = io();
socket.on('connect', function() {
    console.log("connected");

    is_death = false;
    socket.on('on_death', function(data) {
        console.log(data);
        if(is_death === false) {
            var x = document.getElementById("death_audio");
            x.play();
            document.getElementById("status").style.color = "red";
            document.getElementById("status").innerText = "Status: We died"
            is_death = true
        }
    });
    let start = false;
    socket.on('on_start', function(data) {
        console.log(data);
        if(start === false) {
            var x = document.getElementById("start_audio");
            x.play();
            document.getElementById("status").style.color = "lightblue";
            document.getElementById("status").innerText = "Status: Running"
            start = true;
        }
    });
    socket.on('on_hit', function(data) {
        console.log("getting_hit");
        var x = document.getElementById("hit_sound");
        x.play();
        document.getElementById("status").innerText = "Status: Getting hit"

        setInterval(function(){
            document.getElementById("status").style.color = "white";
            document.getElementById("status").innerText = "Status: Running"
        }, 5000)
    });

    socket.on('on_game_over', function(data) {
        console.log(data);
        var x = document.getElementById("game_over");
        x.play();
        document.getElementById("status").style.color = "white";
        document.getElementById("status").innerText = "Status: Game over we staan aan de kant. Je kan me op pakken"
        start = true;
    });

});