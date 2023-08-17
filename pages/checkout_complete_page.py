from selenium.webdriver.common.by import By
from pages.log_in_page import BasePage


class CheckoutCompletePage(BasePage):
    BACK_HOME_BTN = (By.ID, "back-to-products")

    def click_back_home(self):
        self.find(self.BACK_HOME_BTN).click()
