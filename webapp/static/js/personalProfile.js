/*$(document).ready(function validateForm(){
 var instance = $('#Pform').parsley();*/
$(document).ready(function(){
    $('#Pform').parsley();

 $('#Pform').on('submit', function(event){
  event.preventDefault();
  if($('#Pform').parsley().isValid()){


    var firstname = document.contactForm.firstname.value;
    var lastname = document.contactForm.lastname.value;
    var email = document.contactForm.email.value;
    var registeredmobile = document.contactForm.mobile.value;
    var marriedstatus = document.contactForm.status.value;
    var age = document.contactForm.age.value;
    var addr1 = document.contactForm.address1.value;
    var addr2 = document.contactForm.address2.value;
    var addr3 = document.contactForm.address3.value;
    var addr4 = document.contactForm.address4.value;
    var occupation = document.contactForm.occupation.value;



            dataObj={
        "registeredMobile":registeredmobile,
        "firstName": firstname,
        "lastName": lastname,
        "email": email,
        "marriedStatus": marriedstatus,
        "age": age,
        "addrLine1": addr1,
        "addrLine2": addr2,
        "addrLine3": addr3,
        "addrLine4": addr4,
        "occupation": occupation
        };


            console.log(dataObj)
    $.post(CONFIG['host']+"/clients/personal-profile", JSON.stringify(dataObj), function(res){
        data = res.data;
        console.log(res)
         alert("Details are saved Successfully");
         $('#submit').hide()
         $("input").prop('disabled', true)
         $("select").prop('disabled', true)
    });
};
});
})









