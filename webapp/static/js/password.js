(function(){
    console.log("jhdgsagd");
    $('#passwordReEntry').parsley().on('field:success', function() {
        passwordEntry = $('#passwordEntry').val()
        passwordReEntry = $('#passwordReEntry').val()
        
        if(passwordEntry != passwordReEntry){
            console.log("Passowrd does not match");
            $('.invalid-form-error-message')
            .html('Password mismatch')
            .toggleClass('filled', true);
        }else{
            $('.invalid-form-error-message')
            .html('')
            .toggleClass('filled', false);
        }
    });

})();

function savePassword(){
        passwordEntry = $('#passwordEntry').val()
        passwordReEntry = $('#passwordReEntry').val()
        
        if(passwordEntry == passwordReEntry){
            var userName=$("form.user").attr("id");
            dataObj={
                "userName": userName,
                "password": passwordEntry
            }
            $('.invalid-form-error-message')
            .html('')
            .toggleClass('filled', false);
        
            $.ajax({
                url: "http://localhost:8000/clients/registration/save-password",
                type: 'PUT',
                data:JSON.stringify(dataObj),
                dataType : "json",
                success: function(res) {
                    
                    data = res.data;
                    
                    if(res.statusCode == 0){
                        window.location.href = "../personal-profile";
                    } else {
                        console.log("Error in saving password");
                        if(res.statusCode == 1){
                            $('.invalid-form-error-message')
                            .html('Internal Server Error, try later')
                            .toggleClass('filled', true);
                        }else if(res.statusCode == 5){
                            window.location.href = "../login"
                        }
           
                    }           
                }
        
            });
        }else{
            console.log("Passowrd does not match");
            $('.invalid-form-error-message')
            .html('Password mismatch')
            .toggleClass('filled', true);
        }
}
