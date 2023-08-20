from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    BURGER_MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOG_OUT = (By.LINK_TEXT, "Logout")
    ALL_ITEMS = (By.LINK_TEXT, "All Items")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
    NUM_OF_PROD_IN_CART = (By.CLASS_NAME, "shopping_cart_badge")
    REMOVE_BTN = (By.XPATH, "//button[starts-with(@id, 'remove')]")
    TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def wait_for_clickable(self, locator):
        return self._wait.until(EC.element_to_be_clickable(locator))

    def click_log_out(self):
        self.find(self.BURGER_MENU_BTN).click()
        self.wait_for_clickable(self.LOG_OUT).click()

    def click_all_items(self):
        self.find(self.BURGER_MENU_BTN).click()
        self.wait_for_clickable(self.ALL_ITEMS).click()

    def click_shopping_cart(self):
        self.find(self.SHOPPING_CART).click()

    def wait_for(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))

    def get_title(self):
        return self.find(self.TITLE).text

    def get_number_of_products_in_cart(self):
        return self.wait_for(self.NUM_OF_PROD_IN_CART).text

    def wait_for_all(self, locator):
        return self._wait.until(EC.presence_of_all_elements_located(locator))

    def find_remove_btns(self):
        return self.find_all(self.REMOVE_BTN)

    def remove_all_from_cart(self):
        for btn in self.wait_for_all(self.REMOVE_BTN):
            btn.click()
