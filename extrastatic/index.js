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
            $('#results').html("<div class='alert-box alert radius' data-alert>The shortened url for "+json["link"]+
            " is: <a href="+json["link"]+">"+json["short_url"]+"</a>"+"<a href='#' class='close'>&times;</a></div>");
            console.log(json); // log the returned json to the console
            console.log("success"); // another debug check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>We have encountered an error: "+errmsg+
            "<p>This operation is undoable"+" <a href='#' class='close'>&times;</a></div>"); // add error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // more info about the error
        }
    });
});

