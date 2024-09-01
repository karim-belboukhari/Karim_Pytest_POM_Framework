from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

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
        try:
            element = self.driver.find_element(By.XPATH, self.textbox_email)
            element.clear()
            element.send_keys(email)
        except NoSuchElementException:
            return "Username input field not found"
    
    def set_password(self, password):
        """Locate the password input field, clear it, and enter the provided password."""
        try:
            element = self.driver.find_element(By.XPATH, self.textbox_password)
            element.clear()
            element.send_keys(password)
        except NoSuchElementException:
            return "Password input field not found"
    
    def click_login(self):
        """Click the login button."""
        try:
            self.driver.find_element(By.XPATH, self.login_CTA).click()
        except NoSuchElementException:
            return "Login button not found"
        except TimeoutException:
            return "Timed out waiting for login button to be clickable"
    
    def click_logout(self):
        """Click the logout button."""
        try:
            self.driver.find_element(By.XPATH, self.logout_CTA).click()
            self.driver.find_element(By.XPATH, self.final_logout).click()
        except NoSuchElementException:
            return "Logout button not found"
        except TimeoutException:
            return "Timed out waiting for logout button to be clickable"
    
    def get_invalid_credentials_error(self):
        """Retrieve the error message for invalid credentials."""
        try:
            error_message = self.driver.find_element(By.XPATH, self.Invalid_credentials).text
            return error_message
        except NoSuchElementException:
            return "Error message element not found"
    
    def get_empty_username_error(self):
        """Retrieve the error message for empty username."""
        try:
            error_message = self.driver.find_element(By.XPATH, self.empty_username).text
            return error_message
        except NoSuchElementException:
            return "Empty username error element not found"
    
    def get_empty_password_error(self):
        """Retrieve the error message for empty password."""
        try:
            error_message = self.driver.find_element(By.XPATH, self.empty_password).text
            return error_message
        except NoSuchElementException:
            return "Empty password error element not found"
    
    def is_login_button_visible(self):
        """Check if the login button is visible."""
        try:
            return self.driver.find_element(By.XPATH, self.login_CTA).is_displayed()
        except NoSuchElementException:
            return False
    
    def is_logout_button_visible(self):
        """Check if the logout button is visible."""
        try:
            return self.driver.find_element(By.XPATH, self.logout_CTA).is_displayed()
        except NoSuchElementException:
            return False


