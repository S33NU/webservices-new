import logging
from personal_profile.models import PersonalProfile
from personal_profile.models import ProfQuestion
from django.db.models import Q
from metadata.models import LookUpMaster
def savePersonalProfileDB(dataObj):
    try:

        clientProfiledata = PersonalProfile(registeredmobile=dataObj['registeredMobile'],
                                            firstname=dataObj['firstName'],
                                            lastname=dataObj['lastName'], email=dataObj['email'],
                                            marriedstatus=dataObj['marriedStatus'], age=dataObj['age'],
                                            addr1=dataObj['addrLine1'], addr2=dataObj['addrLine2'],
                                            addr3=dataObj['addrLine3'], addr4=dataObj['addrLine4'],
                                            occupation=dataObj['occupation']
                                            )
        clientProfiledata.save()

    except Exception as e:
        logging.error("Error in saving Personal Profile " + str(e))
        raise


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


def getPersonalProfileQuestionsDB():
    try:
        
        profQuestionsObjs = ProfQuestion.objects.all()
        
        return profQuestionsObjs
    except Exception as e:
        logging.error("Error in retrieving Personal Profile questions " + str(e))
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
