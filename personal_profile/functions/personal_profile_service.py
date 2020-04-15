from personal_profile.functions.database import savePersonalProfileDB,getProfileData, getProfileDataFromDbById, updateProfileDataFromDbById
import logging
from metadata.functions.database import getLookUpValues,getLookUpID
from customer.functions.database import getCustomerDetailsDB,updateCustomerDetailsDB

def savePersonalProfileService(personal_profile,userName):
    try:
        savePersonalProfileDB(personal_profile)
        customerObj = getCustomerDetailsDB(userName)
        customerObj = customerObj[0]
        
        dataObj ={
                'username':userName,
                'customerStatus':customerObj.profileStatus,
                'profileStatus':'personal'
        }
        updateCustomerDetailsDB(dataObj)
    except Exception as e:
        logging.error("Error in saving personal profile "+str(e))
        raise


def personalProfileDataService():
    try:
        profiles = getProfileData()
        temp = []
        for profile in profiles:
            prof = {
                'ID': profile.id,
                "registeredMobile": profile.registeredmobile,
                "firstName": profile.firstname,
                "lastName": profile.lastname,
                "email": profile.email,
                "marriedStatus": profile.marriedstatus,
                "age": profile.age,
                "addrLine1": profile.addr1,
                "addrLine2": profile.addr2,
                "addrLine3": profile.addr3,
                "addrLine4": profile.addr4,
                "occupation": profile.occupation
            }
            temp.append(prof)
        return temp
    except Exception as msg:
        logging.error('Error in getting Profiles' + str(msg))
        raise


def personalProfileDataByIdService(id):
    try:
        profilebyID = getProfileDataFromDbById(id)
        temp = []
        for profile in profilebyID:
            byid = {
                'ID': profile.id,
                "registeredMobile": profile.registeredmobile,
                "firstName": profile.firstname,
                "lastName": profile.lastname,
                "email": profile.email,
                "marriedStatus": profile.marriedstatus,
                "age": profile.age,
                "addrLine1": profile.addr1,
                "addrLine2": profile.addr2,
                "addrLine3": profile.addr3,
                "addrLine4": profile.addr4,
                "occupation": profile.occupation
            }
            temp.append(byid)
        if temp == []:
            return 0
        else:
            return temp
    except Exception as msg:
        logging.error('Error in getting Profiles' + str(msg))
        raise


def personalProfileEditDataByIdService(id, data):
    try:
        updateProfileDataFromDbById(id, data)
    except Exception as msg:
        logging.error('Error in updating Profiles' + str(msg))
        raise


    

