function displaySummary(input){
	console.log(input);
	for (var i = 0; i<input.length; i++){
		$("#index-banner").append("<div class='row'><h4>"+input[i]+".</h4></div>");
	}
}

$(document).ready(function(){
	var input = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget leo tellus. Morbi augue nisl, pulvinar eget laoreet eget, gravida non sapien. Cras lectus neque, consequat at mauris sed, scelerisque condimentum urna. Pellentesque tristique ac est eget facilisis. Suspendisse eget ligula euismod, pulvinar diam vel, pellentesque felis. Vestibulum eget suscipit nisl. Mauris tempus magna erat, sit amet pulvinar eros ornare a. Pellentesque id erat sodales, luctus risus eget, feugiat arcu. Nulla eleifend, turpis accumsan maximus imperdiet, nunc est ultricies dui, a porta ante libero nec magna. Proin sit amet turpis vitae massa pretium hendrerit ut vel nibh. Nunc nec tortor."
	displaySummary(input.split(". "));
});