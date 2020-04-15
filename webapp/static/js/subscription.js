

function saveSubscriptionDetails(){
    console.log("Save Payment Details")
    dataObj ={
        'servidList':[1,3],
        'paymentmod':"card",
        'paygateway':"Phonepay",
        'payamount':50000.89,
        'payreference':"refer"
    };

   
    $.post(CONFIG['host']+"/clients/subscriptions/subscription-paid", JSON.stringify(dataObj), function(res){
        data = res.data;
        console.log(res);
        if(res.statusCode == 0){
            console.log("sdad")
            window.location.href = "default";
            
        }else if(res.statusCode == 1){

        }
    });
}