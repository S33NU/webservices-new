
from investment_profile.functions.database import getInvestmentProfileQuestionsDB, saveInvestmentProfileDB
from metadata.functions.database import getLookUpValues,getLookUpID
import logging
from customer.functions.database import getCustomerDetailsDB,updateCustomerDetailsDB


def getInvestmentProfileQuestionsService():
    try:
        profileQuestions=getInvestmentProfileQuestionsDB()
        
        temp = []
        
        for profileQuestion in profileQuestions:
           
            profileQuestionsObj = {
                'profqname':profileQuestion.profqname,
                'profqtype':profileQuestion.profqtype,
                'profqorder':profileQuestion.profqorder,
                #'investqkey': profileQuestion.investqkey,
                #'investqselection': profileQuestion.investqselection,
                'values':None
            }
            if profileQuestion.profqchoicelabels != "null":
                vals=profileQuestion.profqchoicelabels
                profilevalues=vals.split(",")
                profileQuestionsObj['values']=profilevalues
            temp.append(profileQuestionsObj)
        profileQuestions = temp
        return profileQuestions
    except Exception as e:
        logging.error("Error in retrieving investment profile questions service "+str(e))
        

def saveInvestmentProfileService(investment_profile,userName):
    try:
        saveInvestmentProfileDB(investment_profile,userName)
        customerObj = getCustomerDetailsDB(userName)
        customerObj = customerObj[0]
        
        dataObj ={
                'username':userName,
                'customerStatus':customerObj.profileStatus,
                'profileStatus':'invest'
        }
        updateCustomerDetailsDB(dataObj)
    except Exception as e:
        logging.error("Error in saving Investment profile service"+str(e))
        raise
    