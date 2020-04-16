from investment_profile.models import CustInvestmentProfile
from metadata.models import ProfQuestion
import logging
import datetime


def saveInvestmentProfileDB(investmentProfileList,custID):
    try:

        for investmentProfileObj in investmentProfileList:
        
            custInvestmentProfileObj = CustInvestmentProfile(custid=custID,
                                                 order=investmentProfileObj['order'],
                                                 attribute=investmentProfileObj['attribute'],
                                                 custresponse=investmentProfileObj['custresponse'],
                                                 attributetype=investmentProfileObj['attributetype'],
                                                 createddt=datetime.datetime.now()
                                            )
            custInvestmentProfileObj.save()

    except Exception as e:
        logging.error("Error in saving Investment Profile DB" + str(e))
        raise


def getInvestmentProfileDB(custID):
    try:
        custInvestmentProfileObjs = CustInvestmentProfile.objects.filter(custid=custID)
        return custInvestmentProfileObjs
    except Exception as e:
        logging.error("Error in retreving Investment Profile by custID DB" + str(e))
        raise
