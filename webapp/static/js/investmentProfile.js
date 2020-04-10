var INVESTENT_QUESTIONS =[];

(function(){



    $.get(CONFIG['host']+"/clients/investment-profile/questions", function(res, status){
        
        if(res.statusCode == 0){

            INVESTENT_QUESTIONS = res.data;
            
        }else if (res.statusCode == 1){

        }

    });



})();

function saveInvestmentProfile(){
    if($('#investmentForm').parsley().isValid()){
        dataObj = {}
        for(var i=0;i< INVESTENT_QUESTIONS.length;i++) {
         
            if (INVESTENT_QUESTIONS[i].investqtype == "yes/no" && INVESTENT_QUESTIONS[i].investqselection == "singleselect" && INVESTENT_QUESTIONS[i].investqkey.includes(':')){
                ele=$('input[name="'+INVESTENT_QUESTIONS[i].investqkey+'"]');
                for(var j=0;j<ele.length;j++){ 
                    if($(ele[j]).val() != ''){
                        indexValues = INVESTENT_QUESTIONS[i].investqkey.split(':');
                        dataObj[indexValues[0]]=$(ele[j]).attr('id');
                        dataObj[indexValues[1]]=$(ele[j]).val();
                        break;
                    }
                }   


            }
            else if (INVESTENT_QUESTIONS[i].investqtype == "yes/no" && INVESTENT_QUESTIONS[i].investqselection == "singleselect" && !INVESTENT_QUESTIONS[i].investqkey.includes(':')){
                dataObj[INVESTENT_QUESTIONS[i].investqkey]=$('input[name="'+INVESTENT_QUESTIONS[i].investqkey+'"]:checked').val();
            }     
            else if(INVESTENT_QUESTIONS[i].investqtype == "text" && INVESTENT_QUESTIONS[i].investqselection == "null"){
                dataObj[INVESTENT_QUESTIONS[i].investqkey]=$('input[name="'+INVESTENT_QUESTIONS[i].investqkey+'"]').val();
            }
            
    
        }
        
        console.log(dataObj);
        $.post(CONFIG['host']+"/clients/investment-profile", JSON.stringify(dataObj), function(res){
            data = res.data;
            console.log(res)
             alert("Details are saved Successfully");
             $('#saveInvestmentProfileButton').hide()
             $("input").prop('disabled', true)
             
            
        });

    }
}