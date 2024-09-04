from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

class AddCandidate:
    # Locators
    recuitement_flow = "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']"
    add_cta = "//*[@type='button' and @class='oxd-button oxd-button--medium oxd-button--secondary']"
    firstname = "//*[@name='firstName']"
    lastname = "//*[@name='lastName']"
    vacancy_Role_select = "//*[@class='oxd-select-text--after']/child::i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']"
    email = "//label[text()='Email']/following::input[@placeholder='Type here'][1]"
    contact = "//label[text()='Contact Number']/following::input[@placeholder='Type here'][1]"
    date_triger = '//*[@class="oxd-icon bi-calendar oxd-date-input-icon"]'
    date_piker = "//*[@class='oxd-input oxd-input--active' and @placeholder='yyyy-dd-mm']"
    notes = "//*[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']"
    checkboxConsent = "//*[@class='oxd-checkbox-input oxd-checkbox-input--active --label-right oxd-checkbox-input']"
    register_candidate = "//*[@type='submit' and @class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"

    def __init__(self, driver):
        self.driver = driver

    def set_candidate(self):
        """
        Navigates to the recruitment module and clicks on the 'Add' button to start adding a new candidate.
        """
        try:
            self.driver.find_element(By.XPATH, self.recuitement_flow).click()
            self.driver.find_element(By.XPATH, self.add_cta).click()
        except (NoSuchElementException, TimeoutException) as e:
            raise WebDriverException("Failed to click on the recruitment flow or add button.") from e

    def set_firstname(self, name):
        """
        Sets the first name of the candidate.
        """
        try:
            firstname_field = self.driver.find_element(By.XPATH, self.firstname)
            firstname_field.clear()
            firstname_field.send_keys(name)
        except (NoSuchElementException, TimeoutException) as e:
            raise WebDriverException("Failed to set the first name.") from e

    def set_lastname(self, name2):
        """
        Sets the last name of the candidate.
        """
        try:
            lastname_field = self.driver.find_element(By.XPATH, self.lastname)
            lastname_field.clear()
            lastname_field.send_keys(name2)
        except (NoSuchElementException, TimeoutException) as e:
            raise WebDriverException("Failed to set the last name.") from e

    def set_v_role(self, expected_Role):
        """
        Selects the role from the dropdown list.
        """
        try:
            self.driver.find_element(By.XPATH, self.vacancy_Role_select).click()
            option_element = self.driver.find_elements(By.XPATH, "//*[@role='listbox' and @class='oxd-select-dropdown --positon-bottom']/div/span")
            for role in option_element:
                if role.text == expected_Role:
                    role.click()
                    break
        except (NoSuchElementException, TimeoutException) as e:
            raise WebDriverException("Failed to select the role from the dropdown.") from e

    def set_email(self, emails):
        """
        Sets the email address of the candidate.
        """
        try:
            self.driver.find_element(By.XPATH, self.email).send_keys(emails)
        except (NoSuchElementException, TimeoutException) as e:
            raise WebDriverException("Failed to set the email address.") from e

    def set_contact_number(self, contact_Number):
        """
        Sets the contact number of the candidate.
        """
        try:
            self.driver.find_element(By.XPATH, self.contact).send_keys(contact_Number)
        except (NoSuchElementException, TimeoutException) as e:
            raise WebDriverException("Failed to set the contact number.") from e

    def set_datepiker(self, date):
        """
        Sets the date in the date picker field.
        """
        try:
            date_picker_field = self.driver.find_element(By.XPATH, self.date_piker)
            date_picker_field.clear()
            date_picker_field.send_keys(date)
        except (NoSuchElementException, TimeoutException) as e:
            raise WebDriverException("Failed to set the date in the date picker.") from e

    def set_note(self, rand_note):
        """
        Sets the notes for the candidate.
        """
        try:
            self.driver.find_element(By.XPATH, self.notes).send_keys(rand_note)
        except (NoSuchElementException, TimeoutException) as e:
            raise WebDriverException("Failed to set the notes.") from e

    def set_checkbox(self):
        """
        Clicks on the consent checkbox to agree to the terms.
        """
        try:
            self.driver.find_element(By.XPATH, self.checkboxConsent).click()
        except (NoSuchElementException, TimeoutException) as e:
            raise WebDriverException("Failed to click the consent checkbox.") from e

    def save_candidate(self):
        
        """
        Clicks the save button to submit the candidate's details.
        """
        try:
            self.driver.find_element(By.XPATH, self.register_candidate).click()
        except (NoSuchElementException, TimeoutException) as e:
            raise WebDriverException("Failed to click the save button.") from e

