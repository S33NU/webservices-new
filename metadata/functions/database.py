from metadata.functions.metadata import connectToDatabase


def validateCookieDB(cookie):
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()
        sql = "SELECT phonenumber from registration WHERE phonenumber='{}'".format(cookie)

        mycursor.execute(sql)
        result=mycursor.fetchall()
        
        if len(result) == 0:
            sql = "SELECT email from registration WHERE email='{}'".format(cookie)
            mycursor.execute(sql)
            result=mycursor.fetchall()
            cnx.close()
            if len(result) == 0:
                return False 
            elif len(result) != 0:
                return True        
        elif len(result) != 0:
            cnx.close()
            return True
    except Exception as e:
        logging.error("Error in validating Cookie DB "+str(e))
        raise    

def validateClientOTPByEmailDB(dataObj):
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()
        sql = "SELECT email,password from registration WHERE email_otp='"+dataObj['otp']+"' and email = '{}'".format(dataObj['email'])

        mycursor.execute(sql)
        result=mycursor.fetchall()
        cnx.close()
        return result
    except Exception as e:
        logging.error("Error in validating client password by email in DB "+str(e))
        raise 
