
var INVESTENT_QUESTIONS =[];
var INVESTENT_PROFILE_RESPONSE = [];
(function(){



    $.get(CONFIG['host']+"/clients/investment-profile/questions", function(res, status){
        
        if(res.statusCode == 0){

            INVESTENT_QUESTIONS = res.data;
            
            $('#saveStatus1').hide();

            obj=INVESTENT_QUESTIONS.find(ele=>{
                return ele.profqtype=='C'
            })
            if(obj != undefined){
                val1=obj.values[0].replace(/[{()}]/g, '').split(" ").join("");
                val2=obj.values[1].replace(/[{()}]/g, '').split(" ").join("");
                $("#"+val1).on("change paste keyup",function(){
                    val=$(this).val();
                   
                    if(val != ''){
                        $("#"+val2).prop('disabled', true);
                        $("#"+val2).removeAttr('required');
                        $("#"+val2).removeAttr('data-parsley-required-message');
                    } else if(val == ''){
                        $("#"+val1).prop('disabled', true);
                        $("#"+val1).removeAttr('required');
                        $("#"+val1).removeAttr('data-parsley-required-message');
                        $("#"+val2).prop('disabled', false);
                        $("#"+val2).attr('required',true);
                        $("#"+val2).attr('data-parsley-required-message',"Field is required");
                    }

                });
                $("#"+val2).on("change paste keyup",function(){

                    val=$(this).val();
                    if(val != ''){
                        $("#"+val1).prop('disabled', true);
                        $("#"+val1).removeAttr('required');
                        $("#"+val1).removeAttr('data-parsley-required-message');
                    } else if(val == ''){
                        $("#"+val2).prop('disabled', true);
                        $("#"+val2).removeAttr('required');
                        $("#"+val2).removeAttr('data-parsley-required-message');
                        $("#"+val1).prop('disabled', false);
                        $("#"+val1).attr('required',true);
                        $("#"+val1).attr('data-parsley-required-message',"Field is required");
                    }

                });
            }


        }else if (res.statusCode == 1){

            $('#saveStatus1').show();

        }else if(res.statusCode == 5){

            window.location.href = "../login"

            }

    });

    $.get(CONFIG['host']+"/clients/investment-profile", function(res, status){
        
        if(res.statusCode == 0){

            data  = res.data;
            $('#saveStatus1').hide();

            if (typeof data == "boolean"){
                $("#saveButtons").show();
                $('#updateButtons').hide();
            }else if(typeof data == "object"){
                $("#updateButtons").show();
                $('#saveButtons').hide();
                INVESTENT_PROFILE_RESPONSE = data;
                appendExistingData()
            }
           

        }else if (res.statusCode == 1){

            $('#saveStatus1').show();

        }else if(res.statusCode == 5){

            window.location.href = "../login"

            }

    });







})();



$(document).ready(function(){
    $('#saveStatus0').hide();
    $('#saveStatus1').hide();
    $('#investmentForm').parsley();

 $('#investmentForm').on('submit', function(event){
  event.preventDefault();
    if($('#investmentForm').parsley().isValid()){
        dataObjList = []
        var btnid = $(this).find("button:focus").attr('id');
        for(var i=0;i< INVESTENT_QUESTIONS.length;i++) {
                dataObj = {
                    'order':INVESTENT_QUESTIONS[i].profqorder,
                    'attribute':INVESTENT_QUESTIONS[i].profqname,
                    'custresponse':null,
                    'attributetype':INVESTENT_QUESTIONS[i].profqtype
                }
                if (INVESTENT_QUESTIONS[i].profqtype == "C" ){
                    ele=$('input[name="'+INVESTENT_QUESTIONS[i].profqname.split(" ").join("")+'"]:enabled');
                    dataObj['custresponse'] = $(ele).attr('data-value')+","+$(ele).val();
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
        
        if(btnid=="saveInvestmentProfileButton"){    
            $.post(CONFIG['host']+"/clients/investment-profile", JSON.stringify(dataObjList), function(res){
                data = res.data;
                if(res.statusCode == 0){
                     $('#saveButtons').hide();
                     $('#saveStatus0').show();
                     $('#saveStatus1').hide();
                    window.location.href = "default";

                 }

                else if(res.statusCode == 5){

                    window.location.href = "../login"

                }

                else if(res.statusCode == 1){

                     $('#saveStatus1').show();
                    $('#saveStatus0').hide();
                }
             });
            }else if (btnid=="updateInvestmentProfileButton"){
         
                $.ajax({
                    url: CONFIG['host']+"/clients/investment-profile",
                    type: 'PUT',
                    data:JSON.stringify(dataObjList),
                    dataType : "json",
                    success: function(res) {
                        
                        data = res.data;
                        if(res.statusCode == 0){
                            $('#updateButtons').hide();
                            $('#saveStatus0').show();
                            $('#saveStatus1').hide();
                           window.location.href = "default";
       
                        }
       
                       else if(res.statusCode == 5){
       
                           window.location.href = "../login"
       
                       }
       
                       else if(res.statusCode == 1){
       
                            $('#saveStatus1').show();
                           $('#saveStatus0').hide();
                       }       
                                   
                    }
            
                });
            }
    }
});
})

function appendExistingData(){

    for(var i=0;i<INVESTENT_PROFILE_RESPONSE.length;i++){

        if(INVESTENT_PROFILE_RESPONSE[i].attributetype == 'C'){
            choiceEntry = INVESTENT_PROFILE_RESPONSE[i].custresponse.split(",");
            $("#"+choiceEntry[0].replace(/[{()}]/g, '').split(" ").join("")).val(choiceEntry[1]);
            $("input[name='"+INVESTENT_PROFILE_RESPONSE[i].attribute.split(" ").join("")+"']").not("[id='"+choiceEntry[0].replace(/[{()}]/g, '').split(" ").join("")+"']").prop("disabled", true);
            $("input[name='"+INVESTENT_PROFILE_RESPONSE[i].attribute.split(" ").join("")+"']").not("[id='"+choiceEntry[0].replace(/[{()}]/g, '').split(" ").join("")+"']").removeAttr('required');
            $("input[name='"+INVESTENT_PROFILE_RESPONSE[i].attribute.split(" ").join("")+"']").not("[id='"+choiceEntry[0].replace(/[{()}]/g, '').split(" ").join("")+"']").removeAttr('data-parsley-required-message');
        }else if (INVESTENT_PROFILE_RESPONSE[i].attributetype == 'E'){
            $('input[name="'+INVESTENT_PROFILE_RESPONSE[i].attribute.split(" ").join("")+'"]').val(INVESTENT_PROFILE_RESPONSE[i].custresponse);
        }else if (INVESTENT_PROFILE_RESPONSE[i].attributetype == 'S'){
            $("div[data-id='"+INVESTENT_PROFILE_RESPONSE[i].attribute.split(" ").join("")+"']").buttonset();
            $("input[name='"+INVESTENT_PROFILE_RESPONSE[i].attribute.split(" ").join("")+"'][value='" + INVESTENT_PROFILE_RESPONSE[i].custresponse + "']").attr('checked', 'checked');            
            $("div[data-id='"+INVESTENT_PROFILE_RESPONSE[i].attribute.split(" ").join("")+"']").buttonset('refresh');
        }else if (INVESTENT_PROFILE_RESPONSE[i].attributetype == 'M'){
            $('select[name="'+INVESTENT_PROFILE_RESPONSE[i].attribute.split(" ").join("")+'"]').val(INVESTENT_PROFILE_RESPONSE[i].custresponse);
        }






    }
}

function revertToOriginalData(){
    appendExistingData()
}