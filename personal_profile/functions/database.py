import logging
from personal_profile.models import CustPersonalProfile
from customer.models import Customer
from metadata.models import ProfQuestion
from django.db.models import Q
import datetime


def savePersonalProfileDB(dataObj, custID):
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


def updatecustPersonalProfileDB(custPersonalProfileupdatedata, custID):
    try:

        for custPersonalProfileupdatedataObj in custPersonalProfileupdatedata:

            custPersoanlProfileObjs = CustPersonalProfile.objects.filter(custid=custID,
                                                                         attribute=custPersonalProfileupdatedataObj[
                                                                             'attribute'])

            if len(custPersoanlProfileObjs) == 1:

                custPersoanlProfileObjs[0].custresponse = custPersonalProfileupdatedataObj['custresponse']
                custPersoanlProfileObjs[0].save()

            elif len(custPersoanlProfileObjs) == 0:

                custPersoanlProfileObj = CustPersonalProfile(custid=custID,
                                                             order=custPersonalProfileupdatedataObj['order'],
                                                             attribute=custPersonalProfileupdatedataObj['attribute'],
                                                             custresponse=custPersonalProfileupdatedataObj[
                                                                 'custresponse'],
                                                             attributetype=custPersonalProfileupdatedataObj[
                                                                 'attributetype'],
                                                             createddt=datetime.datetime.now()
                                                             )
                custPersoanlProfileObj.save()

    except Exception as e:
        logging.error("Error in updating Personal Profile DB " + str(e))
        raise
