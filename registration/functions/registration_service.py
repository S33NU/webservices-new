from registration.functions.database import saveClientPasswordDB,validateClientPasswordDB
import logging



def saveClientPasswordService(dataObj):
    try:
        saveClientPasswordDB(dataObj)
    except Exception as e:
        logging.error("Error in saving client password "+str(e))
        raise


def saveClientMobileService(dataObj):
    try:
        pass
        #saveClientMobileDB(dataObj)
    except Exception as e:
        logging.error("Error in saving Client Mobile number"+str(e))
        raise

def validateClientPasswordService(dataObj):
    try:
        clientList=validateClientPasswordDB(dataObj)
        if len(clientList) == 1:
            return True
        else:
            return False
    except Exception  as e:
        logging.error("Error in validating client credentials")
        raise    