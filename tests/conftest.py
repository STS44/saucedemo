import pytest
from selenium.webdriver import Chrome
from pages.log_in_page import LogInPage
from pages.inventory_page import InventoryPage
from utils.utils import get_rand_first_name, get_rand_last_name, get_rand_postcode


@pytest.fixture
def driver():
    driver = Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@pytest.fixture
def username():
    return "standard_user"


@pytest.fixture(scope="session")
def password():
    return "secret_sauce"


@pytest.fixture
def locked_out_username():
    return "locked_out_user"


@pytest.fixture
def logged_in_inventory_page(driver, username, password):
    log_in_page = LogInPage(driver)
    log_in_page.enter_username(username)
    log_in_page.enter_password(password)
    log_in_page.click_login()
    inventory_page = InventoryPage(driver)
    return inventory_page


@pytest.fixture
def uniq_first_name():
    return get_rand_first_name()


@pytest.fixture
def uniq_last_name():
    return get_rand_last_name()


@pytest.fixture
def uniq_postcode():
    return get_rand_postcode()
