from pages.log_in_page import LogInPage
from pages.inventory_page import InventoryPage


def test_log_in(driver, username, password):
    log_in_page = LogInPage(driver)
    log_in_page.enter_username(username)
    log_in_page.enter_password(password)
    log_in_page.click_login()
    inventory_page = InventoryPage(driver)
    assert "Products" in inventory_page.get_title()


def test_log_out(logged_in_inventory_page, driver):
    logged_in_inventory_page.click_log_out()
    log_in_page = LogInPage(driver)
    log_in_page.is_url_matches()


def test_lock_out(driver, locked_out_username, password):
    log_in_page = LogInPage(driver)
    log_in_page.enter_username(locked_out_username)
    log_in_page.enter_password(password)
    log_in_page.click_login()
    log_in_page.verify_err_msg()
