from subscriptions.functions.database import getSubscriptionsListDB
import logging



def getSubscriptionsService():
    try:
       subscriptionsList = getSubscriptionsListDB()
       temp=[]
       for subscription in subscriptionsList:
           subscriptionObj={
               'subscriptionKey':subscription[0],
               'subscriptionName':subscription[1],
               'subscriptionDescription':subscription[2],
               'subscriptionCost':subscription[3],
               'subscriptionPeriod':subscription[4]
           }
           temp.append(subscriptionObj) 
       subscriptionsList = temp    
       return subscriptionsList
    except Exception as e:
        logging.error("Error in retrieving subscription list "+str(e))
        raise