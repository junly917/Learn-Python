//菜单点击事件
$(".item .menu").click(function () {
    var all_list = $(this).parent().siblings();
    all_list.children().eq(1).addClass('hide');
    $(this).siblings().removeClass('hide');
})


