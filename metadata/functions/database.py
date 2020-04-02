from registration.models import Registration

def validateCookieDB(cookie):
    try:
        registrationObjs=Registration.objects.filter(phonenumber=cookie)

        if len(registrationObjs) == 0:
            registrationObjs=Registration.objects.filter(email=cookie)
            if len(registrationObjs) == 0:
                return False
            elif len(registrationObjs) != 0:
                return True
        elif len(registrationObjs) != 0:
            return True     
                            
        
    except Exception as e:
        logging.error("Error in validating Cookie DB "+str(e))
        raise    

def validateClientOTPByEmailDB(dataObj):
    try:
        registrationObjs=Registration.objects.filter(email_otp=dataObj['otp'],email=dataObj['email'])
            
        return registrationObjs
    except Exception as e:
        logging.error("Error in validating client password by email in DB "+str(e))
        raise 
