from selenium.webdriver.common.by import By
from pages.log_in_page import BasePage


class CheckoutOverviewPage(BasePage):
    TOTAL_PRICE_WITHOUT_TAX = (By.CLASS_NAME, "summary_subtotal_label")
    CANCEL_BTN = (By.ID, "cancel")
    FINISH_BTN = (By.NAME, "finish")

    def verify_total_price_calc_without_tax(self):
        assert "$129.94" in self.find(self.TOTAL_PRICE_WITHOUT_TAX).text

    def click_cancel(self):
        self.find(self.CANCEL_BTN).click()

    def click_finish(self):
        self.find(self.FINISH_BTN).click()
