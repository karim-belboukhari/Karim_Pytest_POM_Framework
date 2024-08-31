
from selenium.webdriver.common.by import By
from pageObjects.loginpage import Login
from Utilites.readproperties import Readconfig
from Utilites.customlogger import Logenerator
import pytest
import os
import allure

@allure.severity(allure.severity_level.BLOCKER)
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
        login.click_login()
        if driver.title == "OrangeHRM":
            assert True
            self.logger.info("***************logging page passed****************")
        else:
            test_name = request.node.name
            screen = os.path.join(os.path.dirname(__file__), '..', 'Screenshots', f'{test_name}.png')
            driver.save_screenshot(screen)
            self.logger.info("***************logging page failed****************")
            assert False
    def test_invalid_login(self,setup, request):
            self.logger.info("***************verifying the logging page****************")
        
            driver = setup
            login= Login(driver)
            login.set_username("invalid_username")
            login.set_password("invalid_password")
            login.click_login()
            
            
            
            
            if driver.title == "OrangeHRMs":
                
                self.logger.info("***************logging page Failed****************")
                test_name = request.node.name
                screen = os.path.join(os.path.dirname(__file__), '..', 'Screenshots', f'{test_name}.png')
                driver.save_screenshot(screen)
                assert False
            else:
                assert True
                test_name = request.node.name
                screen = os.path.join(os.path.dirname(__file__), '..', 'Screenshots', f'{test_name}.png')
                driver.save_screenshot(screen)
                with open(screen, "rb") as image_file:
                    allure.attach(image_file.read(), name=f'Screenshot for {test_name}',  attachment_type=allure.attachment_type.PNG) 
                self.logger.info("***************logging page passed****************")
                
        
        
        
        
        
        
        
        
        
       
    #def test_login_with_empty_fields(self,setup):
        #pass 
    #def test_login_with_empty_Username(self,setup):
        #pass
    #def test_login_with_empty_password(self,setup):
        #pass  
    #def test_login_with_max_length_username(self,setup):
       # pass 
    #def test_existing_functionality(self,setup):
       # pass        