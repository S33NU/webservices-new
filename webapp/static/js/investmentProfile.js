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
            console.log(INVESTENT_QUESTIONS);
        }else if (res.statusCode == 1){

        }

    });



})();



$(document).ready(function(){
    $('#investmentForm').parsley();

 $('#investmentForm').on('submit', function(event){
  event.preventDefault();
    if($('#investmentForm').parsley().isValid()){
        dataObjList = []
        for(var i=0;i< INVESTENT_QUESTIONS.length;i++) {
            dataObj = {
                'order':INVESTENT_QUESTIONS[i].profqorder,
                'attribute':INVESTENT_QUESTIONS[i].profqname,
                'custresponse':null,
                'attributetype':INVESTENT_QUESTIONS[i].profqtype
            }
            if (INVESTENT_QUESTIONS[i].profqtype == "C" ){
                ele=$('input[name="'+INVESTENT_QUESTIONS[i].profqname+'"]');
                for(var j=0;j<ele.length;j++){ 
                    if($(ele[j]).val() != ''){
                        dataObj['custresponse'] = $(ele[j]).attr('id')+","+$(ele[j]).val(); 
                        break;
                    }
                }   
            }
            else if (INVESTENT_QUESTIONS[i].profqtype == "S" ){
                dataObj['custresponse']=$('input[name="'+INVESTENT_QUESTIONS[i].profqname+'"]:checked').val();
            }
            else if (INVESTENT_QUESTIONS[i].profqtype == "M" ){
                dataObj['custresponse']=$('select[name="'+INVESTENT_QUESTIONS[i].profqname+'"]').val();
            }     
            else if(INVESTENT_QUESTIONS[i].profqtype == "E" ){
                dataObj['custresponse']=$('input[name="'+INVESTENT_QUESTIONS[i].profqname+'"]').val();
            }
            
            dataObjList.push(dataObj);
    
        }
        
        $.post(CONFIG['host']+"/clients/investment-profile", JSON.stringify(dataObjList), function(res){
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
        
    }
});
})



