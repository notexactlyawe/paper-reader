function populateConcepts(){
	console.log("in populateConcepts");

	var data = jQuery.parseJSON($('#my-data').attr("data"));

	for (var j=0; j<data.length;j++) {

		$(".collapsible").append('<li id="ch'+(j+1)+'"><div class="collapsible-header"><b>'+data[j]["concept"]+'</b></div></li>');
		$("#ch"+(j+1)).click(
			function(o){


		   	  var posting = $.post( "/api/v1/wikisummary", {"query": $(this).text(), "sentences": "2" } );
		   	  posting.done(function( data ) {
		   	  		 var response = (jQuery.parseJSON(data))['content'];

		   			 $("#"+o.currentTarget.id).children().next().remove();
		   		     $("#"+o.currentTarget.id).append('<div class="collapsible-body"><p>' + JSON.stringify(response) + '</p><img class="video-placeholder" src="/static/img/video-placeholder.png"></div>');
					 $("#"+o.currentTarget.id).children().next().show();
		   	  });

		   	  $.get( "/api/v1/concept/" + $(this).text(), function( data ) {
				 	var response = (jQuery.parseJSON(data));
					alert(JSON.stringify(response))

//				    $( ".result" ).html( data );
//					 $("#"+o.currentTarget.id).append('<div class="collapsible-body"><p>' + JSON.stringify(response) + '</p><img class="video-placeholder" src="/static/img/video-placeholder.png"></div>');


			  });

			}
		);
	}

}

function searchForAConcept(td_text){

}


$(document).ready(function(){
	searchForAConcept("Protocol-driven");
	populateConcepts();
	$('.modal-trigger').leanModal();

	// $(".modal-trigger").click(function(){
	// 	$('#modal1').openModal();
	// });
	
});