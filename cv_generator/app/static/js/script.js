$(document).ready(function(){
	$("#generate").click(function(){
		var name=$(".xname").val();
		var dob=$(".dob").val();
		var email=$(".email").val();
		var mobile=$(".mobile").val();
		var address=$(".address").val();

	
		if(name==""||dob==""||email==""||mobile==""||address=="")
			 alert("Please fill all fields");
        
        else
			$.ajax({
				type:'POST',
				headers: {
      				'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content'),
   						},
				url: "/generate",
				data: {
   						'name':name,
   						'date_of_birth':dob,
   						'email_ID':email,
   						'mobile_no':mobile,
   						'address':address,
   						},
				success: function(data){
					console.log(data);
				}
			});

	});
})