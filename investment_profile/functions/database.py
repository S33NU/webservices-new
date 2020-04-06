from investment_profile.models import  InvestmentProfile, InvestmentQuestions
import logging





def getInvestmentProfileQuestionsDB():
    try:
        
        investmentQuestionsObjs = InvestmentQuestions.objects.filter(investqstatus='A')

        return investmentQuestionsObjs
    except Exception as e:
        logging.error("Error in retrieving Investment Profile questions " + str(e))
        raise
