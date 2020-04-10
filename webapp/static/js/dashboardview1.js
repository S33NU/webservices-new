function reviewInvestment(){
    console.log("Save Documents")
    dataObj ={
        "subscriptionType":"nirvana_plan_a",
        "amountPaid":"2500"
    };

    $.post(CONFIG['host']+"/clients/investment/review-investment", JSON.stringify(dataObj), function(res){
        data = res.data;
        console.log(res);
        if(res.statusCode == 0){
            console.log("sdad")
            window.location.href = "default";
            
        }else if(res.statusCode == 1){

        }else if(res.statusCode == 5){
            window.location.href = "../login"
        }
    });
}