$(function() {

    var loadData = function() {
        $.ajax({
            url: '/loaddata/',
            type: 'GET',
            dataType: 'json',
        })
        .done(function(data) {
            console.log("success", data);
            $(data).each(function(index, el) {
                $('.js__result').append(el.fields.url+'-'+'title : '+el.fields.title+'\nencoding: '+el.fields.encoding+'\nh1: '+el.fields.h1+'\n');
            });
        })
        .fail(function() {
            console.log("error");
        })
        .always(function() {
            console.log("complete");
        });
    }

    var getData = function(url) {
        $.ajax({
            url: '/getdata/',
            type: 'GET',
            dataType: 'html',
            beforeSend: function(xhr){
                xhr.setRequestHeader('X-CSRFToken', $('#content').data('token'))
            },
        })
        .done(function(data) {
            console.log("success", data);
        })
        .fail(function() {
            console.log("error");
        })
        .always(function() {
            console.log("complete");
        });
    }
    var socket;
    var start_socket = function(){
        socket = new WebSocket("ws://127.0.0.1:5237/parse/");
        socket.onopen = function() {
            getData();
        }
        socket.onmessage = function(event) {
            var json_data = jQuery.parseJSON(event.data);
            $('.js__status').append('<дата '+json_data.time+'>: '+json_data.status+'\n');
            if (json_data.status == "ok") {
                $('.js__result').append(json_data.url+'-'+'title: '+json_data.title+'\nencoding: '+json_data.encoding+'\nh1: '+json_data.h1+'\n');
            }else{$('.js__result').append(json_data.url+'\n')};
        };
    }
    var stop_socket = function() {
        socket.close();
    }
    loadData();
    $('.js__stop').on('click', function(event) {
        event.preventDefault();
        stop_socket();
    });
    $('.js__start').on('click', function(event) {
        event.preventDefault();
        start_socket();
    });
});