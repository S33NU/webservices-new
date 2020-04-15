
from investment_profile.functions.database import saveInvestmentProfileDB
from metadata.functions.database import getLookUpValues,getLookUpID
import logging
from customer.functions.database import getCustomerDetailsDB,updateCustomerDetailsDB,updateTaskByCustIdAndNameDB


      

def saveInvestmentProfileService(investmentProfileList,userName):
    try:
        customerDetailsobjs=getCustomerDetailsDB(userName)
        saveInvestmentProfileDB(investmentProfileList,customerDetailsobjs[0].id)
        updateTaskByCustIdAndNameDB(customerDetailsobjs[0].id,'I','C')
        
    
    except Exception as e:
        logging.error("Error in saving Investment profile service"+str(e))
        raise
    