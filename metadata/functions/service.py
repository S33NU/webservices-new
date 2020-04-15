from metadata.functions.database import validateCookieDB,getMenuItemsByCustomerStatusDB, getProfileQuestionsDB
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


def getProfileQuestionsService(profqclass):
    try:
        profileQuestions=getProfileQuestionsDB(profqclass)
        
        temp = []
        
        for profileQuestion in profileQuestions:
           
            profileQuestionsObj = {
                'profqname':profileQuestion.profqname,
                'profqtype':profileQuestion.profqtype,
                'profqorder':profileQuestion.profqorder,
                'values':None
            }
            if profileQuestion.profqchoicelabels != "null":
                vals=profileQuestion.profqchoicelabels
                profilevalues=vals.split(",")
                profileQuestionsObj['values']=profilevalues
            temp.append(profileQuestionsObj)
        profileQuestions = temp
        profileQuestions = sorted(profileQuestions,key=lambda x:x['profqorder'])
        return profileQuestions
    except Exception as e:
        logging.error("Error in retrieving profile questions service "+str(e))
  