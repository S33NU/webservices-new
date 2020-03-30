import mysql.connector
import logging
from mysql.connector import errorcode
from metadata.functions.metadata import connectToDatabase

def getSubscriptionsListDB():
    try:
        cnx=connectToDatabase()
        mycursor = cnx.cursor()
        mycursor.execute("select subscriptionKey,subscriptionName,subscriptionDescription,subscriptionCost,subscriptionPeriod  from subscription")
        
        result = mycursor.fetchall()
        
        cnx.close()
        
        return result
    except Exception as e:
        logging.error("Error in retrieving data from database "+str(e))
        raise