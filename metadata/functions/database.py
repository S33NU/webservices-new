from registration.models import Registration
from metadata.models import LookUpMaster, MenuItems
from django.db.models import Q
def validateCookieDB(cookie):
    try:
        registrationObjs=Registration.objects.filter(phonenumber=cookie)

        if len(registrationObjs) == 0:
            
            return False
        elif len(registrationObjs) != 0:
            return True     
    except Exception as e:
        logging.error("Error in validating Cookie DB "+str(e))
        raise    

def validateClientOTPByEmailDB(dataObj):
    try:
        registrationObjs=Registration.objects.filter(email_otp=dataObj['otp'],email=dataObj['email'])
            
        return registrationObjs
    except Exception as e:
        logging.error("Error in validating client password by email in DB "+str(e))
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
    
def getMenuItemsByCustomerStatusDB(customerStatus):
    try:
        
        menuItemsObjs = MenuItems.objects.filter(menuItemState__contains=customerStatus)
  
        return menuItemsObjs

    except Exception as e:
        logging.error("Error in retrieving menu items by customer status DB " + str(e))
        raise
    