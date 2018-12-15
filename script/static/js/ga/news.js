function get_article_by_ajax(id,page,date,kw){
    $(".xNotice .xcon ul").html('')

    $.get('article_category.php',{pagesize:18,method:"ajax",id:id,page:page,date:date,keyword:kw},function(data){
        data = $.parseJSON(data);
        h = ''
        $("#totalpage").val(data.page.page_count) 
        $.each(data.result, function(index,values){
            //h = '<li class="col-xs-6 col-sm-3"><div class="ximg"><img src="'+values.image+'" /></div><div class="xnr"><strong>'+values.title+'</strong><p>'+values.description+'</p><a href="'+values.url+'"><span class="xname">'+name+'</span></a><span class="xhr">|</span><span class="xtime">'+values.add_time+'</span></div></li>'
            h += '<li><div class="x_box"><div class="ximg"><a href="#"><img src="'+values.image+'" class="img-responsive" alt="Responsive image" /></a></div><div class="xnr"><a href="'+values.url+'"><span class="xname">'+values.cat_name+'</span></a><span class="xhr">|</span><span class="xtime">'+values.add_time+'</span><strong><a href="'+values.url+'">'+values.title+'</a></strong><i class="xicon16"></i></div></div></li>'
        })

        $(".xNotice .xcon ul").append(h)
        //
        //alert(data.page.page_count)
        //return data.page.page_count; 
    //})
    })
}
function test(total){
       // alert(size)
        $("#pagination_10").delay(5000).whjPaging({
                css: 'css-2',
                totalPage: $("#totalpage").val(),
                showPageNum: 5,
                isShowFL: false,
                isShowPageSizeOpt: false,
                isShowSkip: false,
                isShowRefresh: false,
                isShowTotalPage: true,
                isResetPage: false,
                callBack: function (currPage, pageSize) {
                    console.log('currPage:' + currPage + '     pageSize:' + pageSize);
                    get_article_by_ajax($("#cat_id").val(),currPage,$("#date").val(),$('#kw').val())
                }

        });
    }
$(function(){
    
    //get_article_by_ajax($("#cat_id").val(),1)
    test()
    //setTimeout("test("++")",3000);
    //get_article_by_ajax($("#cat_id").val(),1),
    //test()
    //
    

    
})