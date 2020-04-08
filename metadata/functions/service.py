from metadata.functions.database import validateCookieDB, validateClientOTPByEmailDB,getMenuItemsByCustomerStatusDB
import logging


def validateCookieService(cookie):
    try:
        cookieStatus=validateCookieDB(cookie)
        
        if cookieStatus:
            return True
        else: 
            return False
    except Exception as e:
        logging.error("Error in validating Cookie Service "+str(e))
        raise    
    
def verifyOTPByEmailService(dataObj):
    try:
        clientList = validateClientOTPByEmailDB(dataObj)
        if len(clientList) != 0:
            return True
        else:
            return False
    except Exception as e:
        logging.error("Error in verifyting OTP by email" + str(e))
        raise

def getMenuItemsByCustomerStatuService(customerStatus):
    try:
        menuItemList= getMenuItemsByCustomerStatusDB(customerStatus)
        
        temp = []
        
        for menuItemObj in menuItemList:
           
            menuItemObjList = [menuItem for menuItem in temp if menuItem['menuItemParent'] == menuItemObj.menuItemParent]
            
            if len(menuItemObjList) == 0:
                    
                uiMenuItemObj = {
                    'menuItemParent':menuItemObj.menuItemParent,
                    'UIIcon': menuItemObj.UIIcon,
                    'menuItemKey':menuItemObj.menuItemKey,
                    'child':[] 
                }
                uiMenuItemObj['child'].append({'menuItemName':menuItemObj.menuItemName,'menuItemLink':menuItemObj.menuItemLink})
                temp.append(uiMenuItemObj)
            elif len(menuItemObjList) == 1:
                temp=[menuItem for menuItem in temp if menuItem['menuItemParent'] != menuItemObj.menuItemParent]   
                menuItemObjList[0]['child'].append({'menuItemName':menuItemObj.menuItemName,'menuItemLink':menuItemObj.menuItemLink})         
                temp.append(menuItemObjList[0])
        
        menuItemList = temp
        return menuItemList
    except Exception as e:
        logging.error("Error in retrieving menu items by customer status service" + str(e))
        raise
