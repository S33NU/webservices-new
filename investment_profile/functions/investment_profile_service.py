
from investment_profile.functions.database import saveInvestmentProfileDB, getInvestmentProfileDB, updateInvestmentProfileDB
from metadata.functions.database import getLookUpValues,getLookUpID
import logging
from customer.functions.database import getCustomerDetailsDB,checkTaskStatusByCustIdAndNameDB,updateTaskByCustIdAndNameDB


      

def saveInvestmentProfileService(investmentProfileList,userName):
    try:
        customerDetailsobjs=getCustomerDetailsDB(userName)
        saveInvestmentProfileDB(investmentProfileList,customerDetailsobjs[0].id)
        updateTaskByCustIdAndNameDB(customerDetailsobjs[0].id,'Investment','C')
        
    
    except Exception as e:
        logging.error("Error in saving Investment profile service"+str(e))
        raise
    
    
def getInvestmentProfileService(userName):
    try:
        customerDetailsobjs=getCustomerDetailsDB(userName)
        
        custTaskObj=checkTaskStatusByCustIdAndNameDB(customerDetailsobjs[0].id,'Investment')
        investmentData = False
        if len(custTaskObj) == 0:
            
            custInvestmentgProfileObjs=getInvestmentProfileDB(customerDetailsobjs[0].id)
            
            investmentData = []
            for custInvestmentgProfileObj in custInvestmentgProfileObjs:
                
                obj = {
                    'order':custInvestmentgProfileObj.order,
                    'attribute':custInvestmentgProfileObj.attribute,
                    'custresponse':custInvestmentgProfileObj.custresponse,
                    'attributetype':custInvestmentgProfileObj.attributetype
                }
            
                investmentData.append(obj)
            
        return investmentData     
    except Exception as e:
        logging.error("Error in retreving Investment profile By custID service"+str(e))
        raise
    
def updateInvestmentProfileService(investmentProfileList,userName):
    try:
        customerDetailsobjs=getCustomerDetailsDB(userName)
        print(investmentProfileList)
        updateInvestmentProfileDB(investmentProfileList,customerDetailsobjs[0].id)
        
    
    except Exception as e:
        logging.error("Error in updating Investment profile service"+str(e))
        raise