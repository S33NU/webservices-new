from customer.functions.database import getCustTasksByCustIdDB,getCustomerDetailsDB, saveCustomerDetailsDB,updateCustomerDetailsDB
import logging

def getCustomerDetailsService(userName):
      try:
        customerDetailsObj = getCustomerDetailsDB(userName)
        if len(customerDetailsObj) == 1:
          return customerDetailsObj[0]
      except Exception as e:
        logging.error("Error in retrieving customer details service "+str(e))
        raise
    
def saveCustomerDetailsService(customer_details):
      try:
        saveCustomerDetailsDB(customer_details)
      except Exception as e:
        logging.error("Error in saving customer details service "+str(e))
        raise
      
def updateCustomerDetailsService(customer_details):
      try:
        updateCustomerDetailsDB(customer_details)
      except Exception as e:
        logging.error("Error in updating customer details service "+str(e))
        raise      
      
def getCustomerEmailandMobileService(userName):
    try:
        customerDetailsObj = getCustomerDetailsDB(userName)
        if len(customerDetailsObj) == 1:
            customerDetailsObj=customerDetailsObj[0]
        dataObj = {
            'custregmobile':customerDetailsObj.custregmobile,
            'custemail':customerDetailsObj.custemail  
        }
        
        return dataObj
    except Exception as e:
        logging.error("Error in  retreiving registration details  service "+str(e))
        raise

def getCustTasksByCustIdService(custID):
    try:
        customerTasksObjs = getCustTasksByCustIdDB(custID)
        return customerTasksObjs
    except Exception as e:
      logging.error("Error in retrieving customer tasks by custID service "+str(e))
      raise
      
