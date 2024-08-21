import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\karim.belboukhari\Project51\Configurations\conf.ini")

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
    
