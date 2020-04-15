from customer.models import Customer
from metadata.models import LookUpMaster, MenuItems, ProfQuestion
from django.db.models import Q

def validateCookieDB(cookie):
    try:
        registrationObjs=Customer.objects.filter(custregmobile=cookie)

        if len(registrationObjs) == 0:
            
            return False
        elif len(registrationObjs) != 0:
            return True
    except Exception as e:
        logging.error("Error in validating Cookie DB "+str(e))
        raise    


def getLookUpID(lookupname):
    try:
        
        lookupMasterObjs = LookUpMaster.objects.filter(lookupname=lookupname)
        return lookupMasterObjs

    except Exception as e:
        logging.error("Error in retrieving lookUpId " + str(e))
        raise


def getLookUpValues(lookupid):
    try:
        
        lookupMasterObjs = LookUpMaster.objects.filter(~Q(lookupmasterid=0),lookupid=lookupid)
  
        return lookupMasterObjs

    except Exception as e:
        logging.error("Error in retrieving lookUpValues " + str(e))
        raise

def getLookUpValue(lookupID,lookupmasterID):
    try:
        
        lookupMasterObjs = LookUpMaster.objects.filter(lookupmasterid=lookupmasterID,lookupid=lookupID)
  
        return lookupMasterObjs

    except Exception as e:
        logging.error("Error in retrieving lookUpValues " + str(e))
        raise

    
def getMenuItemsByCustomerStatusDB(customerStatus):
    try:
        
        menuItemsObjs = MenuItems.objects.filter(menuItemState__contains=customerStatus)
  
        return menuItemsObjs

    except Exception as e:
        logging.error("Error in retrieving menu items by customer status DB " + str(e))
        raise


def getProfileQuestionsDB(profqclass):
    try:
        
        investmentQuestionsObjs = ProfQuestion.objects.filter(profqclass=profqclass, profqstatus='A')

        return investmentQuestionsObjs
    except Exception as e:
        logging.error("Error in retrieving Profile questions DB " + str(e))
        raise