// JavaScript Document xt
$(function(){

	if( $(window).width() > 768 ) {
		$(".J_newsHot").insertAfter($(".J_Stime"));
	  }else{
		  $(".J_newsHot").insertAfter($(".J_Snews"));
	  }

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

	$(".J_click").click(function(){
		$(".j_poo").addClass("cur");
	});
	$(".J_off").click(function(){
		$(".j_poo").removeClass("cur");
	});

		// 倒计时

		// var	day = document.getElementById('day');
		// var	hours = document.getElementById('hours');
		// var	minutes = document.getElementById('minutes');
		// var seconds = document.getElementById('seconds');
		// 日 时 分 秒的dom对象
	//	countDownTime.init($(".xicon10").parent().text(), day, hours, minutes, seconds);
	//	countDownTime.start();

	// $(".xMnav").hover(function(){},function(){
	// $(".bottomLine").css("width",parseFloat($(".nav .xcur a").width())+"px");
	// $(".bottomLine").css("left",parseFloat($(".nav .xcur")[0].offsetLeft +45)+"px");
	// })
	// $(".xMnav li").hover(function(){
	// 	$(".bottomLine").css("width",parseFloat($(this).width())+"px");
	// 	$(".bottomLine").css("left",parseFloat($(this)[0].offsetLeft + 45)+"px");
	// });
	// $(".nav li").removeClass("selectedNav");
	// $(this).addClass("selectedNav");
	// $(".bottomLine").css("width",parseFloat($(".nav .xcur a").width())+"px");
	// $(".bottomLine").css("left",parseFloat($(".nav .xcur")[0].offsetLeft +45)+"px");


});



$(document).ready(function(){
	$(".jifen_table").find("tbody tr").mouseover(function(){
			$(this).addClass("qmmactive");
	});
	$(".jifen_table").find("tbody tr").mouseout(function(){
			$(this).removeClass("qmmactive");
	});
	// $(".jifen_table").find("tbody tr").each(function(index,ele){
	// 	//var ind = $(this).index();

	// 	if((index+1)%2 == 0) {
	// 		$(this).addClass("qmmactive");
	// 		console.log(index);
	// 	}
	// });

	$(".xSn-time .xSn-year>a").click(function(){
		$(this).addClass('cur')
		.find('i')//.addClass('down')
		.parent().next().slideDown(300)
		.parent().siblings().children('a').removeClass('cur')
		.find('i')//.removeClass('down')
		.parent().next().slideUp(200);
		 return false;
	});

	$(window).resize(function(){
		if( $(window).width() > 768 ) {
			$(".J_newsHot").insertAfter($(".J_Stime"));
		  }else{
			  $(".J_newsHot").insertAfter($(".J_Snews"));
		  }
	});



	$(".xNotice .xcon li").mouseover(function(){
    	$(this).addClass("cur");
	});
	$(".xNotice .xcon li").mouseout(function(){
		$(this).removeClass("cur");
	});


var swiper = new Swiper('.xban .swiper-container', {
        pagination: '.swiper-pagination',
        nextButton: '.swiper-button-next ',
        prevButton: '.swiper-button-prev',
        slidesPerView: 1,
        paginationClickable: true,
        spaceBetween: 30,
		autoplay: 5000,
        loop: true
    });


certifySwiper = new Swiper('.xcertify .swiper-container', {
	watchSlidesProgress: true,
	slidesPerView: 'auto',
	centeredSlides: true,
	loop: true,
	initialSlide: 1,
	loopedSlides: 5,
	//autoplay: 3000,
	prevButton: '.swiper-button-prev ',
	nextButton: '.swiper-button-next ',
	pagination: '.swiper-pagination',
	//paginationClickable :true,
	onProgress: function(swiper, progress) {
		for (i = 0; i < swiper.slides.length; i++) {
			var slide = swiper.slides.eq(i);
			var slideProgress = swiper.slides[i].progress;
			modify = 1;
			if (Math.abs(slideProgress) > 1) {
				modify = (Math.abs(slideProgress) - 1) * 0.3 + 1;
			}
			translate = slideProgress * modify * 100 + 'px';
			scale = 1 - Math.abs(slideProgress) / 5;
			zIndex = 999 - Math.abs(Math.round(10 * slideProgress));
			slide.transform('translateX(' + translate + ') scale(' + scale + ')');
			slide.css('zIndex', zIndex);
			slide.css('opacity', 1);
			if (Math.abs(slideProgress) > 3) {
				slide.css('opacity', 0);
			}
		}
	},
	onSetTransition: function(swiper, transition) {
		for (var i = 0; i < swiper.slides.length; i++) {
			var slide = swiper.slides.eq(i)
			slide.transition(transition);
		}

	},
	//处理分页器bug
	onSlideChangeStart: function(swiper) {
		if (swiper.activeIndex == 4) {
			swiper.bullets.eq(9).addClass('swiper-pagination-bullet-active');
			//console.log(swiper.bullets.length);
		}
	}
});


   var start = new Date().getTime();
    var end = new Date($(".xicon10").parent().text().replace(/-/g, '/')).getTime();
    var val = $("#qmmhide").val();
   // console.log($("#qmmhide").val())
   // console.log($(".xicon10").parent().text())
    var count = 0;

    var time = setInterval(function(){
        showTime();
    }, 1e3)

    function showTime(){
        count ++;
        var start = new Date().getTime();
        var time_distant = end - start;
        var ts = time_distant/1e3;
        var dd =Math.floor(ts/60/60/24);
        var hh =Math.floor(ts/60/60%24);
        var mm =Math.floor(ts/60%60);
        var ss =Math.floor(ts%60);

        if(ts > 0){

            $('#day').text(dd);
            $('#hours').text(hh);
            $('#minutes').text(mm);
            $('#seconds').text(ss);
            //console.log(dd)


            if(dd == 0 && hh <= 1){
				$('.x_g').find('.btn-8').attr("href",val);
				$('.x_g').find('i').text('查看比赛');
            }

        }else{

            //console.log(2);
            clearInterval(time);
            $('#day').text(00);
            $('#hours').text(00);
            $('#minutes').text(00);
            $('#seconds').text(00);
            $('.x_g').find('.btn-8').attr("href",val);
            $('.x_g').find('i').text('查看比赛');

        }


    }

});

//倒计时 =====


// var countDownTime = {
// 	init: function(a, b, c, d, e) {
// 		this.t = a, this.d = b, this.h = c, this.m = d, this.s = e
// 	},
// 	start: function() {
// 		var a = this;
// 		setInterval(a.timer, 1e3)
// 	},
// 	timer: function(a) {
// 		var b, c, d, e, f, g, h;
// 		a = this.countDownTime,
// 		b = new Date,
// 		c = new Date(a.t),
// 		d = c.getTime() - b.getTime(),
// 		e = Math.floor(a.formatTime(d, "day")),
// 		f = Math.floor(a.formatTime(d, "hours")),
// 		g = Math.floor(a.formatTime(d, "minutes")),
// 		h = Math.floor(a.formatTime(d, "seconds")),
// 		a.d && (a.d.innerText = a.formatNumber(e)),
// 		a.h && (a.h.innerText = a.formatNumber(f)),
// 		a.m && (a.m.innerText = a.formatNumber(g)),
// 		a.s && (a.s.innerText = a.formatNumber(h))
// 	},
// 	formatNumber: function(a) {
// 		if(a<=0){a=0}
// 		return a = a.toString(), a[1] ? a : "0" + a
// 	},
// 	formatTime: function(a, b) {
// 		switch (b) {
// 			case "day":
// 				return a / 1e3 / 60 / 60 / 24;
// 			case "hours":
// 				return a / 1e3 / 60 / 60 % 24;
// 			case "minutes":
// 				return a / 1e3 / 60 % 60;
// 			case "seconds":
// 				return a / 1e3 % 60
// 		}
// 	}
// };
