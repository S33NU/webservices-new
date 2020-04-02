import mysql.connector
import logging
from mysql.connector import errorcode
from metadata.functions.metadata import connectToDatabase
from registration.models import Registration
from django.db.models import Q

def saveClientPasswordDB(dataObj):
    try:
        registrationObjs = []
        registrationObjs=Registration.objects.filter(phonenumber=dataObj['userName'])
        
        if len(registrationObjs) == 0:
            registrationObjs=Registration.objects.filter(email=dataObj['userName'])
       
        for record in registrationObjs:
            record.password = dataObj['password']
            record.save()
        
    except Exception as e:
        logging.error("Error in saving client password " + str(e))
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



def validateClientEmailDB(dataObj, ip, device):
    try:

        registrationObjs = Registration.objects.filter(~Q(password='None'),email=dataObj['email'],ip_address=ip,device=device)

        return registrationObjs
    except Exception as msg:
        logging.error("Error in getting email from DB: " + str(msg))
        raise


def saveClientEmailDB(dataObj, ip, device, otp):
    try:
        registration = Registration(email=dataObj['email'],ip_address=ip,device=device,password='None',email_otp=otp)
        registration.save()        
        
        clientPassword=Registration.objects.filter(email=dataObj['email'])
        
        if clientPassword[0].password == 'None':
            pass
        elif clientPassword[0].password != 'None':
            clientRecords = Registration.objects.filter(email=dataObj['email'],ip_address=ip,device=device)        
            for record in clientRecords:
                record.password = clientPassword[0].password
                record.save()

    except Exception as e:
        logging.error("Error in saving client email in DB " + str(e))
        raise

def validateClientPasswordByEmailDB(dataObj):
    try:
       
        registrationObjs=Registration.objects.filter(email=dataObj['email'],password=dataObj['password'])

        return registrationObjs
    except Exception as e:
        logging.error("Error in validating client password by email in DB "+str(e))
        raise 

def checkClientPasswordByEmailDB(dataObj):
    try:
        
        registrationObjs=Registration.objects.filter(email=dataObj['email'])

        return registrationObjs
    except Exception as e:
        logging.error("Error in checking client password by email in DB "+str(e))
        raise 


