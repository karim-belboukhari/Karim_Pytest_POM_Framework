
from selenium.webdriver.common.by import By
from pageObjects.loginpage import Login
from Utilites.readproperties import Readconfig
from Utilites.customlogger import Logenerator
import pytest
import os


class Test_Login:
    
    email=Readconfig.getemail()
    password=Readconfig.getpassword()
    logger = Logenerator.log_gen()
     
    @pytest.mark.Sanity   
    def test_valid_login(self,setup, request):
        
        self.logger.info("***************verifying the logging page****************")
        
        driver = setup
        login= Login(driver)
        login.set_username(self.email)
        login.set_password(self.password)
        login.click_log()
        if driver.title == "OrangeHRsM":
            assert True
            self.logger.info("***************logging page passed****************")
        else:
            test_name = request.node.name
            screen = os.path.join(os.path.dirname(__file__), '..', 'Screenshots', f'{test_name}.png')
            driver.save_screenshot(screen)
            self.logger.info("***************logging page failed****************")
            assert False
    def test_invalid_login(self,setup):
        pass       
    def test_login_with_empty_fields(self,setup):
        pass 
    def test_login_with_max_length_username(self,setup):
        pass 
    def test_existing_functionality(self,setup):
        pass        