//$('#saveStatus0').hide();
// $('#saveStatus1').hide();


var PROFILE_QUESTIONS =[];

(function(){



    $.get(CONFIG['host']+"/clients/personal-profile/questions", function(res, status){

        if(res.statusCode == 0){

            PROFILE_QUESTIONS = res.data;
            console.log(PROFILE_QUESTIONS);
            $('#getProfqStatus1').hide();

        }else if (res.statusCode == 1){

            $('#getProfqStatus1').show();

        }else if(res.statusCode == 5){

            window.location.href = "../login"

        }

    });


    $.get(CONFIG['host']+"/clients/customer/email-mobile", function(res, status){
        

        if(res.statusCode == 0){

            var data = res.data;
            console.log(data)

            $("#RegisteredMobile").val(data.custregmobile)
            $("#RegisteredMobile").prop("disabled", true);
            if(data.custemail != null){
                $("#EMail").val(data.custemail)
                $("#EMail").prop("disabled", true);

            }

        }

    });



})();



$(document).ready(function(){
    $('#saveStatus0').hide();
    $('#saveStatus1').hide();
    $('#getProfqStatus1').hide();
    $('#Pform').parsley();

 $('#Pform').on('submit', function(event){
  event.preventDefault();
  if($('#Pform').parsley().isValid()){


        dataObjList = []
        custdataObj={}


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
        console.log(custObj);
        $.post(CONFIG['host']+"/clients/personal-profile", JSON.stringify(custObj), function(res){
            data = res.data;
            console.log(res)
                    if(res.statusCode == 0){

             //alert("Details are saved Successfully");
             $('#submit').hide();
             $("input").prop('disabled', true);
             $("#AgeGroup").prop('disabled',true);
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