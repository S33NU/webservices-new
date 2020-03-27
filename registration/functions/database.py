import mysql.connector
import logging
from mysql.connector import errorcode
from metadata.functions.metadata import connectToDatabase


def saveClientPasswordDB(dataObj):
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()
        sql = "UPDATE registration SET password = '" + dataObj['password'] + "' WHERE phonenumber ={}".format(
            dataObj['phonenumber'])
        mycursor.execute(sql)
        cnx.commit()
        cnx.close()
    except Exception as e:
        logging.error("Error in saving client password " + str(e))
        raise


def validateClientMobileDB(dataObj, ip, device):
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()
        sql = "SELECT phonenumber,ip_address,device FROM registration WHERE phonenumber='{}' AND ip_address='{}' AND device='{}'".format(
            dataObj['phonenumber'], ip, device)
        mycursor.execute(sql)
        mobilenos = mycursor.fetchall()
        return mobilenos
    except Exception as msg:
        logging.error("Error in getting mobile nos from DB: " + str(msg))
        raise


def saveClientMobileDB(dataObj, ip, device):
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()
        sql = "INSERT INTO registration(phonenumber,ip_address,device) VALUES(%s,%s,%s)"
        val = (dataObj['phonenumber'], ip, device)
        mycursor.execute(sql, val)

        cnx.commit()
        cnx.close()
    except Exception as e:
        logging.error("Error in saving client mobile number in DB " + str(e))
        raise

def validateClientPasswordDB(dataObj):
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()
        sql = "SELECT phonenumber,password from registration WHERE password='"+dataObj['password']+"' and phonenumber = {}".format(dataObj['phonenumber'])

        mycursor.execute(sql)
        result=mycursor.fetchall()
        cnx.close()
        return result
    except Exception as e:
        logging.error("Error in validating client password DB "+str(e))
        raise 
