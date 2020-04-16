//$('#saveStatus0').hide();
//$('#saveStatus1').hide();


$(document).ready(function(){

        $("#Lumpsum").change(function(){

            $("#Montly\\ \\(SIP\\)").prop('disabled', true);
            $("#Montly\\ \\(SIP\\)").removeAttr('required');
            $("#Montly\\ \\(SIP\\)").removeAttr('data-parsley-required-message');

  });
});


$(document).ready(function(){

        $("#Montly\\ \\(SIP\\)").change(function(){

            $("#Lumpsum").prop('disabled', true);
            $('#Lumpsum').removeAttr('required');
            $('#Lumpsum').removeAttr('data-parsley-required-message');

  });
});




var INVESTENT_QUESTIONS =[];

(function(){



    $.get(CONFIG['host']+"/clients/investment-profile/questions", function(res, status){
        
        if(res.statusCode == 0){

            INVESTENT_QUESTIONS = res.data;
            console.log(INVESTENT_QUESTIONS);
            $('#getProfqStatus1').hide();

        }else if (res.statusCode == 1){

            $('#getProfqStatus1').show();

        }else if(res.statusCode == 5){

            window.location.href = "../login"

            }

    });



})();



$(document).ready(function(){
    $('#saveStatus0').hide();
    $('#saveStatus1').hide();
    $('#getProfqStatus1').hide();
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
                ele=$('input[name="'+INVESTENT_QUESTIONS[i].profqname.split(" ").join("")+'"]');
                for(var j=0;j<ele.length;j++){ 
                    if($(ele[j]).val() != ''){
                        dataObj['custresponse'] = $(ele[j]).attr('id')+","+$(ele[j]).val(); 
                        break;
                    }
                }   
            }
            else if (INVESTENT_QUESTIONS[i].profqtype == "S" ){
                dataObj['custresponse']=$('input[name="'+INVESTENT_QUESTIONS[i].profqname.split(" ").join("")+'"]:checked').val();
            }
            else if (INVESTENT_QUESTIONS[i].profqtype == "M" ){
                dataObj['custresponse']=$('select[name="'+INVESTENT_QUESTIONS[i].profqname.split(" ").join("")+'"]').val();
            }     
            else if(INVESTENT_QUESTIONS[i].profqtype == "E" ){
                dataObj['custresponse']=$('input[name="'+INVESTENT_QUESTIONS[i].profqname.split(" ").join("")+'"]').val();
            }
            
            dataObjList.push(dataObj);
    
        }
        console.log(dataObjList)
        $.post(CONFIG['host']+"/clients/investment-profile", JSON.stringify(dataObjList), function(res){
            data = res.data;
            console.log(res)


            if(res.statusCode == 0){

             //alert("Details are saved Successfully");
             $('#saveInvestmentProfileButton').hide();
             $("input").prop('disabled', true);
             $('#saveStatus0').show();
             $('#saveStatus1').hide();
             $('#getProfqStatus1').hide();
             window.location.href = "default";

             }

            else if(res.statusCode == 5){

                    window.location.href = "../login"

            }

        else if(res.statusCode == 1){

         $('#saveStatus1').show();
         $('#saveStatus0').hide();
         $('#getProfqStatus1').hide();

        }

             
            
        });
        
    }
});
})



