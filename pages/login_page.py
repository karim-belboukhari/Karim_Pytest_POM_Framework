from selenium.webdriver.common.by import By

class Login:
    # Define XPaths for the elements
    textbox_email = '//*[@name ="username"]'
    textbox_password = '//*[@name="password"]' 
    login_CTA = "//*[@type='submit']"
    logout_CTA = "//*[@class='oxd-userdropdown-name']"
    final_logout = "//*[@role='menuitem' and text()='Déconnexion' or text()='Logout']"
    Invalid_credentials = "//*[text()='Invalid credentials' or text()='Informations d’identification non valides']"
    empty_username = "//*[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message' and text()='Required' or text()='Obligatoire']"
    empty_password = "//*[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message' and text()='Required' or text()='Obligatoire']"
    
    def __init__(self, driver):
        self.driver = driver
    
    def set_username(self, email):
        """Locate the username input field, clear it, and enter the provided email."""
        element = self.driver.find_element(By.XPATH, self.textbox_email)
        element.clear()
        element.send_keys(email)
    
    def set_password(self, password):
        """Locate the password input field, clear it, and enter the provided password."""
        element = self.driver.find_element(By.XPATH, self.textbox_password)
        element.clear()
        element.send_keys(password)
    
    def click_login(self):
        """Click the login button."""
        self.driver.find_element(By.XPATH, self.login_CTA).click()
    
    def click_logout(self):
        """Click the logout button."""
        self.driver.find_element(By.XPATH, self.logout_CTA).click()
        self.driver.find_element(By.XPATH, self.final_logout).click()
    
    def get_invalid_credentials_error(self):
        """Retrieve the error message for invalid credentials."""
        return self.driver.find_element(By.XPATH, self.Invalid_credentials).text
    
    def get_empty_username_error(self):
        """Retrieve the error message for empty username."""
        return self.driver.find_element(By.XPATH, self.empty_username).text
    
    def get_empty_password_error(self):
        """Retrieve the error message for empty password."""
        return self.driver.find_element(By.XPATH, self.empty_password).text
    
    def is_login_button_visible(self):
        """Check if the login button is visible."""
        return self.driver.find_element(By.XPATH, self.login_CTA).is_displayed()
    
    def is_logout_button_visible(self):
        """Check if the logout button is visible."""
        return self.driver.find_element(By.XPATH, self.logout_CTA).is_displayed()
