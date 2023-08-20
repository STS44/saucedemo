from pages.cart_page import CartPage


def test_calculate_total_quantity(logged_in_inventory_page, driver):
    logged_in_inventory_page.add_all_to_cart()
    logged_in_inventory_page.click_shopping_cart()
    cart_page = CartPage(driver)
    cart_page.click_remove_red_t_shirt()
    cart_page.verify_red_t_shirt_not_exist()
    assert "5" in cart_page.get_number_of_products_in_cart()
