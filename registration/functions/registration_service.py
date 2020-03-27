from registration.functions.database import saveClientPasswordDB,validateClientPasswordDB, saveClientMobileDB, validateClientMobileDB
import logging
from metadata.functions.metadata import getOTP,verifyOTP


def saveClientPasswordService(dataObj):
    try:
        saveClientPasswordDB(dataObj)
    except Exception as e:
        logging.error("Error in saving client password "+str(e))
        raise

def validateMobileandSaveService(dataObj, ip, device):
    try:
        clientDetails = validateClientMobileDB(dataObj, ip, device)
        if clientDetails == []:
            return True
        else:
            pass
    except Exception as msg:
        logging.error('Error in validating mobile service' + str(msg)) 
        
        
def saveClientMobileService(dataObj, ip, device):
    try:
        saveClientMobileDB(dataObj, ip, device)
    except Exception as e:
        logging.error("Error in saving Client Mobile number" + str(e))
        raise

def validateClientPasswordService(dataObj):
    try:
        getOTP(str(919160384325))
        clientList=validateClientPasswordDB(dataObj)
        if len(clientList) == 1:
            return True
        else:
            return False
    except Exception  as e:
        logging.error("Error in validating client credentials")
        raise    

def verifyOTPService(dataObj):
    try:
        response=verifyOTP(str(dataObj['phoneNumber']),str(dataObj['otp']))
        if response.type == 'success':
            return True
        else:
            return False
        
    except Exception as e:
        logging.error("Error in validating OTP "+str(e))
        raise
