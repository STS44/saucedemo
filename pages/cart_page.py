from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.log_in_page import BasePage


class CartPage(BasePage):
    REMOVE_BTN_FOR_RED_T_SHIRT = (By.NAME, "remove-test.allthethings()-t-shirt-(red)")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")
    CHECKOUT_BTN = (By.ID, "checkout")

    def click_remove_red_t_shirt(self):
        self.find(self.REMOVE_BTN_FOR_RED_T_SHIRT).click()

    def verify_red_t_shirt_not_exist(self):
        try:
            self.find(self.REMOVE_BTN_FOR_RED_T_SHIRT)
            print("The element exists")
        except NoSuchElementException:
            print("The element does not exist")

    def click_continue_shopping(self):
        self.find(self.CONTINUE_SHOPPING_BTN).click()

    def click_checkout(self):
        self.find(self.CHECKOUT_BTN).click()
