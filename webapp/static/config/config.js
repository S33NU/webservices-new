var CONFIG ={
    host : "http://localhost:8000"
}

function getCookie(){
    var cookieArr = document.cookie.split(";");
    userName = '';
    for(var i = 0; i < cookieArr.length; i++) {
        var cookiePair = cookieArr[i].split("=");

        if("userName"== cookiePair[0].trim()) {
              userName = cookiePair[1];
        }
    }
    return userName;
}