from selenium.webdriver.common.by import By
from pages.log_in_page import BasePage


class CheckoutInfoPage(BasePage):
    FORM_FIRST_NAME = (By.NAME, "firstName")
    FORM_LAST_NAME = (By.NAME, "lastName")
    FORM_POSTAL_CODE = (By.NAME, "postalCode")
    CONTINUE_BTN = (By.NAME, "continue")

    def enter_first_name(self, uniq_first_name):
        first_name_field = self.find(self.FORM_FIRST_NAME)
        first_name_field.clear()
        first_name_field.send_keys(uniq_first_name)

    def enter_last_name(self, uniq_last_name):
        last_name_field = self.find(self.FORM_LAST_NAME)
        last_name_field.clear()
        last_name_field.send_keys(uniq_last_name)

    def enter_postal_code(self, uniq_postcode):
        postal_code_field = self.find(self.FORM_POSTAL_CODE)
        postal_code_field.clear()
        postal_code_field.send_keys(uniq_postcode)

    def click_continue(self):
        self.find(self.CONTINUE_BTN).click()
