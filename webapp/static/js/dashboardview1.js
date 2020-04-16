function reviewInvestment(){
    dataObj ={
        "subscriptionType":"nirvana_plan_a",
        "amountPaid":"2500"
    };

    $.post(CONFIG['host']+"/clients/investment/review-investment", JSON.stringify(dataObj), function(res){
        data = res.data;
        
        if(res.statusCode == 0){
            
            window.location.href = "default";
            
        }else if(res.statusCode == 1){

        }else if(res.statusCode == 5){
            window.location.href = "../login"
        }
    });
}