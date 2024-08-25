import configparser
import os

CONFIG_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'Configurations', 'conf.ini')
config = configparser.RawConfigParser()
config.read(CONFIG_FILE_PATH)

class Readconfig:
    def geturl():
        url = config.get("common info", "link")
        return url
    
    def getemail():
        email = config.get("common info", "email")
        return email
    
    def getpassword():
        password = config.get("common info", "password")
        return password
    
