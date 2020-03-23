import mysql.connector
import logging
from mysql.connector import errorcode
from personal_profile.functions.metadata import getConfig


def connectToDatabase():
    try:
        config = getConfig()
        sqldb_config = config['sqldb_config']
        cnx = mysql.connector.connect(user=sqldb_config['user'], password=sqldb_config['password'],
                                      host=sqldb_config['host'],
                                      database=sqldb_config['database'])
        return cnx
    except Exception as err:
        logging.error("Error in connecting to database " + str(err))
        raise


def connectToDatabase2():
    try:
        config = getConfig()
        sqldb_config = config['sqldb_config_2']
        cnx = mysql.connector.connect(user=sqldb_config['user'], password=sqldb_config['password'],
                                      host=sqldb_config['host'],
                                      database=sqldb_config['database'])
        return cnx
    except Exception as err:
        logging.error("Error in connecting to database " + str(err))
        raise

def saveDashboardDB(dataObj):
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()

        sql = "INSERT INTO dashboard(invested, currentvalue, gainper, gainamount, advised) VALUES (%s, %s,%s, %s,%s)"

        val = (dataObj['invested'], dataObj['currentValue'], dataObj['gainPer'], dataObj['gainAmount'],
               dataObj['advised'])

        mycursor.execute(sql, val)

        cnx.commit()

        cnx.close()
    except Exception as e:
        logging.error("Error in saving Personal Profile " + str(e))
        raise

def dashboardData():
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()

        mycursor.execute("SELECT * FROM dashboard;")

        allprofiles = mycursor.fetchall()

        return allprofiles
    except Exception:
        raise