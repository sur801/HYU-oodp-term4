function asking(id){

	if (confirm("실행할래?")== true){    //확인
		var xhr = new XMLHttpRequest();
		var url = "http://localhost:5000/delete";
		xhr.open("POST", url, true);
		xhr.setRequestHeader('Content-Type', 'text/plain');
		xhr.send(id)

	}else{   //취소
    	return;
	}
}
