import logging
from customer.functions.database import getCustomerDetailsDB,updateCustomerDetailsDB, updateTaskByCustIdAndNameDB
from subscriptions.functions.database import saveSubscriptionDetailsDB,savePaymentDetailsDB,getCustSubscriptionByServIDAndCustIdDB
from subscriptions.functions.database import getCustPaymentByIDs, updateCustSubscriptionPaymentID, updateCustSubscriptionStatus
import datetime
import pytz
from metadata.functions.database import getLookUpValue, getLookUpID


def getSubscriptionsService():
    try:
       #subscriptionsList = getSubscriptionsListDB()
       temp=[]
       for subscription in subscriptionsList:
           subscriptionObj={
               'subscriptionKey':subscription.subscriptionKey,
               'subscriptionName':subscription.subscriptionName,
               'subscriptionDescription':subscription.subscriptionDescription,
               'subscriptionCost':subscription.subscriptionCost,
               'subscriptionPeriod':subscription.subscriptionPeriod
           }
           temp.append(subscriptionObj) 
       subscriptionsList = temp    
       return subscriptionsList
    except Exception as e:
        logging.error("Error in retrieving subscription list "+str(e))
        raise
   
def saveSubscriptionService(subscriptionDetils,userName):
    try:
        
        customerObj = getCustomerDetailsDB(userName)
        customerObj = customerObj[0]
        
        servsigneddt=datetime.datetime.now()
        lookupObj = getLookUpID('Service')
        
        if len(lookupObj) == 1:
            lookupObj = lookupObj[0]
            
      
        for servid in subscriptionDetils['servidList']:
            lookUpValueObj = getLookUpValue(lookupObj.lookupid,servid)
            if len(lookUpValueObj) == 1:
                lookUpValueObj = lookUpValueObj[0]
            servexpdt= servsigneddt+datetime.timedelta(int(lookUpValueObj.lookupparam1))
            print(servexpdt)
            servexpdt = servsigneddt + datetime.timedelta(0,600)
            obj = {
                'custid':customerObj.id,
                'servid':servid,
                'servsigneddt':servsigneddt,
                'servexpdt':servexpdt,
                'servstatus':'A'    
            }
            saveSubscriptionDetailsDB(obj)
        
            
            custSubscriptionObj = getCustSubscriptionByServIDAndCustIdDB(customerObj.id,servid,'A')
            
            if len(custSubscriptionObj) == 1:
                custSubscriptionObj = custSubscriptionObj[0]
            
            obj = {
                'custid':customerObj.id,
                'servid':servid,
                'custsubid':custSubscriptionObj.id,
                'paymentmod':subscriptionDetils['paymentmod'],
                'paygateway':subscriptionDetils['paygateway'],
                'payamount':subscriptionDetils['payamount'],
                'payreference': subscriptionDetils['payreference']
            }
            
            savePaymentDetailsDB(obj)
        
            custPaymentObj = getCustPaymentByIDs(customerObj.id,servid,custSubscriptionObj.id)
            if len(custPaymentObj) == 1:
                custPaymentObj = custPaymentObj[0]
            
            updateCustSubscriptionPaymentID(custSubscriptionObj.id,custPaymentObj.id)
        
        
        if customerObj.custstatus == 'R' and customerObj.custstatusold == 'P':
            dataObj ={
                'custregmobile':userName,
                'customerStatus':'S',
            }
            updateCustomerDetailsDB(dataObj)
        elif customerObj.custstatus == 'E' and customerObj.custstatusold == 'S' :
            dataObj ={
                'custregmobile':userName,
                'customerStatus':'S',
                }
            updateCustomerDetailsDB(dataObj)
        elif customerObj.custstatus == 'E' and customerObj.custstatusold == 'I' :
            dataObj ={
                'custregmobile':userName,
                'customerStatus':'I',
                }
            updateCustomerDetailsDB(dataObj)
            
    except Exception as e:
        logging.error("Error in saving subscription service"+str(e))
        raise


def checkSubscriptionExpirationService(userName):
    try:
        customerObj = getCustomerDetailsDB(userName)
        customerObj = customerObj[0]
        
        lookupObj = getLookUpID('Service')
        
        if len(lookupObj) == 1:
            lookupObj = lookupObj[0]
            
        custSubscriptionObjs = getCustSubscriptionByCustIDAndStatus(customerObj.id,'A')
        
        for custSubscriptionObj in custSubscriptionObjs:
            
            lookUpValueObj = getLookUpValue(lookupObj.lookupid,custSubscriptionObj.servid)
            if len(lookUpValueObj) == 1:
                lookUpValueObj = lookUpValueObj[0]
            
            if lookUpValueObj.lookupparam1 != '1':
                utc=pytz.UTC
                signdt = custSubscriptionObj.servsigneddt.replace(tzinfo=utc)
                expirationDt = custSubscriptionObj.servexpdt.replace(tzinfo=utc)   
                if signdt<expirationDt:
                    return True
                else:
                    updateCustSubscriptionStatus(customerObj.id,'E') 
                    return False  
    except Exception as e:
        logging.error("Error in saving subscription"+str(e))
        raise




def reviewInvestmentService(userName):
    try:
        
        dataObj = {
                'custregmobile':userName,
                'customerStatus':'I',
        }
        updateCustomerDetailsDB(dataObj)
            
    except Exception as e:
        logging.error("Error in review investment service "+str(e))
        raise
    
def saveDocumentsService(userName):
    try:
        customerObj = getCustomerDetailsDB(userName)
        customerObj = customerObj[0]
        
        updateTaskByCustIdAndNameDB(customerObj.id,'Document','C')
            
    except Exception as e:
        logging.error("Error in save documents service "+str(e))
        raise    
    