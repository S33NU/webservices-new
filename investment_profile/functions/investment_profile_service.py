
from investment_profile.functions.database import getInvestmentProfileQuestionsDB
from metadata.functions.database import getLookUpValues,getLookUpID
import logging


def getInvestmentProfileQuestionsService():
    try:
        profileQuestions=getInvestmentProfileQuestionsDB()
        
        temp = []
        
        for profileQuestion in profileQuestions:
           
            profileQuestionsObj = {
                'investqname':profileQuestion.investqname,
                'investqtype':profileQuestion.investqtype,
                'investqorder':profileQuestion.investqorder,
                'investqkey': profileQuestion.investqkey,
                'investqselection': profileQuestion.investqselection,
                'values':None
            }
            
            lookUpId = getLookUpID(profileQuestionsObj['investqkey'])
            
            if len(lookUpId) != 0:
                
                lookUpValues = getLookUpValues(lookUpId[0].lookupid)
                lookUpValues = [ lookUpValue.lookupname+":"+lookUpValue.lookupparam1 for lookUpValue in lookUpValues]
                profileQuestionsObj['values']=lookUpValues      
            temp.append(profileQuestionsObj)
        profileQuestions = temp
        #print(profileQuestions)
        return profileQuestions
    except Exception as e:
        logging.error("Error in retrieving investment profile questions "+str(e))
        

