from dashboard.functions.database import saveDashboardDB,dashboardData
import logging

def saveDashboardService(data):
    try:
        saveDashboardDB(data)
    except Exception as e:
        logging.error("Error in saving dashboard " + str(e))
        raise

def dashboardService():
    try:
        data = dashboardData()
        temp = []
        for i in data:
            prof = {
                'ID': i[0],
                "invested": i[1],
                "currentValue": i[2],
                "gainPer": i[3],
                "gainAmount": i[4],
                "advised": i[5]
            }
            temp.append(prof)
        return temp
    except Exception as msg:
        logging.error('Error in getting Profiles' + str(msg))
        raise