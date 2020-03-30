from metadata.functions.database import validateCookieDB, validateClientOTPByEmailDB
import logging


def validateCookieService(cookie):
    try:
        cookieStatus=validateCookieDB(cookie)
        
        if cookieStatus:
            return True
        else: 
            return False
    except Exception as e:
        logging.error("Error in validating Cookie Service "+str(e))
        raise    
    
def verifyOTPByEmailService(dataObj):
    try:
        clientList = validateClientOTPByEmailDB(dataObj)
        if len(clientList) != 0:
            return True
        else:
            return False
    except Exception as e:
        logging.error("Error in verifyting OTP by email" + str(e))

    