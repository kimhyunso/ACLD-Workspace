$(document).ready(function(){
	$("#addPartBtn").click(function(){
		var emp_name = $("#emp_name").val();
		var rank = $("#rank").val();
		var demp_name = $("#demp_name").val();
		var emp_no = $("#emp_no").val();
		var MAC = $("#MAC").val();
		var IP = $("#IP").val();
		var phone_no = $("#phone_no").val();
		var landline = $("#landline").val();
		var email = $("#email").val();
		var location = $("#location").val();
		var emp_data = {
			'emp_name' : emp_name,
			'rank' : rank,
			'demp_name' : demp_name,
			'emp_no' : emp_no,
			'MAC' : MAC,
			'IP' : IP,
			'phone_no' : phone_no,
			'landline' : landline,
			'email' : email,
			'location' : location
		}

		$.ajax({
			type :"POST",
			url : "{% url 'main:addDepart' %}",
			headers: { "X-CSRFToken": '{{csrf_token}}' },
			data : JSON.stringify(emp_data),
			dataType : "JSON",
			success : function(response){
				location.href="{% url 'main:addEmp' %}";
			}
		});
	});
});