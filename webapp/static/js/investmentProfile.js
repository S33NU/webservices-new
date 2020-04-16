
var INVESTENT_QUESTIONS =[];

(function(){



    $.get(CONFIG['host']+"/clients/investment-profile/questions", function(res, status){
        
        if(res.statusCode == 0){

            INVESTENT_QUESTIONS = res.data;
            
            $('#getProfqStatus1').hide();

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

            $('#getProfqStatus1').show();

        }else if(res.statusCode == 5){

            window.location.href = "../login"

            }

    });

    $.get(CONFIG['host']+"/clients/investment-profile", function(res, status){
        
        if(res.statusCode == 0){

            data  = res.data;
            $('#getProfqStatus1').hide();

            if (typeof data == "boolean"){
                console.log("Test");
            }else if(typeof data == "object"){
                $("#saveInvestmentProfileButton").hide();
                $('#updateInvestmentProfileButton').show();
                for(var i=0;i<data.length;i++){

                    if(data[i].attributetype == 'C'){
                        choiceEntry = data[i].custresponse.split(",");
                        $("#"+choiceEntry[0].split(" ").join("")).val(choiceEntry[1]);
                    }else if (data[i].attributetype == 'E'){
                        $('input[name="'+data[i].attribute.split(" ").join("")+'"]').val(data[i].custresponse);
                    }else if (data[i].attributetype == 'S'){
                        $("input[name='"+data[i].attribute.split(" ").join("")+"'][value='" + data[i].custresponse + "']").attr('checked', 'checked');

                    }else if (data[i].attributetype == 'M'){
                        $('select[name="'+data[i].attribute.split(" ").join("")+'"] option[value="'+data[i].custresponse+'"]').attr("selected","selected");
                    }






                }
            }
           

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
        var btnid = $(this).find("button:focus").attr('id');
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
                            dataObj['custresponse'] = $(ele[j]).attr('data-value')+","+$(ele[j]).val(); 
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
        
        if(btnid=="saveInvestmentProfileButton"){    
            $.post(CONFIG['host']+"/clients/investment-profile", JSON.stringify(dataObjList), function(res){
                data = res.data;
                if(res.statusCode == 0){
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
            }else if (btnid=="updateInvestmentProfileButton"){
                console.log("put")
            }
    }
});
})



