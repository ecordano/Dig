/**
 * Created by Emma on 3/15/2017.
 */

$(function () {
    $('#createGarden').click(function (){

        $.ajax({
            url: '/calculate',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response){
                document.write(response);
            },
            error: function(error){
                console.log(error);
            }
        })
    })
})