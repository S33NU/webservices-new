from subscriptions.functions.database import getSubscriptionsListDB
import logging



def getSubscriptionsService():
    try:
       subscriptionsList = getSubscriptionsListDB()
       temp=[]
       for subscription in subscriptionsList:
           subscriptionObj={
               'subscriptionKey':subscription.subscriptionKey,
               'subscriptionName':subscription.subscriptionName,
               'subscriptionDescription':subscription.subscriptionDescription,
               'subscriptionCost':subscription.subscriptionCost,
               'subscriptionPeriod':subscription.subscriptionPeriod
           }
           temp.append(subscriptionObj) 
       subscriptionsList = temp    
       return subscriptionsList
    except Exception as e:
        logging.error("Error in retrieving subscription list "+str(e))
        raise