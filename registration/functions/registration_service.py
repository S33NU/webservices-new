from registration.functions.database import saveClientPAsswordDB,saveClientMobileDB
import logging



def saveClientPasswordService(dataObj):
    try:
        saveClientPAsswordDB(dataObj)
    except Exception as e:
        logging.error("Error in saving client password "+str(e))
        raise


def saveClientMobileService(dataObj):
    try:
        saveClientMobileDB(dataObj)
    except Exception as e:
        logging.error("Error in saving Client Mobile number"+str(e))
        raise
