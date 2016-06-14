$(function(){


$(".ind-menu>ul>li").hover(function() {

    $(this).addClass("cur").find("div").show();

}, function() {
    $(this).removeClass("cur").find("div").hide();
});




    $(".grid .site-a").click(function() {
	$(".grid .add_box").show();
});
$(".grid .close").click(function(){
	$(".grid .add_box").hide();
});
$(".grid .add_box p a").each(function(i) {
    $(this).click(function(){
	$(this).addClass("cur").siblings().removeClass("cur");
	$(".add_list ul").hide();
	$(".add_list ul").eq(i).show();
	});
});;


 $(".grid span").hover(function(){
	$(this).find("ol").show("slow");
 },function(){
	$(this).find("ol").hide();
 });
})

//加入收藏
function AddFavorite(sURL, sTitle)
{
  try
   {
       window.external.addFavorite(sURL, sTitle);
   }
  catch (e)
  {
     try
      {
          window.sidebar.addPanel(sTitle, sURL, "");
      }
      catch (e)
      {
          alert("加入收藏失败，请使用Ctrl+D进行添加");
     }
 }
}


//设为首页
function SetHome(obj){
	try{
		obj.style.behavior='url(#default#homepage)';
		obj.setHomePage('http://#setHomePage');
	}catch(e){
		if(window.netscape){
			try{
				netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");
			}catch(e){
				alert("抱歉，此操作被浏览器拒绝！\n\n请在浏览器地址栏输入“about:config”并回车然后将[signed.applets.codebase_principal_support]设置为'true'");
			};
		}else{
		alert("抱歉，您所使用的浏览器无法完成此操作。\n\n您需要手动将'http://#setHomePage'设置为首页。");
		};
	};
};


//设为首页和加入收藏
$(function(){
	$(".grid a.sc").click(function(){
		AddFavorite('http://#setHomePage', '福建龙祥居物业管理有限公司首页');
	});
	$(".nav ul.wrp_ul li").hover(function(){
		$(this).find("ul").show();
		},function(){
		$(this).find("ul").hide();
	})
})



$(function(){
$(".top>ul>li").hover(function(){

	$(this).addClass("cur").find("div").slideDown();

	},function(){
		$(this).removeClass("cur").find("div").hide();
	});
})
$(function(){
$("#sidebar .menu>li>a").click(function() {

			$(this).next().toggle();
			  $(this).parent("li").siblings("li").find("ul").hide();
			});
		   })



$(function(){
		   $(".text").focus(function(){
										var txt_value=$(this).val();
									if(txt_value==this.defaultValue){
										$(this).val("");
									}
										});
		   $(".text").blur(function(){
									  var txt_value=$(this).val();
									  if(txt_value==""){
										 $(this).val(this.defaultValue);
									  }
									   });
})
function setHeight(){
  var O1 = $(arguments[0]);
  var O2 = $(arguments[1]);
  if(O1 && O2){
    O1.attr('style', ' ');
    O2.attr('style', ' ');
    var maxH = Math.max(O1.height(), O2.height());
    if(O1.height() < maxH){
      O1.height(maxH);
    }else{
      O2.height(maxH);
    }
  }
};
$(function(){
$(".link ul li:last").css("background","none");
$(".last_bg").css("background","none");
})
function FN_select3(){
	var zIndex = 99;
	$('div.jselect_box3').each(function(i){
		var _this = $(this);
		zIndex = zIndex - i;
		$(this).css('z-index',zIndex);
		_this.hover(
			function(){$(this).find('ul').stop(true,true).animate({ height: 'show'},400)},
			function(){$(this).find('ul').stop(true,true).animate({ height: 'hide'},1)}
		);
		_this.find('li').click(function(){
			_this.find('h4').html($(this).html());
			_this.find('ul').hide();
		});
	})
}

$(function(){
	$("#s_nav li:has(ul)").hover(function(){
		$(this).addClass('current').children('a').addClass('current').end().children('ul').stop(true,true).slideDown(100);
		}
		,function(){
			$(this).removeClass('current').children('a').removeClass('current').end().children('ul').stop(true,true).slideUp(100);
			});
	});

var ImgLibE=function(btnA,btnB,targetImgs,targetTI,step,speed,isHorV){
	this.btnA=btnA;
	this.btnB=btnB;
	this.targetImgs=targetImgs;
	this.targetTI=targetTI;
	this.step=step||300;
	this.speed=speed||1000;
	this.isHorV=isHorV;//Set the value false if you want to change the direction to Vertical
	this.initialization();
	this.attachEvent();
}

ImgLibE.prototype={
	attachIndex:function(target){
		$(target).find("li").each(function(kis){
			$(this).attr("Index",kis);
		});
	},
	initialization:function(){
		var _t=this;
		_t._outer_org_=$(_t.targetImgs).parent();
		_t.scrollValue=0;
		_t.attachIndex(_t.targetImgs);
		if(_t.isHorV){
			var _ee=_t.step*$(_t.targetImgs).find("li").length;
			$(_t.targetImgs).width(_ee);
			_t.MAXVALUE=_ee-_t._outer_org_.css("width").replace("px","");
		}else{
			_t.MAXVALUE=$(_t.targetImgs).height()-_t._outer_org_.height();
		}
	},
	attachEvent:function(){
		var _t=this;
		_t.btnAEvent();
		_t.btnBEvent();
		_t.elementsClick();
	},
	autoPlay:function(direction){

	},
	scrollLeft:function(){
		var _t=this;
		_t.scrollValue+=_t.step;
		if(_t.scrollValue>_t.MAXVALUE){_t.scrollValue=_t.MAXVALUE;}
		_t._outer_org_.animate({scrollLeft:_t.scrollValue},_t.speed);
	},
	scrollRight:function(){
		var _t=this;
		_t.scrollValue-=_t.step;
		if(_t.scrollValue<=0){_t.scrollValue=0;}
		_t._outer_org_.animate({scrollLeft:_t.scrollValue},_t.speed);
	},
	scrollTop:function(){
		var _t=this;
		_t.scrollValue+=_t.step;
		if(_t.scrollValue>_t.MAXVALUE){_t.scrollValue=_t.MAXVALUE;}
		_t._outer_org_.animate({scrollTop:_t.scrollValue},_t.speed);
	},
	scrollDown:function(){
		var _t=this;
		_t.scrollValue-=_t.step;
		if(_t.scrollValue<=0){_t.scrollValue=0;}
		_t._outer_org_.animate({scrollTop:_t.scrollValue},_t.speed);
	},
	btnAEvent:function(){
		var _t=this;

		$(_t.btnA).click(function(){
			if(_t.MAXVALUE<=0)
				return;
			if(_t.isHorV){
				_t.scrollLeft();
			}else{
				_t.scrollTop();
			}
		});
	},
	btnBEvent:function(){
		var _t=this;

		$(_t.btnB).click(function(){
			if(_t.isHorV){
				_t.scrollRight();
			}else{
				_t.scrollDown();
			}
		});
	},
	elementsClick:function(){
		var _t=this;
		$(_t._outer_org_).find("li").each(function(it){
			$(this).click(function(){
				$(_t.targetTI).find("li").removeClass("cur");
				$(_t._outer_org_).find("li").removeClass("cur");
				$(this).addClass("cur");
				$(_t.targetTI).find("li").eq($(this).attr("Index")).addClass("cur");
			});
		});
	}
};
