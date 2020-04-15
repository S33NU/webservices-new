
(function() {
    $("#existingUserLogin").hide();
    $("#newUserLogin").hide();
    $("#loginSubmit").hide();
    $("#otpMessage").hide();
    $('#userMobileNumber').parsley().on('field:success', function() {
        var phonenumber =  $('#userMobileNumber').val();
        dataObj={
            "custregmobile":phonenumber,
            "custcountrycode":"91"
        }
       
        $.post(CONFIG['host']+"/clients/registration/validate-phoneno", JSON.stringify(dataObj), function(res){
            data = res.data;
            $("#loginSubmit").show();
            if(res.statusCode == 0){
                $('.invalid-form-error-message')
                    .html('')
                    .toggleClass('filled', false);
                
                if(data){
                    console.log("old");
                    $("#mobileotpMessage").hide();
                    $("#newUserLogin").hide();
                    $("#existingUserLogin").show();
                }else{
                    console.log("new");
                    $("#newUserLogin").show();
                    $("#mobileotpMessage").show();
                    $("#mobileotpMessage").html("OTP sent to mobile");
                    $("#existingUserLogin").hide();  
                }
            }else if(res.statusCode == 1){
               
                $('.invalid-form-error-message')
                    .html('Internal Server Error, try later')
                    .toggleClass('filled', true);
                
            }
        });
    });

    $('#userMobileNumber').parsley().on('field:error', function() {
        $("#existingUserLogin").hide();
        $("#newUserLogin").hide();
        $("#otpMessage").hide();
        $("#loginSubmit").hide();
        $("#userOTP").val('');
        $("#userPassword").val('');
        $("#userMobileNumber").val('');
        $('#mobile').prop('checked', true);
        $('.invalid-form-error-message')
        .html('')
        .toggleClass('filled', false);
    });

    $('input[type=radio][name=otpType]').change(function() {
        if (this.value == 'email') {
            $("#mobileotpMessage").hide();
            $('#userEmailID').prop('required',true);
            registerEmailValidation()
            $("#userEmailID").parsley().validate();
        }
        else if (this.value == 'mobile') {
            $("#emailotpMessage").hide();
            $('#userEmailID').prop('required',false);
            $("#userMobileNumber").parsley().validate();
        }
    }); 
})();





function verifyUserCredentials(){
    
    var phonenumber =  $('#userMobileNumber').val()
    var otp=$("#userOTP").val();
    var password = $("#userPassword").val();
    var email =  $('#userEmailID').val();
    
    if(otp != "" && password == ""){
        
        var otpType=$("input[name='otpType']:checked").val();
        if (otpType == 'mobile'){
            dataObj={
                "custregmobile":phonenumber,
                "custcountrycode":"91",
                "otp":otp
            };
            verifyOTPByMobile(dataObj,phonenumber);

        }else if (otpType == 'email'){
            dataObj={
                "custregmobile":phonenumber,
                "otp":otp
            };
            
            verifyOTPByEmail(dataObj,phonenumber);
        }
    }else if(password != "" && otp == ""){
        dataObj={
            "custregmobile":phonenumber,
            "password":password
        }
        
        validatePassword(dataObj,phonenumber);


    }
}

function validatePassword(dataObj,phonenumber){
    $.post(CONFIG['host']+"/clients/registration/validate-password", JSON.stringify(dataObj), function(res){
        data = res.data;
        statusCode = res.statusCode;
        if(statusCode==0){
            
            $('.invalid-form-error-message')
                .html('')
                .toggleClass('filled', false);
            
            var dateVar = new Date();
            //dateVar.setTime(dateVar.getTime() + (1*24*60*60*1000));
            dateVar.setTime(dateVar.getTime() + (300*1000));
            
            var expires = "expires="+ dateVar.toUTCString();
            document.cookie="userName="+phonenumber+";"+expires+";path=/";
            window.location.href = "home/default"
        }else{
            console.log("Error in validation");
            
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

function verifyOTPByMobile(dataObj,phonenumber){
    $.post(CONFIG['host']+"/clients/registration/verifyOTP", JSON.stringify(dataObj), function(res){
        data = res.data;
        statusCode = res.statusCode;
        if(statusCode==0){
            $('.invalid-form-error-message')
                .html('')
                .toggleClass('filled', false);
            $("#mobileotpMessage").hide();
            var dateVar = new Date();
            //dateVar.setTime(dateVar.getTime() + (1*24*60*60*1000));
            dateVar.setTime(dateVar.getTime() + (300*1000));
            var expires = "expires="+ dateVar.toUTCString();
            document.cookie="userName="+phonenumber+";"+expires+";path=/";
            window.location.href = "home/default";
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

}




function verifyOTPByEmail(dataObj,phonenumber){
    $.post(CONFIG['host']+"/clients/registration/verifyOTP-email", JSON.stringify(dataObj), function(res){
        data = res.data;
        statusCode = res.statusCode;
        if(statusCode==0){
            $('.invalid-form-error-message')
                .html('')
                .toggleClass('filled', false);
            $("#emailotpMessage").hide();
            var dateVar = new Date();
            //dateVar.setTime(dateVar.getTime() + (1*24*60*60*1000));
            dateVar.setTime(dateVar.getTime() + (300*1000));
            var expires = "expires="+ dateVar.toUTCString();
            document.cookie="userName="+phonenumber+";"+expires+";path=/";
            window.location.href = "home/default";
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

}

function resendOTP(){
    console.log("resend OTP");
    var phonenumber =  $('#userMobileNumber').val()
    var otpType=$("input[name='otpType']:checked").val();
    var email =  $('#userEmailID').val();

    dataObj ={
        'otpType':otpType,
        'custregmobile':phonenumber,
        'email':email
    };
    $("#mobileotpMessage").hide();
    $("#emailotpMessage").hide();
    $.post(CONFIG['host']+"/clients/registration/resend-otp", JSON.stringify(dataObj), function(res){
        data = res.data;

        if(res.statusCode == 0){
            $('.invalid-form-error-message')
                .html('')
                .toggleClass('filled', false);
                if (otpType == 'mobile'){
                    $("#mobileotpMessage").show();
                }else if (otpType == 'email'){
                    $("#emailotpMessage").show();
                }    
            
        }else if(res.statusCode == 1){

            $('.invalid-form-error-message')
                .html('Internal Server Error, try later')
                .toggleClass('filled', true);
            
        }
    });

}

function registerEmailValidation(){
    console.log("email Validation")
    $('#userEmailID').parsley().on('field:success', function() {
        var email = $('#userEmailID').val();
        var phonenumber =  $('#userMobileNumber').val()
        dataObj={
            "email": email,
            "custregmobile":phonenumber
        }
       
        $.post(CONFIG['host']+"/clients/registration/send-otp-email", JSON.stringify(dataObj), function(res){
            data = res.data;

            if(res.statusCode == 0){
                $('.invalid-form-error-message')
                    .html('')
                    .toggleClass('filled', false);
                $("#emailotpMessage").html("OTP sent to email");
                $("#emailotpMessage").show();

            }else if(res.statusCode == 1){

                $('.invalid-form-error-message')
                    .html('Internal Server Error, try later')
                    .toggleClass('filled', true);
                
            }
        });
    
    });
}
