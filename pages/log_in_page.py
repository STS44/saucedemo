from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LogInPage(BasePage):
    URL = "https://www.saucedemo.com/"
    FORM_USERNAME = (By.NAME, "user-name")
    FORM_PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.NAME, "login-button")
    ERR_MSG = (By.XPATH, "//div[contains(@class, 'error-message')]/h3")

    def enter_username(self, username):
        username_field = self.find(self.FORM_USERNAME)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.find(self.FORM_PASSWORD)
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        self.find(self.LOGIN_BTN).click()

    def is_url_matches(self):
        return self.driver.current_url == self.URL

    def verify_err_msg(self):
        assert (
            "Epic sadface: Sorry, this user has been locked out"
            in self.find(self.ERR_MSG).text
        )
