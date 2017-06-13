/**
 * Created by Junly on 2017/5/26.
 */


function Login(){
    var user=document.getElementById('user').value
    var passwd=document.getElementById('passwd').value
    if (user=='admin' && passwd=='huang'){
        alert('login sucesses.')
    }else{
        alert('login failed.')
    }

}

function ShowMenu(nid){
    var Current_item = document.getElementById(nid);
    var item_list = Current_item.parentElement.parentElement.children;
    for(i=0;i<item_list.length;i++){
        item_list[i].children[1].classList.add('hide');
    }
    Current_item.nextElementSibling.classList.remove('hide')
}
