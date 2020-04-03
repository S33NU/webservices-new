import logging
from subscriptions.models import Subscription
def getSubscriptionsListDB():
    try:
        subscriptionObjs = Subscription.objects.all()
        
        return subscriptionObjs
    except Exception as e:
        logging.error("Error in retrieving data from database "+str(e))
        raise