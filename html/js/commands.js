/**
 * Created by Junly on 2017/5/31.
 */
function ShowMenu(eid){
    var current = document.getElementById(eid);
    var list = current.parentElement.parentElement.children;
    for(var i=0 ;i< list.length; i++ ){
        if(list[i].children[1]){
            list[i].children[1].classList.add('hide');
        }else {
            continue;
        }
    }
    current.nextElementSibling.classList.remove('hide')
}
function ShowUser(show){
    var current = document.getElementById(show);
    current.classList.remove('hide')

}

function showAddHostHtml(){
    $("#maincontent").load("addhost.html");
}
function showHostInfoHtml(){
    $("#maincontent").load("edithost.html");
}


function showHostInfo(){
    var current = document.getElementById("zhezhao");
        current.classList.remove('hide');
    var info = document.getElementById("hostinfo");
        info.classList.remove('hide');
}
function closeInfo(){
    var current = document.getElementById("zhezhao");
        current.classList.add('hide');
    var info = document.getElementById("hostinfo");
        info.classList.add('hide');
}
function closeThisWindow(nid){
    var current = document.getElementById(nid);
    current.classList.add('hide');
}
function delHost(nid){
    var current = document.getElementById(nid);
    current.classList.remove('hide');
}