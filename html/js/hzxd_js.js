//菜单点击事件
$(".m_menu").click(function () {
    var all_list = $(this).parent().siblings().not("#ds");
    // var q = all_list.children().children().eq(1)
    // console.log(q)
        // q.addClass('hide');
    // $(this).siblings().removeClass('hide');
})

//登录事件
$("#login").click(function () {
    var u = $("#login-user").val()
    var p = $("#login-password").val()
    if (u.length == 0 ) {
        $("#u-err").removeClass('hide');
    }
    if (p.length == 0 ) {
         $("#p-err").removeClass('hide');
    }
    if((u=='admin') && (p=='admin')){
        location.href="index.html"
    }else {
        $("#u-p-err").removeClass('hide');
    }
})
