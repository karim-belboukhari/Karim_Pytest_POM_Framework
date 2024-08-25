from pageObjects.loginpage import Login
from pageObjects.add_candidatepage import Add_Candidate
from Utilites.customlogger import Logenerator
from Utilites.readproperties import Readconfig
import time
from selenium.webdriver.common.by import By
import random
import string
import pytest
import os

class Test_Add_Candidate:
   
   email= Readconfig.getemail()
   password=Readconfig.getpassword()
   loggin= Logenerator.log_gen()
   screen2 = os.path.join(os.path.dirname(__file__), '..', 'Screenshots', 'addUser.png')
   @pytest.mark.Sanity
   def test_addcandidate(self, setup):
       self.loggin.info("***********************test_addcandidate started**********************")
       driver = setup
       Lp = Login(driver)
       Lp.set_username(self.email)
       Lp.set_password(self.password)
       Lp.click_log()
       self.loggin.info("***********************logging passed**********************")
       AddCand = Add_Candidate(driver)
       AddCand.set_candidate()
       AddCand.set_firstname("karim")
       AddCand.set_lastname("belboukhari")
       AddCand.set_V_role("Senior QA Lead")
       self.emaill = random_generator() +"@gmail.com"
       AddCand.set_email(self.emaill)
       time.sleep(3)
       #AddCand.set_datepiker("2023-26-08")
       AddCand.set_note("Test for the note section")
       AddCand.set_checkbox()
       AddCand.Save_candidate()
       time.sleep(5)
       expectedresult = "karim belboukhari"
       
       expectedfild = driver.find_element(By.XPATH, "//*[@class='oxd-grid-3 orangehrm-full-width-grid']/div[1]/div[1]/div[2]/child::p")
    
       print(expectedfild.text)
       if expectedfild.text == expectedresult :
           
           assert True
           self.loggin.info("***********************test_addcandidate Passed**********************")
       else:
           driver.save_screenshot("Screenshots\\addUser.png")
           self.loggin.info("***********************test_addcandidate Failed **********************")
           assert False

def random_generator(size=8, chars= string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))