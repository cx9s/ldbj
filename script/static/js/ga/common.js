
$(function(){
	//首页搜索全局蒙版js
$(".xrli").click(function(){
	$(".sousuo_mb").addClass("active");
	$(".sousuo_mb input").val("")
	window.setTimeout(function(){$(".sousuo_mb input").focus();},0);
})
//input失去焦点事件
$(".sousuo_mb input").blur(function(){
	$(".sousuo_mb").removeClass("active");
	var key=$(".sousuo_mb input").val();
	var surl='/news.php?keyword='+key
	window.location.href=surl
})
$(".sousuo_mb input").keydown(function(event) {
	if (event.keyCode == 13) {
		$(".sousuo_mb").removeClass("active");
	}
})

	var _line = $('#_line');

	 if($(window).width() < 768){

	    var _height = $(window).height();
	    var _navHeight = $(".qmmNav").height();
	    $('.qmmSite').height(_height - _navHeight);
	}

	var resizeTimer = null;
	$(window).resize(function(){

	if (resizeTimer) clearTimeout(resizeTimer);

	   resizeTimer = setTimeout(function(){

	    $('.qmmSite').css("height","70px")
	    if($(window).width() > 767){

	        // PC端 - 二级导航 - 动效开始
	        $('.navbar-nav').find('li').each(function(index){
	            var _li = $(this);
	            var txt_width = _li.find('a').width();

	            _li.find('.pc-line').width(txt_width);
	            _li.find('.pc-line').css('margin-left',-txt_width/2);

	            _li.on('mouseenter',function(){
	            	_li.find('.pc-line').show();
	                _li.find('.pc-line').stop().animate({
	                    height:5
	                });

	                if(!_li.hasClass('xcur')){

	                    $('.subNav').find('ul').each(function(_index){
	                        if(index == _index + 1){
	                            $('.subNav').find('ul').eq(_index).addClass('active').siblings('ul').removeClass('active')
	                        }
	                    });
	                    $('.subNav').stop().slideDown()
	                }else{
	                	$('.subNav').find('ul').removeClass('active');
	                	$('.subNav').stop().slideUp()
	                }

	            });

	            _li.on('mouseleave',function(){
	                _li.find('.pc-line').stop().animate({
	                    height:0
	                });
	            })

	        });

	        $('.xmenu').on('mouseleave',function(){
	            $('.subNav').stop().slideUp();
	            $('.subNav').find('ul').removeClass('active')
	        });

	        $('.subNav').find('ul').each(function(){
	            var _ul = $(this);
	            _ul.find('li').each(function(){
	                $(this).on('mouseenter',function(){
	                    var _left = $(this).offset().left;
	                    var _width = $(this).width();
	                    _line.stop().animate({
	                        width:_width,
	                        left:(_left + 30)
	                    })
	                });

	            })
	        });

	        $('.subNav').on('mouseleave',function(){
	            _line.stop().animate({
	                width:0,
	                left:0
	            })
	        });

	        // 结束
			
	    }else{
		    var _height = $(window).height();
	    	var _navHeight = $(".qmmNav").height();
	   		$('.qmmSite').height(_height - _navHeight);

	        $('.navbar-nav').find('ul').each(function(){
	            var _ul = $(this);

	            _ul.find('li').each(function(){

	                var _li = $(this);

	                _li.find('.qmmDirct').eq(0).on('click',function(ev){
	                    if(_li.find('.mbSub').eq(0).find('a').length > 0){
	                        _li.find('.mbSub').stop().slideToggle(300);
	                        $(this).toggleClass('on');
	                        _li.siblings('li').find('.mbSub').stop().slideUp();
	                        _li.siblings('li').find('.qmmDirct').removeClass('on');
	                        $(this).parents('ul').siblings('ul').find('.mbSub').stop().slideUp();
	                        $(this).parents('ul').siblings('ul').find('.qmmDirct').removeClass("on");
	                        ev.stopPropagation();
	                    }
	                })
	                
	            });
	        })

	        $('.navbar-nav ul li .nav2').click(function(e){
	        	e.stopPropagation();
	        	if ($(this).siblings(".nav2_con").find("a").length > 0) {
	        		$(this).siblings(".nav2_con").stop().slideToggle(300);
	        		$(this).toggleClass('on');
	        	};
	        	return false
	        })

	    
	    }

	   } , 500);  

	}).resize();


$(".navbar-default .navbar-toggle").click(function(){
	$("#bs-example-navbar-collapse-1").stop().toggleClass("active")
	$(this).toggleClass("active")
	$("#get_input").val("")
	$("#get_submit").attr("type","button")
})
$("#get_submit").click(function(){
	console.log(1)
	var key=$("#get_input").val();
	var surl='http://byu2850360001.my3w.com/news.php?keyword='+key
	console.log(surl)
	window.location.href=surl
})

	$('.x_topbtn').hide();
	$(window).scroll(function(){
		if($(this).scrollTop() > 400){
		$('.x_topbtn').fadeIn();
		}else{
		$('.x_topbtn').fadeOut();
		}
	});
	
	$('.x_topbtn a').click(function(){
			$('html ,body').animate({scrollTop: 0}, 300);
			return false;
		});
	})



	// $(document).click(function(event){
	// 	if($(".qmmMenu").hasClass("in")){
	// 		event.stopPropagation();

	// 		$(".qmmMenu").stop().slideUp();
	// 	}
	// })