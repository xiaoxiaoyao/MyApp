;(function($){
	if(typeof $.fn.DURoll != 'undefined') return;
	$.fn.DURoll = function(options) {
		opts = $.extend({
			rotationSpeed: 10000,
			showlist: true
		}, options || {});

		var $this = this,
			$bdWidth = $('body').innerWidth(),
			$ItemW = 1920,
			$slideList = $this.find('.slide-list'),
			$slideNum = $this.find('.slide-num'),
			$Num = $slideList.find('li').length,
			$slideW = ($Num+1)*$ItemW,
			$current = 0,
			$Left = 0;

		if($bdWidth<975){
			$ItemW = 975;
		}else if($bdWidth>1920){
			$ItemW = 1920;
		}else{
			$ItemW = $bdWidth;
		};

		$slideList.append('<li></li>');
		$slideList.find('li').last().html($slideList.find('li').eq(0).html());
		$slideList.find('li').last().attr('style',$slideList.find('li').eq(0).attr('style'));
		$this.css({
			'width':$ItemW+'px',
			'overflow':'hidden'
		});
		$slideList.css('width',$slideW+'px');
		$slideList.find('li').css({
			'float':'left',
			'width': $ItemW+'px'
		});

		function Goto(){
			(function(){
				$Left = $current*$ItemW;
				$slideList.stop();
				$slideList.animate({'margin-left':-$Left+'px'}, 800,function(){
					if($current > $Num){
						$slideList.css('margin-left','0px');
						$current = 1;
					}
				});
				GoAddClass($current);
				$Left = $current*$ItemW;
				$current++;
				running=setTimeout(arguments.callee, opts.rotationSpeed);
			})();
		};Goto();

		function GoNext(){
			$slideNum.find('li').each(function(i){
				$(this).click(function(){
					window.clearTimeout(running);
					$current = i;
					Goto();
				});
			})
		};
		if(opts.showlist){GoNext();}

		function GoAddClass(I){
			if(I>$Num-1){
				I = 0;
			}
			$slideNum.find('li').eq(I).addClass('current').siblings('li').removeClass('current');
		};

	}
})(jQuery);
