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

def updateInvestmentProfileDB(investmentProfileList,custID):
    try:
        
        for investmentProfileObj in investmentProfileList:
            custInvestmentProfileObjs = CustInvestmentProfile.objects.filter(custid=custID,
                                                                             attribute=investmentProfileObj['attribute'])

            
            if len(custInvestmentProfileObjs) == 1:
                 custInvestmentProfileObjs[0].custresponse=investmentProfileObj['custresponse']
                 custInvestmentProfileObjs[0].save()
                
            elif len(custInvestmentProfileObjs) == 0:
                
                custInvestmentProfileObj = CustInvestmentProfile(custid=custID,
                                                 order=investmentProfileObj['order'],
                                                 attribute=investmentProfileObj['attribute'],
                                                 custresponse=investmentProfileObj['custresponse'],
                                                 attributetype=investmentProfileObj['attributetype'],
                                                 createddt=datetime.datetime.now()
                                            )
                custInvestmentProfileObj.save()

    except Exception as e:
        logging.error("Error in updating Investment Profile DB " + str(e))
        raise
