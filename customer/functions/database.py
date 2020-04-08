import logging
from customer.models import Customer


def getCustomerDetailsDB(userName):
    try:
       
        customerDetailsobj=Customer.objects.filter(userName=userName)
        
        return customerDetailsobj
    except Exception as e:
        logging.error("Error in retrieving customer details DB " + str(e))
        raise
    
def saveCustomerDetailsDB(dataObj):
    try:
        
        customerDetailsobjs=getCustomerDetailsDB(dataObj['userName'])
        if len(customerDetailsobjs) == 0:
            
            customerDetailsobj=Customer(userName=dataObj['userName'],
                                           customerStatus=dataObj['customerStatus'])
                                           
            customerDetailsobj.save()
    except Exception as e:
        logging.error("Error in saving customer details DB " + str(e))
        raise    
    
def updateCustomerDetailsDB(dataObj):
    try:
        customerDetailsobj=Customer.objects.filter(userName=dataObj['username'])
        if len(customerDetailsobj) == 1:
            customerDetailsobj=customerDetailsobj[0]
        if customerDetailsobj.customerStatus == 'P' and dataObj['customerStatus'] == 'R':
            customerDetailsobj.customerStatus=dataObj['customerStatus']
            customerDetailsobj.profileStatus=dataObj['profileStatus']
        elif customerDetailsobj.customerStatus == 'R' and dataObj['customerStatus'] == 'S':
            customerDetailsobj.customerStatus=dataObj['customerStatus']
            customerDetailsobj.profileStatus+=dataObj['profileStatus']
            customerDetailsobj.subscriptionType=dataObj['subscriptionType']
            customerDetailsobj.subscriptionExpirationDate = dataObj['subscriptionExpirationDate']
            customerDetailsobj.amountPaid = dataObj['amountPaid']
        elif customerDetailsobj.customerStatus == 'R' and dataObj['customerStatus'] == 'R':
            customerDetailsobj.profileStatus=dataObj['profileStatus']
        elif customerDetailsobj.customerStatus == 'S' and dataObj['customerStatus'] == 'S':
            customerDetailsobj.profileStatus=dataObj['profileStatus']
        elif customerDetailsobj.customerStatus == 'S' and dataObj['customerStatus'] == 'I':
            customerDetailsobj.customerStatus=dataObj['customerStatus']
        elif customerDetailsobj.customerStatus == 'I' and dataObj['customerStatus'] == 'E':
            customerDetailsobj.customerStatus=dataObj['customerStatus']
        elif customerDetailsobj.customerStatus == 'E' and dataObj['customerStatus'] == 'I':
            customerDetailsobj.customerStatus=dataObj['customerStatus']
            customerDetailsobj.subscriptionType=dataObj['subscriptionType']
            customerDetailsobj.subscriptionExpirationDate = dataObj['subscriptionExpirationDate']
            customerDetailsobj.amountPaid = dataObj['amountPaid']
            
        customerDetailsobj.save()
    except Exception as e:
        logging.error("Error in updating customer details DB " + str(e))
        raise    
    