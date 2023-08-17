from selenium.webdriver.common.by import By
from pages.log_in_page import BasePage
from selenium.webdriver.support.select import Select


class InventoryPage(BasePage):
    PRODUCT_SORT = (By.CLASS_NAME, "product_sort_container")
    FIRST_ITEM_NAME = (
        By.CSS_SELECTOR,
        ".inventory_list :first-child :nth-child(2) :first-child a :only-child",
    )
    LAST_ITEM_NAME = (
        By.CSS_SELECTOR,
        ".inventory_list :last-child :nth-child(2) :first-child a :only-child",
    )
    FIRST_ITEM_PRICE = (
        By.CSS_SELECTOR,
        ".inventory_list :first-child :nth-child(2) div.pricebar :first-child",
    )
    LAST_ITEM_PRICE = (
        By.CSS_SELECTOR,
        ".inventory_list :last-child :nth-child(2) div.pricebar :first-child",
    )
    ADD_TO_CART_BTN = (By.XPATH, "//button[starts-with(@id, 'add-to-cart')]")
    ADD_TO_CART_BTN_FOR_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BTN_FOR_BACKPACK = (By.ID, "remove-sauce-labs-backpack")

    def verify_sort_name_z_to_a(self):
        Select(self.find(self.PRODUCT_SORT)).select_by_visible_text("Name (Z to A)")
        assert (
            "Test.allTheThings() T-Shirt (Red)" in self.find(self.FIRST_ITEM_NAME).text
        )
        assert "Sauce Labs Backpack" in self.find(self.LAST_ITEM_NAME).text

    def verify_sort_name_a_to_z(self):
        Select(self.find(self.PRODUCT_SORT)).select_by_visible_text("Name (A to Z)")
        assert "Sauce Labs Backpack" in self.find(self.FIRST_ITEM_NAME).text
        assert (
            "Test.allTheThings() T-Shirt (Red)" in self.find(self.LAST_ITEM_NAME).text
        )

    def verify_sort_price_low_to_high(self):
        Select(self.find(self.PRODUCT_SORT)).select_by_visible_text(
            "Price (low to high)"
        )
        assert "$7.99" in self.find(self.FIRST_ITEM_PRICE).text
        assert "$49.99" in self.find(self.LAST_ITEM_PRICE).text

    def verify_sort_price_high_to_low(self):
        Select(self.find(self.PRODUCT_SORT)).select_by_visible_text(
            "Price (high to low)"
        )
        assert "$49.99" in self.find(self.FIRST_ITEM_PRICE).text
        assert "$7.99" in self.find(self.LAST_ITEM_PRICE).text

    def add_all_to_cart(self):
        for btn in self.find_all(self.ADD_TO_CART_BTN):
            btn.click()

    def add_backpack_to_cart(self):
        self.find(self.ADD_TO_CART_BTN_FOR_BACKPACK).click()

    def verify_remove_backpack_from_cart_present(self):
        assert self.find(self.REMOVE_BTN_FOR_BACKPACK)

    def find_add_to_cart_btns(self):
        self.find_all(self.ADD_TO_CART_BTN)
