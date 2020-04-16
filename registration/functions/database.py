import logging
from registration.models import CustRegistration
from django.db.models import Q
import datetime

def saveClientPasswordDB(dataObj,custID):
    try:
        registrationObjs = []
        registrationObjs=CustRegistration.objects.filter(custid=custID)
    
        for record in registrationObjs:
            record.password = dataObj['password']
            record.updateddt=datetime.datetime.now()
            record.save()
        
    except Exception as e:
        logging.error("Error in saving client password DB" + str(e))
        raise


def validateClientMobileDB(custID, ip, device):
    try:
        
        registrationObjs = CustRegistration.objects.filter(~Q(password='None'),custid=custID,ipaddress=ip,device=device)

        return registrationObjs
    except Exception as msg:
        logging.error("Error in getting mobile number from DB: " + str(msg))
        raise


def saveClientMobileDB(dataObj, ip, device,custID):
    try:
        
        
        registration = CustRegistration(custid=custID,
                                        ipaddress=ip,
                                        device=device,
                                        password='None',
                                        createddt=datetime.datetime.now(),
                                        updateddt=datetime.datetime.now())
        registration.save()         
        
        clientPassword=CustRegistration.objects.filter(custid=custID)
        
        if clientPassword[0].password == 'None':
            pass
        elif clientPassword[0].password != 'None':
            clientRecords = CustRegistration.objects.filter(custid=custID,ipaddress=ip,device=device)        
            for record in clientRecords:
                record.password = clientPassword[0].password
                record.updateddt=datetime.datetime.now()
                record.save()
                            
    except Exception as e:
        logging.error("Error in saving client mobile number in DB " + str(e))
        raise

def validateClientPasswordDB(password,custID):
    try:
        
        registrationObjs=CustRegistration.objects.filter(custid=custID,password=password)
        
        
        return registrationObjs
    except Exception as e:
        logging.error("Error in validating client password DB "+str(e))
        raise 



def updateEmailOTPDB(otp,custId):
    try:
        
        registrationObjs=CustRegistration.objects.filter(custid=custId)
        for record in registrationObjs:
            record.eotp = otp
            record.updateddt=datetime.datetime.now()
            record.save()
        return registrationObjs
    except Exception as e:
        logging.error("Error in sending OTP by email  DB "+str(e))
        raise 

def validateClientOTPByEmailDB(otp,custID):
    try:
        registrationObjs=CustRegistration.objects.filter(eotp=otp,custid=custID)
            
        return registrationObjs
    except Exception as e:
        logging.error("Error in validating client password by email in DB "+str(e))
        raise 

def getCustRegistrationDB(custID):
    try:
        
        registrationObjs=CustRegistration.objects.filter(custid=custID)

        return registrationObjs[0]
    except Exception as e:
        logging.error("Error in retreving customer regsiration OBj DB "+str(e))
        raise 

