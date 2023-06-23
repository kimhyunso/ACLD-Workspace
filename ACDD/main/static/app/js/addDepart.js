function addPartRegist(url, csrf_token){
	console.log(url, csrf_token);
	const dempName = document.getElementById("dempName").value;
	const landLine = document.getElementById("landLine").value;
	const location = document.getElementById("location").value;

	data = {
		"dempName" : dempName,
		"landLine" : landLine,
		"location" : location,
	}

	fetch(url,
	{
		method: 'POST',
		body : JSON.stringify(data),
		datatype : 'JSON',
		headers: { "X-CSRFToken": '{{csrf_token}}' },
	})
	.then(function (response) {
		window.location.replace(url);
	})
	.catch(function (err) {
		alert('다시 입력해주세요!');
	});
}