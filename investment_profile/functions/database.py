from investment_profile.models import CustInvestmentProfile
from metadata.models import ProfQuestion
import logging
import datetime




def getInvestmentProfileQuestionsDB():
    try:
        
        investmentQuestionsObjs = ProfQuestion.objects.filter(profqclass='I', profqstatus='A')

        return investmentQuestionsObjs
    except Exception as e:
        logging.error("Error in retrieving Investment Profile questions DB " + str(e))
        raise


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
