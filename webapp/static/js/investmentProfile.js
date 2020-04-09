 $('#saveStatus0').hide();
 $('#saveStatus5').hide();


$(document).ready(function(){
        $("#lump_sum").change(function(){
        $("#month_sip").prop('disabled', true);
        $('#month_sip').removeAttr('required');
        $('#month_sip').removeAttr('data-parsley-required-message');
  });
});


$(document).ready(function(){
        $("#month_sip").change(function(){
        $("#lump_sum").prop('disabled', true);
        $('#lump_sum').removeAttr('required');
        $('#lump_sum').removeAttr('data-parsley-required-message');

  });
});




var INVESTENT_QUESTIONS =[];

(function(){



    $.get(CONFIG['host']+"/clients/investment-profile/questions", function(res, status){
        
        if(res.statusCode == 0){

            INVESTENT_QUESTIONS = res.data;
            
        }else if (res.statusCode == 1){

        }

    });



})();



$(document).ready(function(){
    $('#investmentForm').parsley();

 $('#investmentForm').on('submit', function(event){
  event.preventDefault();
    if($('#investmentForm').parsley().isValid()){
        dataObj = {}
        userName=getCookie();
        dataObj['userName']=userName;
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


            if(res.statusCode == 0){

//             alert("Details are saved Successfully");
             $('#saveInvestmentProfileButton').hide();
             $("input").prop('disabled', true);
             $('#saveStatus0').show();
             $('#saveStatus5').hide();
             window.location.href = "default";

             }

            else if(res.statusCode == 5){

                    window.location.href = "../login"

            }

        else if(res.statusCode == 1){

         $('#saveStatus5').show();
         $('#saveStatus0').hide();

        }

             
        });

    };
});
})



