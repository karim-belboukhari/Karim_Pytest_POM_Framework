
from selenium.webdriver.common.by import By
from pages.login_page import Login
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LoggingGenerator
import pytest
import os
import allure
import time

@allure.severity(allure.severity_level.BLOCKER)
class TestLogin:
    
    email=ReadConfig.get_email()
    password=ReadConfig.get_password()
    logger = LoggingGenerator.log_gen()
     
    @pytest.mark.Sanity 
    def test_valid_login(self,setup, request):
        
        self.logger.info("***************verifying the test_valid_login****************")
        
        driver = setup
        login= Login(driver)
        login.set_username(self.email)
        login.set_password(self.password)
        login.click_login()
        if driver.title == "OrangeHRM":
            assert True
            self.logger.info("***************test_valid_login passed****************")
        else:
            test_name = request.node.name
            screenshots_path = os.path.join(os.path.dirname(__file__), '..', 'screenshots', f'{test_name}.png')
            time.sleep(2)
            driver.save_screenshot(screenshots_path)
            self.logger.info("***************test_valid_login failed****************")
            assert False
    def test_invalid_login(self,setup, request):
        
        
        self.logger.info("***************verifying the test_invalid_login****************")
        
        driver = setup
        login= Login(driver)
        login.set_username("invalid_username")
        login.set_password("invalid_password")
        login.click_login()
        
        invalid_credentials_error = login.get_invalid_credentials_error()
        
        if invalid_credentials_error == "Invalid credentials" or "Informations d’identification non valides":
            assert True
            self.logger.info("***************test_invalid_login passed****************")
        else:
            self.logger.info("***************test_invalid_login failed****************")
            test_name = request.node.name
            screenshots = os.path.join(os.path.dirname(__file__), '..', 'screenshots', f'{test_name}.png')
            time.sleep(2)
            driver.save_screenshot(screenshots)
            with open(screenshots, "rb") as image_file:
                allure.attach(image_file.read(), name=f'Screenshot for {test_name}',  attachment_type=allure.attachment_type.PNG)
            assert False
                
      
    def test_login_with_empty_fields(self,setup, request):
        self.logger.info("***************verifying the test_login_with_empty_fields****************")
        
        driver = setup
        login= Login(driver)
        login.set_username("")
        login.set_password("")
        login.click_login()
        
        empty_username_error = login.get_empty_username_error()
        empty_password_error = login.get_empty_password_error()
        
        if (empty_username_error in ["Required", "Obligatoire"]) and (empty_password_error in ["Required", "Obligatoire"]):
            
            assert True
            self.logger.info("***************test_login_with_empty_fields passed****************")
        else:
            self.logger.info("***************test_login_with_empty_fields failed****************")
            test_name = request.node.name
            screenshots = os.path.join(os.path.dirname(__file__), '..', 'screenshots', f'{test_name}.png')
            time.sleep(2)
            driver.save_screenshot(screenshots)
            with open(screenshots, "rb") as image_file:
                allure.attach(image_file.read(), name=f'Screenshot for {test_name}',  attachment_type=allure.attachment_type.PNG)
            assert False

    
    
    
    
    
    
    
    
    
     
    #def test_login_with_empty_Username(self,setup):
        #pass
    #def test_login_with_empty_password(self,setup):
        #pass  
    #def test_login_with_max_length_username(self,setup):
       # pass 
    #def test_existing_functionality(self,setup):
       # pass        