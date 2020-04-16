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


def saveCustomerProfileDB(dataObj):


    mblno=dataObj['RegisteredMobile']

    custprofilebymblno=Customer.objects.get(custregmobile=mblno)

    custprofilebymblno.custfirstname=dataObj['FirstName']
    custprofilebymblno.custlastname=dataObj['LastName']
    custprofilebymblno.custemail=dataObj['EMail']
    custprofilebymblno.custmaritalstatus=dataObj['MarriedStatus']
    custprofilebymblno.custagegroup=dataObj['AgeGroup']
    custprofilebymblno.custadd1=dataObj['AddressLine1']
    custprofilebymblno.custadd2=dataObj['AddressLine2']
    custprofilebymblno.custcity=dataObj['City']
    custprofilebymblno.custstate=dataObj['State']
    custprofilebymblno.zipcode=dataObj['Pincode']
    custprofilebymblno.custoccupation=dataObj['Occupation']
    custprofilebymblno.updateddt=datetime.datetime.now()
    custprofilebymblno.save()



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

def getCustTasksByCustIdDB(custID):
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
