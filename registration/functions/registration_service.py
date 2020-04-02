from registration.functions.database import saveClientPasswordDB,checkClientPasswordDB,validateClientPasswordDB,saveClientMobileDB, validateClientMobileDB
from registration.functions.database import checkClientPasswordByEmailDB, saveClientEmailDB,validateClientEmailDB, validateClientPasswordByEmailDB
import logging
from metadata.functions.metadata import getOTP,verifyOTP,getOTPByEmail, getConfig
import json

from random import randint

def saveClientPasswordService(dataObj):
    try:
        saveClientPasswordDB(dataObj)
    except Exception as e:
        logging.error("Error in saving client password "+str(e))
        raise

def saveClientMobileService(dataObj, ip, device):
    try:
        saveClientMobileDB(dataObj, ip, device)
    except Exception as e:
        logging.error("Error in saving Client Mobile number" + str(e))
        raise
     
def validateMobileandSaveService(dataObj, ip, device):
    try:
        clientDetails = validateClientMobileDB(dataObj, ip, device)
        if len(clientDetails) == 0:
            getOTP("91"+str(dataObj['phonenumber']))
            saveClientMobileService(dataObj, ip, device)
            return True
        else:
            return False
    except Exception as msg:
        logging.error('Error in validating mobile service' + str(msg))
        raise
        
def validateClientPasswordService(dataObj):
    try:
        
        clientList=validateClientPasswordDB(dataObj)
        if len(clientList) != 0:
            return True
        else:
            return False
    except Exception  as e:
        logging.error("Error in validating client credentials")
        raise    

def verifyOTPService(dataObj):
    try:
        
        response=verifyOTP(dataObj['phonenumber'],dataObj['otp'])
        
        response = json.loads(response)
        if response["type"] == "success":
            return True
        else:
            return False
        
    except Exception as e:
        logging.error("Error in validating OTP "+str(e))
        raise

def checkClientPasswordService(dataObj):
    try:
        clientPasswordList = checkClientPasswordDB(dataObj)
        if clientPasswordList[0].password != 'None':
            return True
        elif clientPasswordList[0].password == 'None':
            return False
    except Exception as e:
        logging.error("Error in checking client password service "+str(e))
        raise
    
    
def saveClientEmailService(dataObj, ip, device, otp):
    try:
        saveClientEmailDB(dataObj, ip, device, otp)
    except Exception as e:
        logging.error("Error in saving Client email service " + str(e))
        raise
     
def validateEmailandSaveService(dataObj, ip, device):
    try:
        clientDetails = validateClientEmailDB(dataObj, ip, device)
        if len(clientDetails) == 0:
            config = getConfig()
            email_otp_config = config['EMAIL_OTP_CONFIG']
            n = email_otp_config.getint('otp_length')
            range_start = 10**(n-1)
            range_end = (10**n)-1
            otp=randint(range_start, range_end)
            getOTPByEmail(str(dataObj['email']),otp)
            saveClientEmailService(dataObj, ip, device, str(otp))
            return True
        else:
            return False
    except Exception as msg:
        logging.error('Error in validating email service' + str(msg))
        raise
        
def validateClientPasswordByEmailService(dataObj):
    try:
        
        clientList=validateClientPasswordByEmailDB(dataObj)
        if len(clientList) != 0:
            return True
        else:
            return False
    except Exception  as e:
        logging.error("Error in validating client credentials by email")
        raise    

        
    except Exception as e:
        logging.error("Error in validating OTP by email service"+str(e))
        raise

def checkClientPasswordByEmailService(dataObj):
    try:
        clientPasswordList = checkClientPasswordByEmailDB(dataObj)
        
        if clientPasswordList[0].password != 'None':
            return True
        elif clientPasswordList[0].password == 'None':
            return False
    except Exception as e:
        logging.error("Error in checking client password by email service "+str(e))
        raise    
    
    
    
    
    