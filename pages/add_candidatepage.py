from selenium.webdriver.common.by import By


class AddCandidate:
    #locators
    recuitement_flow = "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']"
    add_cta= "//*[@type='button' and @class='oxd-button oxd-button--medium oxd-button--secondary']"
    firstname= "//*[@name='firstName']"
    lastname= "//*[@name='lastName']"
    vacancy_Role_select= "//*[@class='oxd-select-text--after']/child::i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']"
    email="//label[text()='Email']/following::input[@placeholder='Type here'][1]"
    contact="//label[text()='Contact Number']/following::input[@placeholder='Type here'][1]"
    date_triger= '//*[@class="oxd-icon bi-calendar oxd-date-input-icon"]'
    date_piker= "//*[@class='oxd-input oxd-input--active' and @placeholder='yyyy-dd-mm']"
    notes="//*[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']"
    checkboxConsent="//*[@class='oxd-checkbox-input oxd-checkbox-input--active --label-right oxd-checkbox-input']"
    save_candidate="//*[@type='submit' and @class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"
    
    
    def __init__(self, driver):
        self.driver = driver
    #the methodes
    def set_candidate(self):
        self.driver.find_element(By.XPATH, self.recuitement_flow).click()
        self.driver.find_element(By.XPATH, self.add_cta).click()
    def set_firstname(self, name):
        self.driver.find_element(By.XPATH, self.firstname).clear()
        self.driver.find_element(By.XPATH, self.firstname).send_keys(name)
    def set_lastname(self, name2):
        self.driver.find_element(By.XPATH, self.lastname).clear()
        self.driver.find_element(By.XPATH, self.lastname).send_keys(name2)
    def set_v_role(self, expected_Role):
        self.driver.find_element(By.XPATH, self.vacancy_Role_select).click()
        
        option_element = self.driver.find_elements(By.XPATH, "//*[@role='listbox' and @class='oxd-select-dropdown --positon-bottom']/div/span")
        for role in option_element:
            if role.text == expected_Role:
                role.click()
                break
            
    def set_email(self, emails): 
        self.driver.find_element(By.XPATH, self.email).send_keys(emails)
    def set_contact_number(self, contact_Number):
        self.driver.find_element(By.XPATH, self.contact).send_keys(contact_Number)
    def set_datepiker(self, date):
        self.driver.find_element(By.XPATH, self.date_piker).clear()
        self.driver.find_element(By.XPATH, self.date_piker).send_keys(date)
    def set_note(self,rand_note):
        self.driver.find_element(By.XPATH, self.notes).send_keys(rand_note)
    def set_checkbox(self):
        self.driver.find_element(By.XPATH, self.checkboxConsent).click()
    def Save_candidate(self):
        self.driver.find_element(By.XPATH, self.save_candidate).click()
        
     

            
        
  
        
