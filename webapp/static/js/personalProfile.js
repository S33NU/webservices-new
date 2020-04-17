//$('#saveStatus0').hide();
// $('#saveStatus1').hide();


var PROFILE_QUESTIONS =[];

(function(){



    $.get(CONFIG['host']+"/clients/personal-profile/questions", function(res, status){

        if(res.statusCode == 0){

            PROFILE_QUESTIONS = res.data;
            
            $('#saveStatus1').hide();

        }else if (res.statusCode == 1){

            $('#saveStatus1').show();

        }else if(res.statusCode == 5){

            window.location.href = "../login"

        }

    });


   /* $.get(CONFIG['host']+"/clients/customer/email-mobile", function(res, status){


        if(res.statusCode == 0){

            var data = res.data;
            

            $("#RegisteredMobile").val(data.custregmobile)
            $("#RegisteredMobile").prop("disabled", true);
            if(data.custemail != null){
                $("#EMail").val(data.custemail)
                $("#EMail").prop("disabled", true);

            }

        }

    });
*/

    $.get(CONFIG['host']+"/clients/personal-profile", function(res, status){


         data=res.data;

        if(res.statusCode == 0){
                    $('#saveStatus1').hide();


            if (data instanceof Object && data instanceof Array){
                $("#updateButtons").show();
                $('#saveButtons').hide();
                console.log("Test");
                for(var i=0;i<data.length;i++){

                    if(data[i].attributetype == 'C'){
                        choiceEntry = data[i].custresponse.split(",");
                        $("#"+choiceEntry[0].replace(/[{()}]/g, '').split(" ").join("")).val(choiceEntry[1]);
                    }else if (data[i].attributetype == 'E'){
                        $('input[name="'+data[i].attribute.split(" ").join("")+'"]').val(data[i].custresponse);
                    }else if (data[i].attributetype == 'S'){
                        $("input[name='"+data[i].attribute.split(" ").join("")+"'][value='" + data[i].custresponse + "']").attr('checked', 'checked');

                    }else if (data[i].attributetype == 'M'){
                        $('select[name="'+data[i].attribute.split(" ").join("")+'"] option[value="'+data[i].custresponse+'"]').attr("selected","selected");
                    }

                }
            }

            else{

                $("#saveButtons").show();
                $('#updateButtons').hide();

                $("#RegisteredMobile").val(data.custregmobile)
                     if(data.custemail != null){
                            $("#EMail").val(data.custemail)
                        }



            }
        }
        else if (res.statusCode == 1){

            $('#saveStatus1').show();

        }else if(res.statusCode == 5){

            window.location.href = "../login"

            }

    });


})();



$(document).ready(function(){
    $('#saveStatus0').hide();
    $('#saveStatus1').hide();
    $('#Pform').parsley();

 $('#Pform').on('submit', function(event){
  event.preventDefault();
  if($('#Pform').parsley().isValid()){


        dataObjList = []
        custdataObj={}
        var btnid = $(this).find("button:focus").attr('id');
        for(var i=0;i< PROFILE_QUESTIONS.length;i++) {
        dataObj = {
                'order':PROFILE_QUESTIONS[i].profqorder,
                'attribute':PROFILE_QUESTIONS[i].profqname,
                'custresponse':null,
                'attributetype':PROFILE_QUESTIONS[i].profqtype
            }



            if (PROFILE_QUESTIONS[i].profqtype == "S" ){
                dataObj['custresponse']=$('input[name="'+PROFILE_QUESTIONS[i].profqname.split(" ").join("")+'"]:checked').val();
                custdataObj[PROFILE_QUESTIONS[i].profqname.split(" ").join("")]=$('input[name="'+PROFILE_QUESTIONS[i].profqname.split(" ").join("")+'"]:checked').val();
            }


            else if(PROFILE_QUESTIONS[i].profqtype == "E" ){
                dataObj['custresponse']=$('input[name="'+PROFILE_QUESTIONS[i].profqname.split(" ").join("")+'"]').val();
                custdataObj[PROFILE_QUESTIONS[i].profqname.split(" ").join("")]=$('input[name="'+PROFILE_QUESTIONS[i].profqname.split(" ").join("")+'"]').val();
            }


            else if (PROFILE_QUESTIONS[i].profqtype == "M"){
                dataObj['custresponse']=$('select[name="'+PROFILE_QUESTIONS[i].profqname.split(" ").join("")+'"]').val();
                custdataObj[PROFILE_QUESTIONS[i].profqname.split(" ").join("")]=$('select[name="'+PROFILE_QUESTIONS[i].profqname.split(" ").join("")+'"]').val();
            }
            dataObjList.push(dataObj);
        }
            custObj={
            'custProfile' :dataObjList,
            'cust' :custdataObj
            }
        
                if(btnid=="saveInvestmentProfileButton"){$.post(CONFIG['host']+"/clients/personal-profile", JSON.stringify(custObj), function(res){
            data = res.data;
            
                    if(res.statusCode == 0){

             //alert("Details are saved Successfully");
             $('#submit').hide();
             $("input").prop('disabled', true);
             $("#AgeGroup").prop('disabled',true);
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
                    url: CONFIG['host']+"/clients/personal-profile",
                    type: 'PUT',
                    data:JSON.stringify(custObj),
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