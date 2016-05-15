function populateConcepts(){
	concepts = ["Concept#1","Concept#2","Concept#3"];
	
	for (var i=0; i<concepts.length; i++){
		$(".collapsible").append('<li id="ch'+(i+1)+'"><div class="collapsible-header">'+concepts[i]+'</div></li>');
		$("#ch"+(i+1)).click(
			function(o){
				console.log("I'm in #"+o.currentTarget.id);
				$("#"+o.currentTarget.id).children().next().remove();
				$("#"+o.currentTarget.id).append('<div class="collapsible-body"><p>This concept is about lorem ipsum dores ist amet.</p><img class="video-placeholder" src="static/img/video-placeholder.png"></div>');
			}
		);
	}

}




$(document).ready(function(){
	searchForAConcept(concept)
	
});