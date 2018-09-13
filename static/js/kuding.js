//自定义js文件

//通知区域条目的点击事件
function a_c(t) {
    t.siblings('.li_c').toggleClass("hidden");
    if (t.children(".ico").children().attr("class") === "fa fa-lg fa-hand-o-right") {
        t.children(".ico").children().attr("class", "fa fa-lg fa-hand-o-down");
    }
    else {
        t.children(".ico").children().attr("class", "fa fa-lg fa-hand-o-right");
    }
    t.parent().siblings().children('.li_c').addClass("hidden");
    t.parent().siblings().children('.main').children(".ico").children().attr("class", "fa fa-lg fa-hand-o-right");
}