function asking(){
	if (confirm("실행할래?")== true){    //확인

    document.form.submit();
	}else{   //취소
    	return;
	}
}
