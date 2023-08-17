from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage


def test_checkout(
    logged_in_inventory_page, driver, uniq_first_name, uniq_last_name, uniq_postcode
):
    logged_in_inventory_page.add_all_to_cart()
    logged_in_inventory_page.click_shopping_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_info_page = CheckoutInfoPage(driver)
    checkout_info_page.enter_first_name(uniq_first_name)
    checkout_info_page.enter_last_name(uniq_last_name)
    checkout_info_page.enter_postal_code(uniq_postcode)
    checkout_info_page.click_continue()

    checkout_overview_page = CheckoutOverviewPage(driver)
    checkout_overview_page.verify_total_price_calc_without_tax()
    assert "6" in checkout_overview_page.get_number_of_products_in_cart()
