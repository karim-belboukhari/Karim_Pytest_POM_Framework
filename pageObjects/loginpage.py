from selenium.webdriver.common.by import By


class Login:
    
    textbox_email= '//*[@name ="username"]'
    textbox_password = '//*[@name="password"]' 
    login_CTA= "//*[@type='submit']"
    logout_CTA="//*[@class='oxd-userdropdown-name']"
    final_logout="//*[@role='menuitem' and text()='Déconnexion' or text()='Logout']"
    
    def __init__(self, driver):
        self.driver = driver
    
    def set_username(self, email):
        self.driver.find_element(By.XPATH, self.textbox_email).clear()
        self.driver.find_element(By.XPATH, self.textbox_email).send_keys(email)
    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password).clear()
        self.driver.find_element(By.XPATH, self.textbox_password).send_keys(password)
    def click_log(self):
        self.driver.find_element(By.XPATH, self.login_CTA).click() 
    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_CTA).click()
        self.driver.find_element(By.XPATH, self.final_logout).click()    
        
        
        
        

