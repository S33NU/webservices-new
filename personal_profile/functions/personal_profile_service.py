from personal_profile.functions.database import savePersonalProfileDB, getcustPersonalProfileDB, \
    updatecustPersonalProfileDB
import logging
from metadata.functions.database import getLookUpValues, getLookUpID
from customer.functions.database import getCustomerDetailsDB, updateCustomerDetailsDB, \
    updateTaskByCustIdAndNameDB, saveCustomerDetailsDB, updateCustomerProfileDB, checkTaskStatusByCustIdAndNameDB
from customer.models import Customer


def savePersonalProfileService(personal_profile, userName):
    try:
        customerDetailsobjs = getCustomerDetailsDB(userName)
        updateCustomerProfileDB(personal_profile['cust'])
        savePersonalProfileDB(personal_profile['custProfile'], customerDetailsobjs[0].id)
        updateTaskByCustIdAndNameDB(customerDetailsobjs[0].id, 'Personal', 'C')

    except Exception as e:
        logging.error("Error in saving personal profile " + str(e))
        raise


def getcustPersonalProfileService(userName):
    try:
        customerDetailsobjs = getCustomerDetailsDB(userName)

        custTaskObj = checkTaskStatusByCustIdAndNameDB(customerDetailsobjs[0].id, 'Personal')
        custPersonalProfileData = False
        print(customerDetailsobjs[0].id)
        print(len(custTaskObj))
        if len(custTaskObj) == 0:

            custPersonalProfileObjs = getcustPersonalProfileDB(customerDetailsobjs[0].id)

            custPersonalProfileData = []
            for custPersoanlProfileObj in custPersonalProfileObjs:
                obj = {
                    'order': custPersoanlProfileObj.order,
                    'attribute': custPersoanlProfileObj.attribute,
                    'custresponse': custPersoanlProfileObj.custresponse,
                    'attributetype': custPersoanlProfileObj.attributetype
                }

                custPersonalProfileData.append(obj)
        elif len(custTaskObj) != 0:
            custMblandEmail = Customer.objects.get(id=customerDetailsobjs[0].id)
            custPersonalProfileData = {
                "custregmobile": custMblandEmail.custregmobile,
                "custemail": custMblandEmail.custemail
            }

        return custPersonalProfileData
    except Exception as e:
        logging.error("Error in retrieving Personal profile By custID service" + str(e))
        raise


def updateCustPersonalProfileService(custPersonalProfileUpdatedata, userName):
    try:
        customerDetailsobjs = getCustomerDetailsDB(userName)
        print(custPersonalProfileUpdatedata['custProfile'])
        updateCustomerProfileDB(custPersonalProfileUpdatedata['cust'])
        updatecustPersonalProfileDB(custPersonalProfileUpdatedata['custProfile'], customerDetailsobjs[0].id)

    except Exception as e:
        logging.error("Error in updating Personal Profile service" + str(e))
        raise
