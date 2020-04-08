from customer.functions.database import getCustomerDetailsDB, saveCustomerDetailsDB
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