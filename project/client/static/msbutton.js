$(document).ready(function(){
    $(".msbutton").click(function(e) {
        var button = $(this)
        $.ajax({
            type: "POST",
            url: "/buttonClick",
            data: { 
                id: $(this).attr("id")
            },
            success: function(result) {
                var result = $.parseJSON(result);
                //console.log(result);
                if ("value" in result) {
                    button.val(result["value"]);
                };
            },
            error: function(result) {
                console.log(result);
            }
        });
    });
});
