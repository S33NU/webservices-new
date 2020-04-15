import logging
from customer.functions.database import getCustomerDetailsDB,updateCustomerDetailsDB
import datetime
import pytz


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
        #print(customerObj)
        #print(datetime.datetime.now())
        #print(datetime.datetime.now()+datetime.timedelta(0,30))
        d=datetime.datetime.now()
        #print(d.year)
        e=datetime.datetime(d.year+1,d.month,d.day,23,59,59,999999)
        #print(e)
        subscriptionExpirationDate = datetime.datetime.now()+datetime.timedelta(0,600)
        
        if customerObj.customerStatus_new == 'R':
            dataObj ={
                'username':userName,
                'customerStatus':'S',
                'profileStatus':'document',
                'subscriptionType':subscriptionDetils['subscriptionType'],
                'amountPaid':subscriptionDetils['amountPaid'],
                'subscriptionExpirationDate':subscriptionExpirationDate
            }
            updateCustomerDetailsDB(dataObj)
        elif customerObj.customerStatus_new == 'E' and customerObj.customerStatus_old == 'S' :
            dataObj ={
                'username':userName,
                'customerStatus':'S',
                'subscriptionType':subscriptionDetils['subscriptionType'],
                'amountPaid':subscriptionDetils['amountPaid'],
                'subscriptionExpirationDate':subscriptionExpirationDate
                }
            updateCustomerDetailsDB(dataObj)
        elif customerObj.customerStatus_new == 'E' and customerObj.customerStatus_old == 'I' :
            dataObj ={
                'username':userName,
                'customerStatus':'I',
                'subscriptionType':subscriptionDetils['subscriptionType'],
                'amountPaid':subscriptionDetils['amountPaid'],
                'subscriptionExpirationDate':subscriptionExpirationDate
                }
            updateCustomerDetailsDB(dataObj)
            
    except Exception as e:
        logging.error("Error in saving subscription service"+str(e))
        raise




def reviewInvestmentService(userName):
    try:
        
        dataObj = {
                'username':userName,
                'customerStatus':'I',
                'profileStatus':'completed'
        }
        updateCustomerDetailsDB(dataObj)
            
    except Exception as e:
        logging.error("Error in review investment service "+str(e))
        raise
    
def saveDocumentsService(userName):
    try:
        customerObj = getCustomerDetailsDB(userName)
        customerObj = customerObj[0]
        
        dataObj ={
                'username':userName,
                'customerStatus':customerObj.profileStatus,
                'profileStatus':'document'
        }
        updateCustomerDetailsDB(dataObj)
            
    except Exception as e:
        logging.error("Error in save documents service "+str(e))
        raise    
    