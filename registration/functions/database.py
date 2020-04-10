import logging
from registration.models import Registration
from django.db.models import Q

def saveClientPasswordDB(dataObj,userName):
    try:
        registrationObjs = []
        registrationObjs=Registration.objects.filter(phonenumber=userName)
    
        for record in registrationObjs:
            record.password = dataObj['password']
            record.save()
        
    except Exception as e:
        logging.error("Error in saving client password DB" + str(e))
        raise


def validateClientMobileDB(dataObj, ip, device):
    try:
        
        registrationObjs = Registration.objects.filter(~Q(password='None'),phonenumber=dataObj['phonenumber'],ip_address=ip,device=device)

        return registrationObjs
    except Exception as msg:
        logging.error("Error in getting mobile number from DB: " + str(msg))
        raise


def saveClientMobileDB(dataObj, ip, device):
    try:
        registration = Registration(phonenumber=dataObj['phonenumber'],ip_address=ip,device=device,password='None')
        registration.save()        
        
        clientPassword=Registration.objects.filter(phonenumber=dataObj['phonenumber'])
        
        if clientPassword[0].password == 'None':
            pass
        elif clientPassword[0].password != 'None':
            clientRecords = Registration.objects.filter(phonenumber=dataObj['phonenumber'],ip_address=ip,device=device)        
            for record in clientRecords:
                record.password = clientPassword[0].password
                record.save()
                            
    except Exception as e:
        logging.error("Error in saving client mobile number in DB " + str(e))
        raise

def validateClientPasswordDB(dataObj):
    try:
        
        registrationObjs=Registration.objects.filter(phonenumber=dataObj['phonenumber'],password=dataObj['password'])
        
        
        return registrationObjs
    except Exception as e:
        logging.error("Error in validating client password DB "+str(e))
        raise 

def checkClientPasswordDB(dataObj):
    try:
        
        registrationObjs=Registration.objects.filter(phonenumber=dataObj['phonenumber'])
        
        return registrationObjs
    except Exception as e:
        logging.error("Error in checking client password DB "+str(e))
        raise 


def updateEmailOTPDB(otp,phonenumber,email):
    try:
        
        registrationObjs=Registration.objects.filter(phonenumber=phonenumber)
        for record in registrationObjs:
            record.email = email
            record.email_otp = otp
            record.save()
        return registrationObjs
    except Exception as e:
        logging.error("Error in sending OTP by email  DB "+str(e))
        raise 

def getRegistrationDetailsDB(userName):
    try:
        
        registrationObjs=Registration.objects.filter(phonenumber=userName)
        if len(registrationObjs) > 0:
            registrationObjs = registrationObjs[0]
        return registrationObjs
    except Exception as e:
        logging.error("Error in retreiving registration details DB "+str(e))
        raise 

