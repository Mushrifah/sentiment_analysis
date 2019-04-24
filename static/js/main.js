$("#submit").click(function(){
	    var Reviews = {'review': $('#Reviews').val()};
	    console.log(Reviews)

	    $.ajax({
        url: '/predict',
        type: 'post',
        data: Reviews ,
        timeout: 6000,
        success: function(response){

            //var result = JSON.parse(response);
            console.log(response);
            var result = response;
 			$('#result').css({"display": "inline","color":"black"});
 			$('#result').text(result.label);
        },
    });


});
