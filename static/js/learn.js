function populateConcepts(){

	console.log("in populateConcepts");
	concepts = ["Concept#1","Concept#2","Concept#3"];

//	for (var i=0; i<concepts.length; i++){
//		$(".collapsible").append('<li id="ch'+(i+1)+'"><div class="collapsible-header">'+concepts[i]+'</div></li>');
//		$("#ch"+(i+1)).click(
//			function(o){
//				console.log("I'm in #"+o.currentTarget.id);
//				$("#"+o.currentTarget.id).children().next().remove();
//				$("#"+o.currentTarget.id).append('<div class="collapsible-body"><p>This concept is about lorem ipsum dores ist amet.</p><img class="video-placeholder" src="static/img/video-placeholder.png"></div>');
//			}
//		);
//	}

	var data = jQuery.parseJSON($('#my-data').attr("data"));

	for (var j=0; j<data.length;j++) {

		$(".collapsible").append('<li id="ch'+(j+1)+'"><div class="collapsible-header">'+data[j]["concept"]+'</div></li>');
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