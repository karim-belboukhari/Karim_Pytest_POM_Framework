import configparser
import os

CONFIG_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'config', 'conf.ini')
config = configparser.RawConfigParser()
config.read(CONFIG_FILE_PATH)

class ReadConfig:
    def get_url():
        url = config.get("common info", "link")
        return url
    
    def get_email():
        email = config.get("common info", "email")
        return email
    
    def get_password():
        password = config.get("common info", "password")
        return password
    
