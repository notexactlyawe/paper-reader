function populateConcepts(){
	console.log("in populateConcepts");

	var data = jQuery.parseJSON($('#my-data').attr("data"));
	console.log(data);
	for (var j=0; j<data.length;j++) {

		$(".collapsible").append('<li id="ch'+(j+1)+'"><div class="collapsible-header"><b>'+data[j]["concept"]+'</b></div></li>');
		$("#ch"+(j+1)).click(
			function(o){
				var querydata = $(this).text()
		   	  var posting = $.post( "/api/v1/wikisummary", {"query": querydata, "sentences": "2" } );
		   	  posting.done(function( data ) {
		   	  		 var response = (jQuery.parseJSON(data))['content'];

		   			 $("#"+o.currentTarget.id).children().next().remove();
		   		     $("#"+o.currentTarget.id).append('<div class="collapsible-body"><p>' + JSON.stringify(response) + '</p><img class="video-placeholder" src="/static/img/video-placeholder.png">');
					 $("#"+o.currentTarget.id).children().next().show();

			   $.get( "/api/v1/concept/" + encodeURIComponent(querydata), function( data ) {
				 	var response = (jQuery.parseJSON(data));
				 	var similars = response['subs'];
				 	alert(similars);

				 	for (var x = 0; x < similars.length; x++) {

				 		$("#"+o.currentTarget.id).append('<a href=\"#\">' + JSON.stringify(similars[x]) + '</p>');
				 	}
					$("#"+o.currentTarget.id).append('</div>');
					alert(JSON.stringify(response));

//				    $( ".result" ).html( data );
//					 $("#"+o.currentTarget.id).append('<div class="collapsible-body"><p>' + JSON.stringify(response) + '</p><img class="video-placeholder" src="/static/img/video-placeholder.png"></div>');


			  });
		   	  });



			}
		);
	}

}



// function populateSummary(){
// 	//var posting = $.post( "/api/v1/summarize" );

	
// 	var input = jQuery.parseJSON($('#my-summary').attr("data"));
// 	console.log(input);
// 	for (var i = 0; i<input.length; i++){
// 		$("#modal1").append("<div class='row'><h4>"+input[i]+".</h4></div>");
// 	}

// 	$(document).ready(function(){
// 		var input = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget leo tellus. Morbi augue nisl, pulvinar eget laoreet eget, gravida non sapien. Cras lectus neque, consequat at mauris sed, scelerisque condimentum urna. Pellentesque tristique ac est eget facilisis. Suspendisse eget ligula euismod, pulvinar diam vel, pellentesque felis. Vestibulum eget suscipit nisl. Mauris tempus magna erat, sit amet pulvinar eros ornare a. Pellentesque id erat sodales, luctus risus eget, feugiat arcu. Nulla eleifend, turpis accumsan maximus imperdiet, nunc est ultricies dui, a porta ante libero nec magna. Proin sit amet turpis vitae massa pretium hendrerit ut vel nibh. Nunc nec tortor."
// 		displaySummary(input.split(". "));
// 	});
// }


$(document).ready(function(){
	//searchForAConcept("Protocol-driven");
	populateConcepts();
	console.log($("great-id").text());

	$('.modal-trigger').leanModal();

	$(".modal-trigger").click(function(){
		$('#modal1').openModal();
	});
	//populateSummary();

});