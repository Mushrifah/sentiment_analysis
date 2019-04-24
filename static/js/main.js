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
 			$('#result').css('display', 'inline');
 			$('#result').text(result.label);

            //     $('#rfc').text("RFC: " + result.rfc);
            // result = response
            // if(result.status){
            //     $('#loader_sensor').css('display', 'none');

            //     $('#rfc').css('display', 'inline');
            //     $('#kmeans').css('display', 'inline');
            //     $('#svm').css('display', 'inline');

            //     $('#rfc').text("RFC: " + result.rfc);
            //     $('#kmeans').text("KMeans: " + result.kmeans);
            //     $('#svm').text("SVM: " + result.svm);
            // }else{
            //     $('#loader_sensor').css('display', 'none');
            //     $('#kmeans').css('display', 'inline');
            //     $('#kmeans').text(result.message);
            //     $('#kmeans').css('color', 'red');
            // }
        },
    });


});
