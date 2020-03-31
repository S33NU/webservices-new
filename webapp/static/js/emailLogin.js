(function() {
    $("#existingUserLogin").hide();
    $("#newUserLogin").hide();
    $("#loginSubmit").hide();
    $('#userEmailID').parsley().on('field:success', function() {
        var email = $('#userEmailID').val();
        dataObj={
            "email": email
        }
       
        $.post("http://localhost:8000/clients/registration/validate-email", JSON.stringify(dataObj), function(res){
            data = res.data;
            console.log(res);
            $("#loginSubmit").show();
            if(res.statusCode == 0){
                $('.invalid-form-error-message')
                    .html('')
                    .toggleClass('filled', false);


                if(data){
                    console.log("old");
                    $("#newUserLogin").hide();
                    $("#otpMessage").hide();
                    $("#existingUserLogin").show();  
                }else{
                    console.log("new");
                    $("#otpMessage").show();
                    $("#otpMessage").html("OTP sent to "+email);
                    $("#newUserLogin").show();
                    $("#existingUserLogin").hide();  
                }
            }else if(res.statusCode == 1){
            console.log(res);
                $('.invalid-form-error-message')
                    .html('Internal Server Error, try later')
                    .toggleClass('filled', true);
                
            }
        });
    });

    $('#userEmailID').parsley().on('field:error', function() {
        $("#existingUserLogin").hide();
        $("#newUserLogin").hide();
        $("#loginSubmit").hide();
        $("#otpMessage").hide();
        $('.invalid-form-error-message')
        .html('')
        .toggleClass('filled', false);
    });


})();

function verifyUserCredentials(){
    
    email =  $('#userEmailID').val()
    otp=$("#userOTP").val();
    password = $("#userPassword").val();

    
    if(otp != "" && password == ""){
        dataObj={
            "email":email,
            "otp":otp
        }
        
        $.post("http://localhost:8000/clients/registration/verifyOTP-email", JSON.stringify(dataObj), function(res){
            data = res.data;
            statusCode = res.statusCode;
            if(statusCode==0){
                $('.invalid-form-error-message')
                    .html('')
                    .toggleClass('filled', false);
                $("#otpMessage").html("");
                checkPassword(email);
            }else{
                  
                console.log("Invalid OTP");
                if(statusCode == 3){
                    $('.invalid-form-error-message')
                    .html('Invalid OTP')
                    .toggleClass('filled', true);
                }else if (statusCode == 1){
                    $('.invalid-form-error-message')
                    .html('Internal Server Error, try later')
                    .toggleClass('filled', true);
                }
            }
        });

   
    }else if(password != "" && otp == ""){
        dataObj={
            "email":email,
            "password":password
        }
        
        $.post("http://localhost:8000/clients/registration/validate-password-email", JSON.stringify(dataObj), function(res){
            data = res.data;
            statusCode = res.statusCode;
            if(statusCode==0){
                
                $('.invalid-form-error-message')
                    .html('')
                    .toggleClass('filled', false);
                
                var dateVar = new Date();
                dateVar.setTime(dateVar.getTime() + (1*24*60*60*1000));
                var expires = "expires="+ dateVar.toUTCString();
                document.cookie="userName="+email+";"+expires+";path=/";
                window.location.href = "personal-profile"
            }else{
                console.log("Error in validation")
                if(statusCode == 2){
                    $('.invalid-form-error-message')
                    .html('Invalid Credentials')
                    .toggleClass('filled', true);
                }else if (statusCode == 1){
                    $('.invalid-form-error-message')
                    .html('Internal Server Error, try later')
                    .toggleClass('filled', true);
                }
            }
            
        });


    }
}

function checkPassword(email){
    
    dataObj = {
        "email":email
    }

    $.post("http://localhost:8000/clients/registration/check-password-email", JSON.stringify(dataObj), function(res){
            data = res.data;
            var dateVar = new Date();
            dateVar.setTime(dateVar.getTime() + (1*24*60*60*1000));
            var expires = "expires="+ dateVar.toUTCString();
            document.cookie="userName="+email+";"+expires+";path=/";
                
            if(data){
                console.log("alredy registered");
                window.location.href = "personal-profile";     
            }else{
                console.log("new user");
                window.location.href = "save-password/"+email;
            }
    });
    

}