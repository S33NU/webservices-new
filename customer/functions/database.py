import logging
from customer.models import Customer,CustTask
import datetime

def getCustomerDetailsDB(custregmobile):
    try:
       
        customerDetailsObj=Customer.objects.filter(custregmobile=custregmobile)
        
        return customerDetailsObj
    except Exception as e:
        logging.error("Error in retrieving customer details DB " + str(e))
        raise
    
def saveCustomerDetailsDB(dataObj):
    try:
        
        customerDetailsobjs=getCustomerDetailsDB(dataObj['custregmobile'])
        
        if len(customerDetailsobjs) == 0:
            
            customerDetailsobj=Customer(custregmobile=dataObj['custregmobile'],
                                           custstatusold=dataObj['custstatusold'],
                                           custstatus=dataObj['custstatus'],
                                           custcountrycode=dataObj['custcountrycode'],
                                           createddt=datetime.datetime.now(),
                                           updateddt=datetime.datetime.now())
                                           
            customerDetailsobj.save()
            
    except Exception as e:
        logging.error("Error in saving customer details DB " + str(e))
        raise    

def updateCustomerEmailDB(custemail,custregmobile):
    try:
        
        customerDetailsobjs=getCustomerDetailsDB(custregmobile)
        
        if len(customerDetailsobjs) != 0:
            customerDetailsobjs[0].custemail = custemail 
            customerDetailsobjs[0].updateddt=datetime.datetime.now()
            customerDetailsobjs[0].save()
            
    except Exception as e:
        logging.error("Error in updating customer email DB " + str(e))
        raise    


    
def updateCustomerDetailsDB(dataObj):
    try:
        customerDetailsobj=Customer.objects.filter(custregmobile=dataObj['custregmobile'])
        if len(customerDetailsobj) == 1:
            customerDetailsobj=customerDetailsobj[0]
        if customerDetailsobj.custstatus == 'P' and customerDetailsobj.custstatusold == 'P':
            customerDetailsobj.custstatusold = customerDetailsobj.custstatus
            customerDetailsobj.custstatus=dataObj['customerStatus']
        elif customerDetailsobj.custstatus == 'R' and customerDetailsobj.custstatusold == 'P' and dataObj['customerStatus'] == 'S':
            customerDetailsobj.custstatusold = customerDetailsobj.custstatus
            customerDetailsobj.custstatus=dataObj['customerStatus']
            customerDetailsobj.subscriptionType=dataObj['subscriptionType']
            customerDetailsobj.subscriptionExpirationDate = dataObj['subscriptionExpirationDate']
            customerDetailsobj.amountPaid = dataObj['amountPaid']
        elif customerDetailsobj.custstatus == 'E' and customerDetailsobj.custstatusold == 'S' and dataObj['customerStatus'] == 'S':
            customerDetailsobj.custstatusold = customerDetailsobj.custstatus
            customerDetailsobj.custstatus=dataObj['customerStatus']
            customerDetailsobj.subscriptionType=dataObj['subscriptionType']
            customerDetailsobj.subscriptionExpirationDate = dataObj['subscriptionExpirationDate']
            customerDetailsobj.amountPaid = dataObj['amountPaid']    
        elif customerDetailsobj.custstatus == 'S' and dataObj['customerStatus'] == 'E':
            customerDetailsobj.custstatusold = customerDetailsobj.custstatus
            customerDetailsobj.custstatus=dataObj['customerStatus']
        elif customerDetailsobj.custstatus == 'I' and dataObj['customerStatus'] == 'E':
            customerDetailsobj.custstatusold = customerDetailsobj.custstatus
            customerDetailsobj.custstatus=dataObj['customerStatus']
        elif customerDetailsobj.custstatus == 'E' and customerDetailsobj.custstatusold == 'I' and dataObj['customerStatus'] == 'I':
            customerDetailsobj.custstatusold = customerDetailsobj.custstatus
            customerDetailsobj.custstatus=dataObj['customerStatus']
            customerDetailsobj.subscriptionType=dataObj['subscriptionType']
            customerDetailsobj.subscriptionExpirationDate = dataObj['subscriptionExpirationDate']
            customerDetailsobj.amountPaid = dataObj['amountPaid']    
        elif customerDetailsobj.custstatus == 'S' and dataObj['customerStatus'] == 'I':
            customerDetailsobj.custstatusold = customerDetailsobj.custstatus
            customerDetailsobj.custstatus=dataObj['customerStatus']
        customerDetailsobj.updateddt=datetime.datetime.now()
        customerDetailsobj.save()
    except Exception as e:
        logging.error("Error in updating customer details DB " + str(e))
        raise    
    
    
def updateCustTaskStatusDB(profileTaskStatusList):
    try:
        
        for profileTask in profileTaskStatusList:
            custTaskobj=CustTask(custid=profileTask['custid'],taskname=profileTask['taskname'],status=profileTask['status'],tasktype=profileTask['tasktype'])
            custTaskobj.save()
            
    except Exception as e:
        logging.error("Error in creating customer tasks  DB " + str(e))
        raise    

def getTasksByCustIdDB(custID):
    try:
        
        custTaskobjs=CustTask.objects.filter(custid=custID)
        return custTaskobjs    
    except Exception as e:
        logging.error("Error in retreiving customer tasks DB " + str(e))
        raise    

def getTaskByCustIdAndNameDB(custID,taskName):
    try:   
        custTaskobjs=CustTask.objects.filter(custid=custID,taskname=taskName)
        return custTaskobjs    
    except Exception as e:
        logging.error("Error in retreiving customer tasks by custid and task name DB " + str(e))
        raise    

def updateTaskByCustIdAndNameDB(custID,taskName,taskStatus):
    try:   
        custTaskobjs=CustTask.objects.filter(custid=custID,taskname=taskName)
        if len(custTaskobjs) == 1:
            custTaskobjs[0].status = taskStatus
            custTaskobjs[0].save()
        return custTaskobjs    
    except Exception as e:
        logging.error("Error in retreiving customer tasks by custid and task name DB " + str(e))
        raise    
