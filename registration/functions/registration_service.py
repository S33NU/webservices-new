from registration.functions.database import saveClientPasswordDB,validateClientPasswordDB,saveClientMobileDB, validateClientMobileDB
from registration.functions.database import updateEmailOTPDB, validateClientOTPByEmailDB
import logging
from metadata.functions.metadata import getOTP,verifyOTP,getOTPByEmail, getConfig,generateOTP,reSendOTP
import json

from customer.functions.database import saveCustomerDetailsDB,getTasksByCustIdDB,updateCustomerEmailDB,updateCustomerDetailsDB,getCustomerDetailsDB,updateCustTaskStatusDB
def saveClientPasswordService(dataObj,userName):
    try:
        customerDetailsobjs=getCustomerDetailsDB(userName)
        saveClientPasswordDB(dataObj,customerDetailsobjs[0].id)
        custObj={
            'custregmobile':userName,
            'customerStatus':'R'
        }
        custTasksObjs = getTasksByCustIdDB(customerDetailsobjs[0].id)
        if len(custTasksObjs) != 3: 
            profileTaskStatusList = []
            obj = {
                'custid':customerDetailsobjs[0].id,
                'taskname':'Personal',
                'status':'P',
                'tasktype':'P'
            }
            profileTaskStatusList.append(obj)
            obj = {
                'custid':customerDetailsobjs[0].id,
                'taskname':'Investment',
                'status':'P',
                'tasktype':'P'
            }
            profileTaskStatusList.append(obj)
            obj = {
                'custid':customerDetailsobjs[0].id,
                'taskname':'document',
                'status':'P',
                'tasktype':'D'
            }
            profileTaskStatusList.append(obj)
            updateCustTaskStatusDB(profileTaskStatusList)
        updateCustomerDetailsDB(custObj)
        
    except Exception as e:
        logging.error("Error in saving client password service "+str(e))
        raise

def sendOTPByEmailService(dataObj):
    try:
        otp=generateOTP()
        getOTPByEmail(dataObj['email'],otp)
        customerDetailsobjs=getCustomerDetailsDB(dataObj['custregmobile'])
        updateEmailOTPDB(otp,customerDetailsobjs[0].id)
        updateCustomerEmailDB(dataObj['email'],dataObj['custregmobile'])    
    except Exception as e:
        logging.error("Error in sending OTP by email service "+str(e))
        raise
def resendOTPService(dataObj):
    try:
        if dataObj['otpType'] == 'mobile':
            reSendOTP(dataObj['custcountrycode']+dataObj['custregmobile'])
        elif dataObj['otpType'] == 'email':
            otp=generateOTP()
            getOTPByEmail(dataObj['email'],otp)
            customerDetailsobjs=getCustomerDetailsDB(dataObj['custregmobile'])                
            updateEmailOTPDB(otp,customerDetailsobjs[0].id)
    except Exception as e:
        logging.error("Error in resending OTP service "+str(e))
        raise
         
def saveClientMobileService(dataObj, ip, device,custID):
    try:
        saveClientMobileDB(dataObj, ip, device, custID)
    except Exception as e:
        logging.error("Error in saving Client Mobile number service " + str(e))
        raise
     
def validateMobileandSaveService(dataObj, ip, device):
    try:
        customerDetailsobjs=getCustomerDetailsDB(dataObj['custregmobile'])
        if len(customerDetailsobjs) != 0:
            clientDetails = validateClientMobileDB(customerDetailsobjs[0].id, ip, device)
            if len(clientDetails) == 0:
                getOTP(dataObj['custcountrycode']+dataObj['custregmobile'])
                saveCustomerDetailsDB({'custregmobile':dataObj['custregmobile'],'custstatus':'P','custstatusold':'P','custcountrycode':dataObj['custcountrycode']})
                customerDetailsobjs = getCustomerDetailsDB(dataObj['custregmobile'])
                saveClientMobileService(dataObj, ip, device, customerDetailsobjs[0].id)
                return True
            else:
                return False
        else:
            getOTP(dataObj['custcountrycode']+dataObj['custregmobile'])
            saveCustomerDetailsDB({'custregmobile':dataObj['custregmobile'],'custstatus':'P','custstatusold':'P','custcountrycode':dataObj['custcountrycode']})
            customerDetailsobjs = getCustomerDetailsDB(dataObj['custregmobile'])
            saveClientMobileService(dataObj, ip, device, customerDetailsobjs[0].id)
            return True
    except Exception as msg:
        logging.error('Error in validating mobile service ' + str(msg))
        raise
        
def validateClientPasswordService(dataObj):
    try:
        customerDetailsobjs=getCustomerDetailsDB(dataObj['custregmobile'])
        
        clientList=validateClientPasswordDB(dataObj['password'],customerDetailsobjs[0].id)
        if len(clientList) != 0:
            return True
        else:
            return False
    except Exception  as e:
        logging.error("Error in validating client credentials service "+str(e))
        raise    

def verifyOTPService(dataObj):
    try:
        
        response=verifyOTP(dataObj['custcountrycode']+dataObj['custregmobile'],dataObj['otp'])
        
        response = json.loads(response)
        if response["type"] == "success":
            return True
        else:
            return False
        
    except Exception as e:
        logging.error("Error in validating OTP service "+str(e))
        raise

def verifyOTPByEmailService(dataObj):
    try:
        customerDetailsobjs=getCustomerDetailsDB(dataObj['custregmobile'])
        
        clientList = validateClientOTPByEmailDB(dataObj['otp'],customerDetailsobjs[0].id)
        if len(clientList) != 0:
            return True
        else:
            return False
    except Exception as e:
        logging.error("Error in verifyting OTP by email" + str(e))
        raise
     

       
    
    
    
    
    