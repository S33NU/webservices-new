

function saveSubscriptionDetails(){
    console.log("Save Payment Details")
    dataObj ={
        "subscriptionType":"nirvana_plan_a",
        "amountPaid":"2500"
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