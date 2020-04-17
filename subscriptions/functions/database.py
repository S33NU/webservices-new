import logging
from subscriptions.models import CustSubscription, CustPayments


def savePaymentDetailsDB(custPayments):
    try:
        
        
        custPaymentsObj= CustPayments(custid=custPayments['custid'],
                                          servid=custPayments['servid'],
                                          custsubid=custPayments['custsubid'],
                                          paymentmod=custPayments['paymentmod'],
                                          paygateway=custPayments['paygateway'],
                                          payamount=custPayments['payamount'],
                                          payreference=custPayments['payreference'])
        custPaymentsObj.save()
    except Exception as e:
        logging.error("Error in saving payment details DB"+str(e))
        raise
    
    
def saveSubscriptionDetailsDB(custSubscription):
    try:
        
        custSubscriptionObj= CustSubscription(custid=custSubscription['custid'],
                                                  servid=custSubscription['servid'],
                                                  servsigneddt=custSubscription['servsigneddt'],
                                                  servexpdt=custSubscription['servexpdt'],
                                                  servstatus=custSubscription['servstatus'])
        custSubscriptionObj.save()
    except Exception as e:
        logging.error("Error in saving subscription details DB"+str(e))
        raise



def getCustSubscriptionByServIDAndCustIdDB(custID,servID,servstatus):
    try:
        custSubscriptionObjs= CustSubscription.objects.filter(custid=custID,servid=servID,servstatus=servstatus)
        return custSubscriptionObjs
    except Exception as e:
        logging.error("Error in retreving cust subscription by servid and custid  DB"+str(e))
        raise

def getCustPaymentByIDsDB(custID,servID,custsubID):
    try:
        custPaymentsObjs = CustPayments.objects.filter(custid=custID,servid=servID,custsubid=custsubID)
        return custPaymentsObjs
    except Exception as e:
        logging.error("Error in retreving cust payment by servid and custid and custsubid DB"+str(e))
        raise

def updateCustSubscriptionPaymentIDDB(custsubID,paymentID):
    try:
        custSubscriptionObjs= CustSubscription.objects.filter(id=custsubID)
        
        if len(custSubscriptionObjs) == 1:
            custSubscriptionObjs[0].servpayid = paymentID
            custSubscriptionObjs[0].save()
        
    except Exception as e:
        logging.error("Error in updating cust subscription payment id DB"+str(e))
        raise

def updateCustSubscriptionStatusDB(custID,servstatus):
    try:

        custSubscriptionObjs= CustSubscription.objects.filter(custid=custID,servstatus='A')
        
        for custSubscriptionObj in custSubscriptionObjs:
            custSubscriptionObj.servstatus = servstatus
            custSubscriptionObj.save()
        
    except Exception as e:
        logging.error("Error in updating cust subscription status by custid and servstatus DB"+str(e))
        raise
    
def getCustSubscriptionByStatusAndCustIdDB(custID,servstatus):
    try:
        custSubscriptionObjs= CustSubscription.objects.filter(custid=custID,servstatus=servstatus)
        return custSubscriptionObjs
    except Exception as e:
        logging.error("Error in retreving cust subscription by status and custid  DB"+str(e))
        raise