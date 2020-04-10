from registration.functions.database import saveClientPasswordDB,checkClientPasswordDB,validateClientPasswordDB,saveClientMobileDB, validateClientMobileDB
from registration.functions.database import updateEmailOTPDB,getRegistrationDetailsDB
import logging
from metadata.functions.metadata import getOTP,verifyOTP,getOTPByEmail, getConfig,generateOTP,reSendOTP
import json

from customer.functions.database import saveCustomerDetailsDB,updateCustomerDetailsDB
def saveClientPasswordService(dataObj,userName):
    try:
        
        saveClientPasswordDB(dataObj,userName)
        custObj={
            'username':userName,
            'customerStatus':'R',
            'profileStatus':'personal,invest,'
        }
        
        updateCustomerDetailsDB(custObj)
        
    except Exception as e:
        logging.error("Error in saving client password service "+str(e))
        raise

def sendOTPByEmailService(dataObj):
    try:
        otp=generateOTP()
        getOTPByEmail(str(dataObj['email']),otp)
        updateEmailOTPDB(otp,dataObj['phonenumber'],dataObj['email'])
        
    except Exception as e:
        logging.error("Error in sending OTP by email service "+str(e))
        raise
def resendOTPService(dataObj):
    try:
        if dataObj['otpType'] == 'mobile':
            reSendOTP("91"+str(dataObj['phonenumber']))
        elif dataObj['otpType'] == 'email':
            otp=generateOTP()
            getOTPByEmail(str(dataObj['email']),otp)                
            updateEmailOTPDB(otp,dataObj['phonenumber'],dataObj['email'])
    except Exception as e:
        logging.error("Error in resending OTP service "+str(e))
        raise
         
def saveClientMobileService(dataObj, ip, device):
    try:
        saveClientMobileDB(dataObj, ip, device)
    except Exception as e:
        logging.error("Error in saving Client Mobile number service " + str(e))
        raise
     
def validateMobileandSaveService(dataObj, ip, device):
    try:
        clientDetails = validateClientMobileDB(dataObj, ip, device)
        if len(clientDetails) == 0:
            getOTP("91"+str(dataObj['phonenumber']))
            saveClientMobileService(dataObj, ip, device)
            saveCustomerDetailsDB({'userName':dataObj['phonenumber'],'customerStatus_new':'P','customerStatus_old':'P'})
            
            return True
        else:
            return False
    except Exception as msg:
        logging.error('Error in validating mobile service ' + str(msg))
        raise
        
def validateClientPasswordService(dataObj):
    try:
        
        clientList=validateClientPasswordDB(dataObj)
        if len(clientList) != 0:
            return True
        else:
            return False
    except Exception  as e:
        logging.error("Error in validating client credentials service "+str(e))
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
        logging.error("Error in validating OTP service "+str(e))
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
    
def getRegistrationDetailsService(userName):
    try:
        registrationDetailsObj = getRegistrationDetailsDB(userName)
        
        dataObj = {
            'phonenumber':registrationDetailsObj.phonenumber,
            'email':registrationDetailsObj.email  
        }
        
        return dataObj
    except Exception as e:
        logging.error("Error in  retreiving registration details  service "+str(e))
        raise
     

       
    
    
    
    
    