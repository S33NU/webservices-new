import logging
import configparser
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