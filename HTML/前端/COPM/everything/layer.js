
/**
 * jQuery-plugin-layer v0.3
 * author: 贤心
 * date: 2012-3-18
 * blog: http://xu.sentsin.com/
 * 相关交流群：176047036 （web前端开发-js面向对象）
 * (c) Sentsin Xu
 
 ***********************************

具体使用说明请详见：http://xu.sentsin.com/jquery/layer/
 */ 

(function($){	  
	var getPath = function(){
		var js = document.scripts || $("script");
		var jsPath;
		for(var i = js.length; i > 0; i--){
			if(js[i - 1].src.indexOf("layer.js") > -1){
				jsPath = js[i - 1].src.substring(0, js[i - 1].src.lastIndexOf("/") + 1);
			}
		}
		return jsPath;
	};
	if($("html").html().indexOf('png.js') == -1){
		ie6PNG = '<script type="text/javascript" src="' + getPath() + 'skin/png.js"></script>';
	}else{
		ie6PNG = '';
	};
	var iePNG = '<!--[if IE 6]>' + ie6PNG + '<![endif]-->'; 
	$("title").after('\n'+'<link rel="stylesheet" type="text/css" href="'+getPath()+'skin/layer.css"  />');
	$("head").after(iePNG);
	var iE6 = !-[1,] && !window.XMLHttpRequest;
	
	$.layer = function(deliver){
		deliver = $.extend({
			/*--- 默认配置 ---*/
			v_skin		: 0,
			v_shade		: true,
			v_title		: '信息',
			v_istitle	: true,
			v_box		: 0,
			v_btns		: 1,
			v_btn		: ['确定','取消'],
			v_offset	: ['200px','50%'],
			v_area		: ['310px','200px'],
			v_showclose	: true,
			v_closetype	: 0,
			v_msgtype	: 0,
			v_msg		: '',
			v_src		: 'http://xu.sentsin.com',
			v_move		: true,
			v_showtime	: 0,
			v_dom : '#xulayer'
		},deliver);
		
		//适应老版本属性。
		if(deliver.v_closebtn == false){deliver.v_showclose = deliver.v_closebtn;}
		if(deliver.v_button){deliver.v_btns = deliver.v_button;}
		if(deliver.v_button1){deliver.v_btn[0] = deliver.v_button1;}
		if(deliver.v_button2){deliver.v_btn[1] = deliver.v_button2;}
		if(deliver.v_top != null){deliver.v_offset[0] = deliver.v_top + 'px';}
		if(deliver.v_width != null){deliver.v_area[0] = deliver.v_width + 'px';}
		if(deliver.v_height != null){deliver.v_area[1] = deliver.v_height + 'px';}
		if(deliver.v_boxdom){deliver.v_dom = deliver.v_boxdom;}
		
		//if null
		if(deliver.v_btn[0] == ''){deliver.v_btn[0] = '确认';}
		if(deliver.v_btn[1] == ''){deliver.v_btn[1] = '取消';}
		
		
		var frame = new Array(
			'<span class="xubox_msg xubox_msgtype' + deliver.v_msgtype + '"></span><span class="xubox_text">' + deliver.v_msg + '</span>',	
			'<div class="xubox_page xubox_page_' + deliver.v_skin + '"></div>',
			'<iframe name="xubox_iframe" class="xubox_iframe" frameborder="0" src="' + deliver.v_src + '"></iframe>',				
			'<span class="xubox_loading xubox_loading_'+deliver.v_skin+'"></span>'
		);
		
		var H={i : $('.xubox_layer').length , j : $('#xubox_shade').length};
		var shade = '';
		
		if(deliver.v_shade == true && H.j < 1){
			shade = '<div id="xubox_shade" class="xubox_shade_'+deliver.v_skin+'"></div>';
		}
		if(deliver.v_area[0].indexOf('px') != -1){
			var _mleft = (parseInt(deliver.v_area[0])/2);
		}else{
			var _mleft = parseInt(deliver.v_area[0])/200*$(window).width();
		}
		
		if(deliver.v_box == 3){
			deliver.v_btns = 0;
			if(deliver.v_title == '信息'){deliver.v_title = '加载中'}
		}
					
		var boxhtml = '<div class="xubox_layer xubox_layer_' + deliver.v_skin + '">'
					+ '<div class="xubox_main xubox_main_' + deliver.v_skin + '">'
					+ frame[deliver.v_box]
					+ '<h2 class="xubox_title xubox_title_' + deliver.v_skin + '"><i></i><em>' + deliver.v_title + '</em></h2>'
					+ '<a class="xubox_close xubox_close' + deliver.v_closetype + '_' + deliver.v_skin + '" href="javascript:;"></a>'
					+ '<span class="xubox_botton"></span>'
					+ '</div></div>';
		
		/*--- 安装layer ---*/
		if(deliver.v_box == 0){
			if($('.xubox_text').length < 1){
				if($('.xubox_loading').length > 0){layer_close();}
				if(H.i > 0){
					$("body").append(boxhtml);	
				}else{
					$("body").append(shade + boxhtml);	
				}
			}
		}else{
			if(H.i == 0){$.layer({v_title:'插件警告',v_msg:'layer在输出时发现不应该的程序错误，请检查! '});}
			c = 0;
			layer_close();
			$("body").append(shade);
			if(deliver.v_box == 1){
				$(deliver.v_dom).show().wrap(boxhtml);
			}else{$("body").append(boxhtml);}
		}
		
		$('.xubox_layer').each(function(x){$xuboxlayer = $(this);});
		var L = $xuboxlayer.index('.xubox_layer');
		/*--- 风格化layer ---*/
		var $xubox_layer = $(".xubox_layer").eq(L);
		var $xubox_title = $(".xubox_title").eq(L);
		var $xubox_main = $(".xubox_main").eq(L);
		var $xubox_iframe = $(".xubox_iframe").eq(L);
		var $xubox_loading = $(".xubox_loading").eq(L);
		var $xubox_botton = $(".xubox_botton").eq(L);
		var $xubox_close = $(".xubox_close");
		
		if(deliver.v_offset[1].indexOf("px") != -1){
			var _left = _mleft + parseInt(deliver.v_offset[1]);
		}else{
			if(deliver.v_offset[1] == '50%'){
				var _left =  deliver.v_offset[1];
			}else{
				var _left =  _mleft + parseInt(deliver.v_offset[1])/200*$(window).width();
			}
		}
		
		$xubox_layer.css({'top' : deliver.v_offset[0] , 'left' : _left , 'width' : deliver.v_area[0] , 'height' : deliver.v_area[1] , 'margin-left' : -_mleft});
		
		
		//配置按钮
		var isbtn = $xubox_botton.length;
		if(isbtn > 0){
			switch(deliver.v_btns){
				case 0:
					$xubox_botton.html('').hide();
					break;
				case 2:
					$xubox_botton.html('<a href="javascript:;" class="xubox_yes xubox_botton2_' + deliver.v_skin + '">' + deliver.v_btn[0] + '</a>' + '<a href="javascript:;" class="xubox_no xubox_botton3_' + deliver.v_skin + '">' + deliver.v_btn[1] + '</a>');
					break;
				default:
					$xubox_botton.html('<a href="javascript:;" class="xubox_yes xubox_botton1_' + deliver.v_skin + '">' + deliver.v_btn[0] + '</a><a class="xubox_no" style="displa:none;"></a>');
			}
		}
		var $xubox_yes = $(".xubox_yes");
		var $xubox_no = $(".xubox_no");
		
		var H = {
			a : parseInt($xubox_layer.css("padding-bottom")),
			b : parseInt($xubox_title.height()),
			c : parseInt($xubox_main.css('margin-right'))*2,
			d : parseInt($xubox_loading.width()),
			e : parseInt($xubox_loading.height()),
			f : parseInt( $xubox_loading.css('margin-right'))*2,
			g : deliver.v_showtime,
			h : '',
			k : parseInt($xubox_main.css("margin-right"))
		}; 
		
		
		
		//对话框z-index优先
		if(deliver.v_box == 0){
			$xubox_layer.css({'z-index' : '19000002'});
		}
		//页面层风格化
		
		if(deliver.v_box == 1){
			autoHen = function(){
				_boxhen = $(deliver.v_dom).outerHeight() + $xubox_title.outerHeight() + $xubox_botton.find('a').outerHeight() + parseInt($xubox_botton.find('a').css('bottom')) + 20; 
				$xubox_main.css({height : _boxhen});
			};
			$('.xubox_page').css({'width' : $xubox_layer.width() - 2*H.k});
			if($xubox_layer.css('height') == '0px' || $xubox_layer.css('height') == 'auto'){
				autoHen();
			}
			if(deliver.v_istitle == true){
				$('.xubox_page').css({'top' : H.b + 15});
			}else{
				$('.xubox_page').css({'top' : 15});	
			}
			
		}
		//iframe层风格化
		if(deliver.v_box == 2){
			$xubox_iframe.css({'width' : $xubox_layer.width() - 2*H.k});
			deliver.v_istitle ? $xubox_iframe.height($xubox_layer.height() - H.b) : $xubox_iframe.height($xubox_layer.height());
			if(deliver.v_istitle == true){
				$xubox_iframe.css({'top' : H.b + H.a});
			}else{
				$xubox_iframe.css({'top' : H.a});	
			}
			$xubox_iframe.attr("src" , deliver.v_src);
		}
		//加载层风格化
		if(deliver.v_box == 3){
			deliver.v_showclose = false;
			deliver.v_move = false;
			$xubox_layer.css({'width' : (H.d + H.f + H.c)});
			deliver.v_istitle ? $xubox_layer.css({'height' : H.b + H.e + H.f}) : $xubox_layer.css({'height' : H.e + H.f});
			if(deliver.v_istitle == true){
				$('.xubox_loading').css({'top' : H.b + H.a});
			}else{
				$('.xubox_loading').css({'top' : H.a});	
			}
		}
		
		//标题宽度控制
		if(deliver.v_istitle == true){
			$xubox_title.css({'width' :$xubox_layer.width() - 2*H.k});
		}else{
			$('.xubox_title').eq(0).css({'width' :$xubox_layer.width() - 2*H.k});	
		}
		
		//自动关闭层
		if(deliver.v_showtime != 0){
			function maxLoad(){
				deliver.v_showtime--;
				if(deliver.v_showtime == 0){
					c =  L;
					layer_close();
					clearInterval(H.h);
					deliver.v_showtime = H.g;
				}
			};
			H.h = setInterval(maxLoad,1000);
		}
		
		deliver.v_move ? $xubox_title.css({'cursor':'move'}) : $xubox_title.css({'cursor':'auto'});		
		deliver.v_istitle 	||	$xubox_title.remove().hide();
		deliver.v_showclose ||	$xubox_close.remove().hide();
		deliver.v_istitle	||	$xubox_close.attr("class","xubox_close xubox_close1_" + deliver.v_skin);
		
		//建立全屏遮罩格局
		function layer_shade(){	
			var _s={x:$(document).width(),y:$(document).height()};
			if(iE6){
				_s={x:$(document).width(),x1:$(window).width(),y:$(document).height()};
				if(_s.x > _s.x1){_s.x = _s.x-22;}	//ie6的一个bug,此处22是滚动条的宽度。
			}
			$("#xubox_shade").css({'width' : _s.x , 'height' : _s.y});
			
		};
		layer_shade();
		$(window).resize(layer_shade);
		$(window).scroll(layer_shade);
		
		//IE6下始终在可视区域
		function ieFix(){
			$xubox_layer.css({'top' : $(document).scrollTop() + _ieTop});
		};
		if($xubox_layer.css('position') != 'fixed'){
			var _ieTop =  $xubox_layer.offset().top;
			ieFix(); 
			$(window).scroll(ieFix);
		}
		
		//拖拽层
		!deliver.v_move || $xubox_title.attr('move','ok');
		var mDiv = {e : false,x : 0,y : 0,i : 0};
		$('.xubox_title').mousedown(function(M){
			if($(this).attr('move') == 'ok'){
				mDiv.e = true; 
				mDiv.i = $(this).index('.xubox_title');
				$mlayer = $('.xubox_layer').eq(mDiv.i);
				mDiv.x = M.pageX - parseInt($mlayer.position().left);
				mDiv.y = M.pageY - parseInt($mlayer.position().top);
				$(document).mousemove(function(M){
					if(mDiv.e){
						var _x = M.pageX - mDiv.x;
						if($xubox_layer.css('position') == 'fixed'){
							var _y = M.pageY - mDiv.y - $(window).scrollTop();	
						}else{
							var _y = M.pageY - mDiv.y;	
						}
						$mlayer.css({"left" : _x , "top" : _y});
					}					  						   
				}).mouseup(function(){
					mDiv.e = false;
				});
			}
		});
		
		/*--- 关闭层 ---*/
		layer_close = function(){
			function close_page(){
				$close_page = $('.xubox_layer').eq(0).find('.xubox_page').find('*').eq(0);
				for(i = 0 ; i < 3 ; i++){
					$close_page.hide().unwrap();
					if(iE6){$('.xubox_layer').hide();}
					$('.xubox_title').remove().hide();
					$('.xubox_close').remove().hide();
					$('.xubox_botton').remove().hide();	
				}
			};
			if($('.xubox_layer').length == 1){$("#xubox_shade").remove().hide();}
			if(L == 0){
				if(deliver.v_box == 1){
					close_page()
				}else{
					$('.xubox_layer').remove().hide();	
				}
			}else{
				if(c < 1){
					if($('.xubox_iframe').length > 0){
						$('.xubox_layer').remove().hide();
						$("#xubox_shade").remove().hide();
					}else{
						$('.xubox_layer').eq(1).remove().hide();
						close_page();
						$("#xubox_shade").remove().hide();	
					}
				}else{
					$('.xubox_layer').eq(c).remove().hide();	
				}
			}
			clearInterval(H.h);
		};
		deliver = $.extend({
			close : function(){
				c = $(this).parents('.xubox_layer').index('.xubox_layer');
				if(c < 0){return false;}
				layer_close();
			},
			yes : function(){	
				c = $(this).parents('.xubox_layer').index('.xubox_layer');
				if(c < 0){return false;}
				if(c > 0 || L == 0){
					layer_close();	
				}
			},
			no : function(){
				c = $(this).parents('.xubox_layer').index('.xubox_layer');
				if(c < 0){return false;}
				if(c > 0 || L == 0){
					layer_close();	
				}
			}	
		},deliver);
		$('.xubox_layer').each(function(e){
			$(this).find('.xubox_close').click(deliver.close);
			$(this).find('.xubox_yes').click(deliver.yes);
			$(this).find('.xubox_no').click(deliver.no);
		});
		if(iE6){
			$('#xubox_shade,.xubox_layer').ieselect();
			DD_belatedPNG.fix("#xubox_shade,.xubox_layer,.xubox_title,.xubox_title i,.xubox_msg,.xubox_close");
		}
		
	}
	
	//修补IE6下，div无法覆盖select的bug	
	$.fn.ieselect = (iE6 ? function(A) {
		A = $.extend({
			top     : 'auto', 
			left    : 'auto', 
			width   : 'auto', 
			height  : 'auto',
			opacity : true,
			src     : 'javascript:false;'
		}, A);
		var html = '<iframe class="ieselect" frameborder="0" tabindex="-1" src="'+A.src+'"'
					+'style="display:block; position:absolute; z-index:-1;'
					+(A.opacity !== false?'filter:Alpha(Opacity=\'0\');':'')
					+'top:'+(A.top=='auto'?'expression(((parseInt(this.parentNode.currentStyle.borderTopWidth)||0)*-1)+\'px\')':prop(A.top))+';'
					+'left:'+(A.left=='auto'?'expression(((parseInt(this.parentNode.currentStyle.borderLeftWidth)||0)*-1)+\'px\')':prop(A.left))+';'
					+'width:'+(A.width=='auto'?'expression(this.parentNode.offsetWidth+\'px\')':prop(A.width))+';'
					+'height:'+(A.height=='auto'?'expression(this.parentNode.offsetHeight+\'px\')':prop(A.height))+';'
					+'"/>';
		return this.each(function() {
			if ( $(this).children('iframe.ieselect').length === 0 )
				this.insertBefore( document.createElement(html), this.firstChild );
			});
	} : function() { return this; });
	function prop(n) {
		return n && n.constructor === Number ? n + 'px' : n;
	}
	
	/*--- layer拓展函数,默认只设三个，其它形式层您可DIY。 ---*/
	layer_alert = function(a,b,c,d){	//普通对话框
		$.layer({
			v_msg : a,
			yes : b,
			v_msgtype : c,
			v_title : d
		});
	};
	layer_confirm = function(a,b,c,d){	//询问对话框
		$.layer({
			v_msg : a,
			yes : b,
			no : c,
			v_title : d,
			v_msgtype : 4,
			v_btns : 2
		}); 
	};	
	layer_load = function(a,b){	//加载
		$.layer({
			v_showtime : a,
			v_shade : b,
			v_istitle : false,
			v_box : 3
		}); 
	};
})(jQuery);

/*

 * the end
 */
