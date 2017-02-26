$(document).ready(function(){
    $(".msbutton").click(function(e) {
        var button = $(this)
        $.ajax({
            type: "POST",
            url: "/buttonClick",
            data: { 
                id: $(this).attr("id") // < note use of 'this' here
            },
            success: function(result) {
                var result = $.parseJSON(result);
                console.log(result);
                button.val(result["value"]);
            },
            error: function(result) {
                console.log(result);
            }
        });
    });

    $(".newgame").click(function(e) {
        $(".msbutton").val("");
        $.ajax({
            type: "POST",
            url: "/newGame",
            data: { 
            },
            success: function(result) {
            },
            error: function(result) {
            }
        });
    });
});
