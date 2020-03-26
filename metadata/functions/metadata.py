import logging
import configparser
import mysql.connector
from mysql.connector import errorcode
import http.client
def getConfig():
    try:
        config = configparser.ConfigParser()
        config.read('D:\Production_files\config\webservicesconfig.ini')
        return config
    except Exception as e:
        raise 

def configureLogging(logConfig):
    try:
        logging.basicConfig(filename=logConfig['dir_path']+'webservice.log',
                        level=logConfig.getint('level'), format=logConfig['format'], datefmt=logConfig['date_format'])
        
    except Exception as e:
        raise   

def connectToDatabase():
    try:
        config=getConfig()
        sqldb_config = config['sqldb_config']
        cnx = mysql.connector.connect(user=sqldb_config['user'], password=sqldb_config['password'],
                              host=sqldb_config['host'],
                              database=sqldb_config['database'])
        return cnx
    except Exception as err:
        logging.error("Error in connecting to database "+str(err))
        raise 
    
def getOTP(mobile_number):
    try:
        config=getConfig()
        otp_config = config['OTP_CONFIG']
        conn = http.client.HTTPSConnection("api.msg91.com")

        headers = { 'content-type': "application/json" }
        url = "/api/v5/otp?authkey="+otp_config['auth_key']+"&template_id="+otp_config['send_otp_template_id']+"&extra_param=%7B%22OTP%22%3A%2212390%22%7D&mobile="+mobile_number
        conn.request("GET",url, headers=headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))
    
    except Exception as err:
        logging.error("Error in getting OTP")
        raise
    
def verifyOTP(mobile_number,otp):
    try:
        config=getConfig()
        otp_config = config['OTP_CONFIG']
        conn = http.client.HTTPSConnection("api.msg91.com")

        payload = ""

        url = "/api/v5/otp/verify?mobile="+mobile_number+"&otp="+otp+"&authkey="+otp_config['auth_key']       
    
        conn.request("POST", url, payload)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))
    except Exception as e:
        logging.error("Error in verifyting OTP "+str(e))