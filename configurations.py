import configparser
import base64

def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config
def getpassword():
    pwd = 'mypassword@123'
    printdecode = base64.b64decode(pwd)
    return printdecode