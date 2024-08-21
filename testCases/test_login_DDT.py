
from selenium.webdriver.common.by import By
from pageObjects.loginpage import Login
from Utilites.readproperties import Readconfig
from Utilites.customlogger import Logenerator
from Utilites import XLUtils
import time
import pytest


class Test_Login_DDT:
    
    path = r"C:\Users\karim.belboukhari\Project51\TestData\loginData.xlsx"
    logger = Logenerator.log_gen()
      
    @pytest.mark.regression
    def test_log_DDT(self,setup):
        self.logger.info("***************test_log_DDT****************")
        self.logger.info("***************verifying the logging page DDT test****************")
        
        driver = setup
        login= Login(driver)
        
        rows = XLUtils.getRowCount(self.path, "Sheet1")
        print(f"this is the number of rows: {rows}")
        
        lst_status =[]
        
        for r in range(2, rows +1):
            user = XLUtils.readData(self.path,"Sheet1", r, 1 )
            password = XLUtils.readData(self.path,"Sheet1", r , 2)
            exp = XLUtils.readData(self.path,"Sheet1", r , 3)
            
            login.set_username(user)
            login.set_password(password)
            login.click_log()
            time.sleep(3)
            
            actual_url= driver.current_url
            expected_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
            
            if actual_url == expected_url:
                if exp == "Pass":
                    self.logger.info("*********************Passed*******************")
                    login.click_logout()
                    lst_status.append("Pass")
                elif exp == "Fail":
                    self.logger.info("*********************Fail*******************")
                    login.click_logout()
                    lst_status.append("Fail")
            elif actual_url != expected_url:
                if exp == "Fail":
                    self.logger.info("*********************Passed*******************")
                    lst_status.append("Pass")
                elif exp == "Pass":
                    self.logger.info("*********************Fail*******************")
                    lst_status.append("Fail")
        if "Fail" not in lst_status:
            self.logger.info("*************************Login DDT Test Passed **************************")
            assert True
        else:
            self.logger.info("*************************Login DDT Test Failed **************************")
            assert False
        self.logger.info("*********************End of test_log_DDT*********************")               
        self.logger.info("*************** completed the Test_Login_DDT ****************")            
                    

        
        
        
        
        
        
        
        
            
            