function populateConcepts(){

	console.log("in populateConcepts");



	var data = jQuery.parseJSON($('#my-data').attr("data"));

	for (var j=0; j<data.length;j++) {

		$(".collapsible").append('<li id="ch'+(j+1)+'"><div class="collapsible-header"><b>'+data[j]["concept"]+'</b></div></li>');
		$("#ch"+(j+1)).click(
			function(o){
				console.log("I'm in #"+o.currentTarget.id);
				$("#"+o.currentTarget.id).children().next().remove();
				$("#"+o.currentTarget.id).append('<div class="collapsible-body"><p>This concept is about lorem ipsum dores ist amet.</p><img class="video-placeholder" src="static/img/video-placeholder.png"></div>');
			}
		);
	}

}

function searchForAConcept(td_text){

}


$(document).ready(function(){
	searchForAConcept("Protocol-driven");
	populateConcepts();
	
});