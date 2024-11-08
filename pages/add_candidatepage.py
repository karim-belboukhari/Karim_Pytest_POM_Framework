from selenium.webdriver.common.by import By

class AddCandidate:
    # Locators
    recruitment_flow = "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']"
    add_cta = "//*[@type='button' and @class='oxd-button oxd-button--medium oxd-button--secondary']"
    firstname = "//*[@name='firstName']"
    lastname = "//*[@name='lastName']"
    vacancy_Role_select = "//*[@class='oxd-select-text--after']/child::i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']"
    email = "//label[text()='Email']/following::input[@placeholder='Type here'][1]"
    contact = "//label[text()='Contact Number']/following::input[@placeholder='Type here'][1]"
    date_trigger = '//*[@class="oxd-icon bi-calendar oxd-date-input-icon"]'
    date_picker = "//*[@class='oxd-input oxd-input--active' and @placeholder='yyyy-dd-mm']"
    notes = "//*[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']"
    checkboxConsent = "//*[@class='oxd-checkbox-input oxd-checkbox-input--active --label-right oxd-checkbox-input']"
    register_candidate = "//*[@type='submit' and @class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"

    def __init__(self, driver):
        self.driver = driver

    def set_candidate(self):
        """
        Navigates to the recruitment module and clicks on the 'Add' button to start adding a new candidate.
        """
        self.driver.find_element(By.XPATH, self.recruitment_flow).click()
        self.driver.find_element(By.XPATH, self.add_cta).click()

    def set_firstname(self, name):
        """
        Sets the first name of the candidate.
        """
        firstname_field = self.driver.find_element(By.XPATH, self.firstname)
        firstname_field.clear()
        firstname_field.send_keys(name)

    def set_lastname(self, name2):
        """
        Sets the last name of the candidate.
        """
        lastname_field = self.driver.find_element(By.XPATH, self.lastname)
        lastname_field.clear()
        lastname_field.send_keys(name2)

    def set_v_role(self, expected_Role):
        """
        Selects the role from the dropdown list.
        """
        self.driver.find_element(By.XPATH, self.vacancy_Role_select).click()
        option_elements = self.driver.find_elements(By.XPATH, "//*[@role='listbox' and @class='oxd-select-dropdown --positon-bottom']/div/span")
        for role in option_elements:
            if role.text == expected_Role:
                role.click()
                break

    def set_email(self, emails):
        """
        Sets the email address of the candidate.
        """
        self.driver.find_element(By.XPATH, self.email).send_keys(emails)

    def set_contact_number(self, contact_Number):
        """
        Sets the contact number of the candidate.
        """
        self.driver.find_element(By.XPATH, self.contact).send_keys(contact_Number)

    def set_datepicker(self, date):
        """
        Sets the date in the date picker field.
        """
        date_picker_field = self.driver.find_element(By.XPATH, self.date_picker)
        date_picker_field.clear()
        date_picker_field.send_keys(date)

    def set_note(self, rand_note):
        """
        Sets the notes for the candidate.
        """
        self.driver.find_element(By.XPATH, self.notes).send_keys(rand_note)

    def set_checkbox(self):
        """
        Clicks on the consent checkbox to agree to the terms.
        """
        self.driver.find_element(By.XPATH, self.checkboxConsent).click()

    def save_candidate(self):
        """
        Clicks the save button to submit the candidate's details.
        """
        self.driver.find_element(By.XPATH, self.register_candidate).click()
