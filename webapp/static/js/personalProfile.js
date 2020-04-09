var PROFILE_QUESTIONS =[];
 $('#saveStatus0').hide();
 $('#saveFailStatus').hide();
(function(){



    $.get(CONFIG['host']+"/clients/personal-profile/questions", function(res, status){

        if(res.statusCode == 0){

            PROFILE_QUESTIONS = res.data;

        }else if (res.statusCode == 1){

        }

    });



})();



$(document).ready(function(){
    $('#Pform').parsley();

 $('#Pform').on('submit', function(event){
  event.preventDefault();
  if($('#Pform').parsley().isValid()){


        dataObj = {}
        userName=getCookie();
        dataObj['userName']=userName;
        for(var i=0;i< PROFILE_QUESTIONS.length;i++) {


            if (PROFILE_QUESTIONS[i].profqtype == "yes/no" && PROFILE_QUESTIONS[i].profqselection == "singleselect" && !PROFILE_QUESTIONS[i].profqkey.includes(':')){
                dataObj[PROFILE_QUESTIONS[i].profqkey]=$('input[name="'+PROFILE_QUESTIONS[i].profqkey+'"]:checked').val();
            }


            else if(PROFILE_QUESTIONS[i].profqtype == "text" && PROFILE_QUESTIONS[i].profqselection == "null"){
                dataObj[PROFILE_QUESTIONS[i].profqkey]=$('input[name="'+PROFILE_QUESTIONS[i].profqkey+'"]').val();
            }


            else if (PROFILE_QUESTIONS[i].profqtype == "list" && PROFILE_QUESTIONS[i].profqselection == "singleselect" && !PROFILE_QUESTIONS[i].profqkey.includes(':')){
                dataObj[PROFILE_QUESTIONS[i].profqkey]=$('option[name="'+PROFILE_QUESTIONS[i].profqkey+'"]:checked').val();
            }

        }

        console.log(dataObj);
        $.post(CONFIG['host']+"/clients/personal-profile", JSON.stringify(dataObj), function(res){
            data = res.data;
            console.log(res)
                    if(res.statusCode == 0){

//             alert("Details are saved Successfully");
             $('#submit').hide()
             $("input").prop('disabled', true)
             $("#AgeDropdownId").prop('disabled',true)
             $('#saveStatus0').show();


        }
        else{

         $('#saveFailStatus').show();

        }


        });

    }
});
})









