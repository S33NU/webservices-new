function goNextPage(){

    document.cookie = "userName=cvalue;"
    $.get("http://localhost:8000/clients/subscriptions", function(res, status){
        //data = res.data;
        
       console.log(res)
       //window.location.href = "savePassword"
    });



   
}