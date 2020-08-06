function addImage() {
	var imageURL = document.getElementById('imageLink').value
	var docContainer = document.getElementsByClassName('container')
	var rowContent = `<div class="col-md-4 col-sm-6 col-xs-12">
			<div class="thumbnail">
				<img src= "${imageURL}">
			</div>
		</div>`


	document.getElementById('imageContainer').innerHTML += rowContent;
}