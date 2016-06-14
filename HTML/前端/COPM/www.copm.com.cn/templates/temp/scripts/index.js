$(function(){
//$(".top ul li:last").css("background","none");
$(".new_list:last").css("background","none");
$(".procts p.title  a:last").css("background","none");
$(".link ul li:last").css("background","none");
$(".compy a:last").css("background","none");
$(".top ul li .box ul li:last").css("border","0px");
$(".procts p.title a").each(function(i) {
    $(this).click(function(){
		$(".procts p.title a").css("font-weight","normal");
	$(this).css("font-weight","bold");
	$(".procts ul").hide();
	$(".procts ul").eq(i).show();
	});
	
	
	
});
});