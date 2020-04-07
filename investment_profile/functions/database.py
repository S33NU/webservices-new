from investment_profile.models import  InvestmentProfile, InvestmentQuestions
import logging





def getInvestmentProfileQuestionsDB():
    try:
        
        investmentQuestionsObjs = InvestmentQuestions.objects.filter(investqstatus='A')

        return investmentQuestionsObjs
    except Exception as e:
        logging.error("Error in retrieving Investment Profile questions " + str(e))
        raise


def saveInvestmentProfileDB(dataObj):
    try:

        investmentProfileObj = InvestmentProfile(userName=dataObj['userName'],
                                                 investmentAmount=dataObj['investmentAmount'],
                                                 investmentType=dataObj['investmentType'],
                                                 investmentFrequency=dataObj['investmentFrequency'],
                                                 investmentReviewFrequency=dataObj['investmentReviewFrequency'],
                                                 montlyAvgSavings=dataObj['montlyAvgSavings'],
                                                 lossPercent=dataObj['lossPercent']
                                            )
        investmentProfileObj.save()

    except Exception as e:
        logging.error("Error in saving Investment Profile DB" + str(e))
        raise
