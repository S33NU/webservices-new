import logging
import configparser
import mysql.connector
from mysql.connector import errorcode
import http.client
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def getConfig():
    try:
        config = configparser.ConfigParser()
        config.read('D:\Production_files\config\webservicesconfig.ini')
        return config
    except Exception as e:
        raise


def configureLogging(logConfig):
    try:
        logging.basicConfig(filename=logConfig['dir_path'] + 'webservice.log',
                            level=logConfig.getint('level'), format=logConfig['format'],
                            datefmt=logConfig['date_format'])

    except Exception as e:
        raise


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


def getOTP(mobile_number):
    try:
        config = getConfig()
        otp_config = config['OTP_CONFIG']
        conn = http.client.HTTPSConnection("api.msg91.com")

        headers = {'content-type': "application/json"}
        # %7B%22OTP%22%3A%2212390%22%7D
        url = "/api/v5/otp?authkey=" + otp_config['auth_key'] + "&template_id=" + otp_config[
            'send_otp_template_id'] + "&extra_param=&mobile=" + mobile_number
        conn.request("GET", url, headers=headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))

    except Exception as err:
        logging.error("Error in getting OTP")
        raise


def verifyOTP(mobile_number, otp):
    try:
        config = getConfig()
        otp_config = config['OTP_CONFIG']
        conn = http.client.HTTPSConnection("api.msg91.com")

        payload = ""

        url = "/api/v5/otp/verify?mobile=" + mobile_number + "&otp=" + otp + "&authkey=" + otp_config['auth_key']

        conn.request("POST", url, payload)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))
        return data.decode("utf-8")
    except Exception as e:
        logging.error("Error in verifyting OTP " + str(e))


def getOTPByEmail(email):
    try:
        config = getConfig()
        otp_config = config['OTP_CONFIG']
        conn = http.client.HTTPSConnection("api.msg91.com")

        headers = {'content-type': "application/json"}
        # %7B%22OTP%22%3A%2212390%22%7D
        url = "/api/v5/otp?authkey=" + otp_config['auth_key'] + "&template_id=" + otp_config[
            'send_otp_template_id'] + "&extra_param=&mobile=&email="+email
        conn.request("GET", url, headers=headers)

        res = conn.getresponse()
        data = res.read()

        #print(data.decode("utf-8"))

    except Exception as err:
        logging.error("Error in getting OTP")
        raise


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def getOTPByEmail(email_to,otp):
    try:
        
        config = getConfig()
        email_otp_config = config['EMAIL_OTP_CONFIG']
        
        sender_email = email_otp_config['sender']
        #password = getpass.getpass('Sender Password: ')    
        receiver_email = email_to
        message = MIMEMultipart("alternative")
        message["Subject"] =  email_otp_config['subject']
        message["From"] = sender_email
        message["To"] = receiver_email
        part1 = MIMEText(email_otp_config['email_body']+" "+str(otp), "plain")
        message.attach(part1)    
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(email_otp_config['host'], email_otp_config.getint('port'), context=context) as server:
            server.login(sender_email, email_otp_config['password'])
            server.sendmail(sender_email, receiver_email, message.as_string())
        
    except Exception as e:
        logging.error("Error in sending OTP via email to "+email_to+" "+str(e))
        raise