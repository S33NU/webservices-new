import mysql.connector
import logging
from mysql.connector import errorcode
from metadata.functions.metadata import connectToDatabase


def saveClientPasswordDB(dataObj):
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()
        sql = "UPDATE registration SET password = '" + dataObj['password'] + "' WHERE phonenumber ='{}'".format(
                 dataObj['userName'])
        mycursor.execute(sql)
        cnx.commit()
        
        sql = "UPDATE registration SET password = '" + dataObj['password'] + "' WHERE email ='{}'".format(
                 dataObj['userName'])
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
        sql = "SELECT phonenumber,ip_address,device FROM registration WHERE password != 'None' AND phonenumber='{}' AND ip_address='{}' AND device='{}'".format(
            dataObj['phonenumber'], ip, device)
        mycursor.execute(sql)
        mobilenos = mycursor.fetchall()
        return mobilenos
    except Exception as msg:
        logging.error("Error in getting mobile number from DB: " + str(msg))
        raise


def saveClientMobileDB(dataObj, ip, device):
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()
        sql = "INSERT INTO registration(phonenumber,ip_address,device,password) VALUES(%s,%s,%s,%s)"
        val = (dataObj['phonenumber'], ip, device,'None')
        mycursor.execute(sql, val)
        cnx.commit()
        
        sql = "SELECT password FROM registration WHERE phonenumber='{}'".format(dataObj['phonenumber'])
        
        mycursor.execute(sql)
        clientPassword = mycursor.fetchall()
        
        if clientPassword[0][0] == 'None':
            pass
        elif clientPassword[0][0] != 'None':
            sql = "UPDATE registration SET password = '" + clientPassword[0][0] + "' WHERE phonenumber='{}' AND ip_address='{}' AND device='{}'".format(
            dataObj['phonenumber'], ip, device)
            mycursor.execute(sql)
            cnx.commit()
        
        cnx.close()
    except Exception as e:
        logging.error("Error in saving client mobile number in DB " + str(e))
        raise

def validateClientPasswordDB(dataObj):
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()
        sql = "SELECT phonenumber,password from registration WHERE password='"+dataObj['password']+"' and phonenumber = '{}'".format(dataObj['phonenumber'])

        mycursor.execute(sql)
        result=mycursor.fetchall()
        cnx.close()
        return result
    except Exception as e:
        logging.error("Error in validating client password DB "+str(e))
        raise 

def checkClientPasswordDB(dataObj):
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()
        sql = "SELECT password from registration WHERE phonenumber='{}'".format(dataObj['phonenumber'])

        mycursor.execute(sql)
        result=mycursor.fetchall()
        cnx.close()
        return result
    except Exception as e:
        logging.error("Error in checking client password DB "+str(e))
        raise 



def validateClientEmailDB(dataObj, ip, device):
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()
        sql = "SELECT phonenumber,ip_address,device FROM registration WHERE password!='None' AND email='{}' AND ip_address='{}' AND device='{}'".format(
            dataObj['email'], ip, device)
        mycursor.execute(sql)
        mobilenos = mycursor.fetchall()
        return mobilenos
    except Exception as msg:
        logging.error("Error in getting email from DB: " + str(msg))
        raise


def saveClientEmailDB(dataObj, ip, device, otp):
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()
        sql = "INSERT INTO registration(email,ip_address,device,email_otp,password) VALUES(%s,%s,%s,%s,%s)"
        val = (dataObj['email'], ip, device, otp,'None')
        mycursor.execute(sql, val)
        cnx.commit()
        
        sql = "SELECT password FROM registration WHERE email='{}'".format(dataObj['email'])
        
        mycursor.execute(sql)
        clientPassword = mycursor.fetchall()
        
        if clientPassword[0][0] == 'None':
            pass
        elif clientPassword[0][0] != 'None':
            sql = "UPDATE registration SET password = '" + clientPassword[0][0] + "' WHERE email='{}' AND ip_address='{}' AND device='{}'".format(
            dataObj['email'], ip, device)
            mycursor.execute(sql)
            cnx.commit()
        
        cnx.close()
    except Exception as e:
        logging.error("Error in saving client email in DB " + str(e))
        raise

def validateClientPasswordByEmailDB(dataObj):
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()
        sql = "SELECT email,password from registration WHERE password='"+dataObj['password']+"' and email = '{}'".format(dataObj['email'])

        mycursor.execute(sql)
        result=mycursor.fetchall()
        cnx.close()
        return result
    except Exception as e:
        logging.error("Error in validating client password by email in DB "+str(e))
        raise 

def checkClientPasswordByEmailDB(dataObj):
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()
        sql = "SELECT password from registration WHERE email='{}'".format(dataObj['email'])

        mycursor.execute(sql)
        result=mycursor.fetchall()
        cnx.close()
        return result
    except Exception as e:
        logging.error("Error in checking client password by email in DB "+str(e))
        raise 


