from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.inventory_page import InventoryPage


def test_continue_shopping_from_cart(logged_in_inventory_page, driver):
    logged_in_inventory_page.add_backpack_to_cart()
    logged_in_inventory_page.click_shopping_cart()

    cart_page = CartPage(driver)
    cart_page.click_continue_shopping()

    inventory_page = InventoryPage(driver)
    inventory_page.verify_remove_backpack_from_cart_present()


def test_continue_shopping_from_checkout_info(logged_in_inventory_page, driver):
    logged_in_inventory_page.add_backpack_to_cart()
    logged_in_inventory_page.click_shopping_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_info_page = CheckoutInfoPage(driver)
    checkout_info_page.click_all_items()

    inventory_page = InventoryPage(driver)
    inventory_page.verify_remove_backpack_from_cart_present()


def test_continue_shopping_from_checkout_overview(
    logged_in_inventory_page, driver, uniq_first_name, uniq_last_name, uniq_postcode
):
    logged_in_inventory_page.add_backpack_to_cart()
    logged_in_inventory_page.click_shopping_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_info_page = CheckoutInfoPage(driver)
    checkout_info_page.enter_first_name(uniq_first_name)
    checkout_info_page.enter_last_name(uniq_last_name)
    checkout_info_page.enter_postal_code(uniq_postcode)
    checkout_info_page.click_continue()

    checkout_overview_page = CheckoutOverviewPage(driver)
    checkout_overview_page.click_cancel()

    inventory_page = InventoryPage(driver)
    inventory_page.verify_remove_backpack_from_cart_present()


def test_continue_shopping_from_checkout_complete(
    logged_in_inventory_page, driver, uniq_first_name, uniq_last_name, uniq_postcode
):
    logged_in_inventory_page.add_backpack_to_cart()
    logged_in_inventory_page.click_shopping_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_info_page = CheckoutInfoPage(driver)
    checkout_info_page.enter_first_name(uniq_first_name)
    checkout_info_page.enter_last_name(uniq_last_name)
    checkout_info_page.enter_postal_code(uniq_postcode)
    checkout_info_page.click_continue()

    checkout_overview_page = CheckoutOverviewPage(driver)
    checkout_overview_page.click_finish()

    checkout_complete_page = CheckoutCompletePage(driver)
    checkout_complete_page.click_back_home()

    assert logged_in_inventory_page.find_add_to_cart_btns
