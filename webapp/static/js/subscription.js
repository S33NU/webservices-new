

function saveSubscriptionDetails(){
    console.log("Save Payment Details")
    dataObj ={
        'servidList':[1],
        'paymentmod':"card",
        'paygateway':"Phonepay",
        'payamount':50000.89,
        'payreference':"refer"
    };

   
    $.post(CONFIG['host']+"/clients/subscriptions/subscription-paid", JSON.stringify(dataObj), function(res){
        data = res.data;
       
        if(res.statusCode == 0){
            window.location.href = "default";
            
        }else if(res.statusCode == 1){

        }
    });
}