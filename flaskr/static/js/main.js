function asking(id){

	if (confirm("실행할래?")== true){    //확인
		/*var xmlHttpp = new XMLHttpRequest();
    	var sendm = JSON.stringify(id);
    	xmlHttpp.open( "POST", "http://127.0.0.1:5000/delete/", false);
    	xmlHttpp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    	xmlHttpp.send(id);*/
    	$.ajax({
			method: "DELETE",
			url: "/delete/" + id,
			success:function(response){
				location.reload();
			}
		});

	}else{   //취소
    	return;
	}
}
