import logging
from personal_profile.models import PersonalProfile,CustPersonalProfile
from customer.models import Customer
from metadata.models import ProfQuestion
from django.db.models import Q
import datetime





def savePersonalProfileDB(dataObj,custID):
    try:

        for custProfileObj in dataObj:
            custPersonalProfileObj = CustPersonalProfile(custid=custID,
                                                             order=custProfileObj['order'],
                                                             attribute=custProfileObj['attribute'],
                                                             custresponse=custProfileObj['custresponse'],
                                                             attributetype=custProfileObj['attributetype'],
                                                             createddt=datetime.datetime.now()
                                                             )
            custPersonalProfileObj.save()

    except Exception as e:
        logging.error("Error in saving Personal Profile " + str(e))
        raise


def getcustPersonalProfileDB(custID):
    try:
        custPersonalProfileObjs = CustPersonalProfile.objects.filter(custid=custID)
        return custPersonalProfileObjs
    except Exception as e:
        logging.error("Error in retrieving Personal Profile by custID DB" + str(e))
        raise

def updatecustPersonalProfileDB(custPersonalProfileupdatedata,custID):
    try:

       for custPersonalProfileupdatedataObj in custPersonalProfileupdatedata:

            custPersoanlProfileObjs = CustPersonalProfile.objects.filter(custid=custID,
                                                                         attribute=custPersonalProfileupdatedataObj['attribute'])

            if len(custPersoanlProfileObjs) == 1:

                custPersoanlProfileObjs[0].custresponse = custPersonalProfileupdatedataObj['custresponse']
                custPersoanlProfileObjs[0].save()

            elif len(custPersoanlProfileObjs) == 0:

                custPersoanlProfileObj = CustPersonalProfile(custid=custID,
                                                                 order=custPersonalProfileupdatedataObj['order'],
                                                                 attribute=custPersonalProfileupdatedataObj['attribute'],
                                                                 custresponse=custPersonalProfileupdatedataObj['custresponse'],
                                                                 attributetype=custPersonalProfileupdatedataObj['attributetype'],
                                                                 createddt=datetime.datetime.now()
                                                                 )
                custPersoanlProfileObj.save()

    except Exception as e:
        logging.error("Error in updating Personal Profile DB " + str(e))
        raise









#From here old methods





def getProfileData():
    try:
        profiles = PersonalProfile.objects.all()
        return profiles

    except Exception:
        raise


def getProfileDataFromDbById(id):
    try:
        profilebyID = PersonalProfile.objects.filter(pk=id)
        return profilebyID

    except Exception:
        raise


def updateProfileDataFromDbById(id, dataObj):
    try:
        profile = PersonalProfile.objects.get(pk=id)
        try:
            if profile != []:
                profileEdit = PersonalProfile(pk=id,registeredmobile=dataObj['registeredMobile'],
                                              firstname=dataObj['firstName'],
                                              lastname=dataObj['lastName'], email=dataObj['email'],
                                              marriedstatus=dataObj['marriedStatus'], age=dataObj['age'],
                                              addr1=dataObj['addrLine1'], addr2=dataObj['addrLine2'],
                                              addr3=dataObj['addrLine3'], addr4=dataObj['addrLine4'],
                                              occupation=dataObj['occupation'])
                profileEdit.save()
        except Exception:
            raise

    except Exception:
        raise






