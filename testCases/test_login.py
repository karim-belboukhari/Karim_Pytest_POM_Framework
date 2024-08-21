
from selenium.webdriver.common.by import By
from pageObjects.loginpage import Login
from Utilites.readproperties import Readconfig
from Utilites.customlogger import Logenerator
import pytest

class Test_Login:
    
    email=Readconfig.getemail()
    password=Readconfig.getpassword()
    logger = Logenerator.log_gen()
     
    @pytest.mark.Sanity   
    def test_log(self,setup):
        
        self.logger.info("***************verifying the logging page****************")
        
        driver = setup
        login= Login(driver)
        login.set_username(self.email)
        login.set_password(self.password)
        login.click_log()
        if driver.title == "OrangeHRM":
            assert True
            self.logger.info("***************logging page passed****************")
        else:
            driver.save_screenshot(r"C:\Users\karim.belboukhari\Project51\Screenshots\myimage.png")
            self.logger.info("***************logging page failed****************")
            assert False
            
            