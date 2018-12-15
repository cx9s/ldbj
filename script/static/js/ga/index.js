function get_article_by_ajax(id,name){
	//$(".J_newsC .row").html('')
	$.get('article_category.php',{pagesize:4,method:"ajax",id:id},function(data){
		data = $.parseJSON(data);
                        h = ''
        if (id == 38) {
    		$.each(data.result, function(index,values){
                a = '';
                for(var i = 1; i < values.pics.length; i++){
                    a += '<a rel="qmm_group" class="fancybox_'+values.id+'" data-fancybox-group="gallery" href="'+values.pics[i]+'"></a>'
                }
    			h += '<li data-id="'+values.id+'" class="col-xs-6 col-sm-3"><a class="fancybox fancybox_'+values.id+'" data-fancybox-group="gallery" rel="qmm_group" href="'+values.pics[0]+'" data-fancybox-group="gallery" data-href="article.php?id='+values.id+'"><div class="ximg"><img class="img-responsive"  alt="Responsive image" src="'+values.image+'" /></div></a>'+a+'<div class="xnr"><strong>'+values.title+'</strong><p>'+values.description+'</p><a href="news.php?id='+values.cat_id+'"><span class="xname">'+name+'</span></a><span class="xhr">|</span><span class="xtime">'+values.add_time+'</span></div></li>'
    	           })
        }else{
            $.each(data.result, function(index,values){
                h += '<li class="col-xs-6 col-sm-3"><a href="article.php?id='+values.id+'"><div class="ximg"><img class="img-responsive"  alt="Responsive image" src="'+values.image+'" /></div></a><div class="xnr"><strong>'+values.title+'</strong><p>'+values.description+'</p><a href="news.php?id='+values.cat_id+'"><span class="xname">'+name+'</span></a><span class="xhr">|</span><span class="xtime">'+values.add_time+'</span></div></li>'
               })
        };

                       $(".J_newsC .row").attr("data-id", data.result[0].cat_id).html(h);



	})
}

$(function(){
    get_article_by_ajax($(".J_news li:first").find("a").attr("cateid"),$(".J_news li:first").find("a").text())
    $(".J_news li").click(function(){
            $(this).addClass("cur").siblings().removeClass("cur");
            //var index = $(this).index();
            //$('.J_newsC').hide();
            //$('.J_newsC:eq('+index+')').show();
            id = $(this).find("a").attr("cateid")
            get_article_by_ajax(id,$(this).find("a").text());


            setTimeout(function(){
                $(".xnews .xcon .row[data-id = '38'] li").each(function(a,b){
                    $(".fancybox_"+$(this).attr("data-id")).fancybox({
                        'titlePosition'     : 'over',
                        'titleFormat'       : function(title, currentArray, currentIndex, currentOpts) {
                                return '<span id="fancybox-title-over">Image ' + (currentIndex + 1) + ' / ' + currentArray.length + (title.length ? ' &nbsp; ' + title : '') + '</span>';
                        }
                    });
                });
            },100)

    });

    $(".index_erweima img").hide();
    $(".xshare li:eq(0)").click(function(){
        $(".index_erweima img").eq(0).show();
        $(".index_erweima").stop().fadeIn(300)
    });
    $(".xshare li:eq(2)").click(function(){
        $(".index_erweima img").eq(1).show();
        $(".index_erweima").stop().fadeIn(300)
    });

    $(".index_erweima .close").click(function(){
        $(".index_erweima").stop().fadeOut(300)
        $(".index_erweima img").delay(300).hide();
    })
    $(".s0").text($(".xrank .cur .s1").text())


      $(".xvideo .xcon li").each(function(a,i){
        $(this).find("a.fancy_vid").attr("href", $(this).find(".video_hide iframe").attr("src"));
          $(this).find(".video_hide iframe").remove();
      })

      $(".xvideo .xcon li a.fancy_vid").fancybox();


    // $('.fancybox').fancybox();
})
