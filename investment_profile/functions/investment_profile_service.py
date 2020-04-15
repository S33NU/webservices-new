
from investment_profile.functions.database import getInvestmentProfileQuestionsDB, saveInvestmentProfileDB
from metadata.functions.database import getLookUpValues,getLookUpID
import logging
from customer.functions.database import getCustomerDetailsDB,updateCustomerDetailsDB,updateTaskByCustIdAndNameDB


def getInvestmentProfileQuestionsService():
    try:
        profileQuestions=getInvestmentProfileQuestionsDB()
        
        temp = []
        
        for profileQuestion in profileQuestions:
           
            profileQuestionsObj = {
                'profqname':profileQuestion.profqname,
                'profqtype':profileQuestion.profqtype,
                'profqorder':profileQuestion.profqorder,
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
        

def saveInvestmentProfileService(investmentProfileList,userName):
    try:
        customerDetailsobjs=getCustomerDetailsDB(userName)
        saveInvestmentProfileDB(investmentProfileList,customerDetailsobjs[0].id)
        updateTaskByCustIdAndNameDB(customerDetailsobjs[0].id,'I','C')
        
    
    except Exception as e:
        logging.error("Error in saving Investment profile service"+str(e))
        raise
    