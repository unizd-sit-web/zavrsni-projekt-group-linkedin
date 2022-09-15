function searchFunct(){
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById('query');
    filter = input.value.toUpperCase();
    ul = document.getElementById("myUL");
    li = ul.getElementsByTagName('li');

    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
} /* Pull from database instead of predetermined list*/

function storeUser(){ 
    var user = new Object();
    user.name = document.getElementById("name").value;
    user.email = document.getElementById("email").value;
    user.language = document.getElementById("language").value;
  /* Store user to database*/
}

