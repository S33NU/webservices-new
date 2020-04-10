import logging
from customer.models import Customer


def getCustomerDetailsDB(userName):
    try:
       
        customerDetailsObj=Customer.objects.filter(userName=userName)
        
        return customerDetailsObj
    except Exception as e:
        logging.error("Error in retrieving customer details DB " + str(e))
        raise
    
def saveCustomerDetailsDB(dataObj):
    try:
        
        customerDetailsobjs=getCustomerDetailsDB(dataObj['userName'])
        
        if len(customerDetailsobjs) == 0:
            
            customerDetailsobj=Customer(userName=dataObj['userName'],
                                           customerStatus_old=dataObj['customerStatus_old'],
                                           customerStatus_new=dataObj['customerStatus_new'])
                                           
            customerDetailsobj.save()
    except Exception as e:
        logging.error("Error in saving customer details DB " + str(e))
        raise    
    
def updateCustomerDetailsDB(dataObj):
    try:
        customerDetailsobj=Customer.objects.filter(userName=dataObj['username'])
        if len(customerDetailsobj) == 1:
            customerDetailsobj=customerDetailsobj[0]
        if customerDetailsobj.customerStatus_new == 'P' and customerDetailsobj.customerStatus_old == 'P':
            customerDetailsobj.customerStatus_old = customerDetailsobj.customerStatus_new
            customerDetailsobj.customerStatus_new=dataObj['customerStatus']
            customerDetailsobj.profileStatus=dataObj['profileStatus']
        elif customerDetailsobj.customerStatus_new == 'R' and customerDetailsobj.customerStatus_old == 'P' and dataObj['customerStatus'] == 'S':
            customerDetailsobj.customerStatus_old = customerDetailsobj.customerStatus_new
            customerDetailsobj.customerStatus_new=dataObj['customerStatus']
            customerDetailsobj.profileStatus+=dataObj['profileStatus']
            customerDetailsobj.subscriptionType=dataObj['subscriptionType']
            customerDetailsobj.subscriptionExpirationDate = dataObj['subscriptionExpirationDate']
            customerDetailsobj.amountPaid = dataObj['amountPaid']
        elif customerDetailsobj.customerStatus_new == 'E' and customerDetailsobj.customerStatus_old == 'S':
            customerDetailsobj.customerStatus_old = customerDetailsobj.customerStatus_new
            customerDetailsobj.customerStatus_new=dataObj['customerStatus']
            customerDetailsobj.subscriptionType=dataObj['subscriptionType']
            customerDetailsobj.subscriptionExpirationDate = dataObj['subscriptionExpirationDate']
            customerDetailsobj.amountPaid = dataObj['amountPaid']    
        elif customerDetailsobj.customerStatus_new == 'S' and dataObj['customerStatus'] == 'E':
            customerDetailsobj.customerStatus_old = customerDetailsobj.customerStatus_new
            customerDetailsobj.customerStatus_new=dataObj['customerStatus']
        elif customerDetailsobj.customerStatus_new == 'I' and dataObj['customerStatus'] == 'E':
            customerDetailsobj.customerStatus_old = customerDetailsobj.customerStatus_new
            customerDetailsobj.customerStatus_new=dataObj['customerStatus']
        elif customerDetailsobj.customerStatus_new == 'E' and customerDetailsobj.customerStatus_old == 'I':
            customerDetailsobj.customerStatus_old = customerDetailsobj.customerStatus_new
            customerDetailsobj.customerStatus_new=dataObj['customerStatus']
            customerDetailsobj.subscriptionType=dataObj['subscriptionType']
            customerDetailsobj.subscriptionExpirationDate = dataObj['subscriptionExpirationDate']
            customerDetailsobj.amountPaid = dataObj['amountPaid']    
        elif customerDetailsobj.customerStatus_new == 'S' and dataObj['customerStatus'] == 'I':
            customerDetailsobj.customerStatus_old = customerDetailsobj.customerStatus_new
            customerDetailsobj.customerStatus_new=dataObj['customerStatus']
            customerDetailsobj.profileStatus=dataObj['profileStatus']
        elif dataObj['profileStatus'] == "personal" or dataObj['profileStatus'] == "invest" or dataObj['profileStatus'] == "document" :
            customerDetailsobj.profileStatus=customerDetailsobj.profileStatus.replace(dataObj['profileStatus'], "")
        
        customerDetailsobj.save()
    except Exception as e:
        logging.error("Error in updating customer details DB " + str(e))
        raise    
    