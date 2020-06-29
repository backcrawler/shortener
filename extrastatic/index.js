$(document).on("submit", "#post-form", function(e) {
    e.preventDefault();
    console.log("ajax is working!") // debug
    $.ajax({
        url : "/", // endpoint
        type : "POST",
        data : { url: $('#link-text').val(),
                 csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#link-text').val(''); // remove the value from the input
            if (json.result != 'Create successful!') {
                $('#results').html("<div class='alert-box alert radius' data-alert>Unfortunately that won't work: "+
                json["url"]+"<a href='#' class='close'>&times;</a></div>");
                }
            else {
                $('#results').html("<div class='card result-form'>The shortened url for "+json["url"]+
                " is: <p><a id='myRef' href="+json["short_url"]+">"+json["short_url"]+"</a></p>"+
                "<button type='button' class='copy' aria-hidden='false' onclick='copyFunction()'>"+
                "<img src='images/savepic.svg' width=25px height=25px class='copypic'></button></div>");
                }
            console.log(json); // log the returned json to the console
            console.log("success"); // another debug check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>We have encountered an internal error: "+errmsg+
            "<p>This operation is undoable right now..."+" <a href='#' class='close'>&times;</a></div>"); // add error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // more info about the error
        }
    });
});

