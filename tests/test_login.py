
from selenium.webdriver.common.by import By
from pages.login_page import Login
from utilites.read_properties import ReadConfig
from utilites.custom_logger import LoggingGenerator
import pytest
import os
import allure

@allure.severity(allure.severity_level.BLOCKER)
class Test_Login:
    
    email=ReadConfig.get_email()
    password=ReadConfig.get_password()
    logger = LoggingGenerator.log_gen()
     
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
            screenshots_path = os.path.join(os.path.dirname(__file__), '..', 'screenshots', f'{test_name}.png')
            driver.save_screenshot(screenshots_path)
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
                screenshots_path_2 = os.path.join(os.path.dirname(__file__), '..', 'screenshots', f'{test_name}.png')
                driver.save_screenshot(screenshots_path_2)
                assert False
            else:
                assert True
                test_name = request.node.name
                screenshots_path_3 = os.path.join(os.path.dirname(__file__), '..', 'screenshots', f'{test_name}.png')
                driver.save_screenshot(screenshots_path_3)
                with open(screenshots_path_3, "rb") as image_file:
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