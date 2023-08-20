def test_sorting(logged_in_inventory_page):
    logged_in_inventory_page.verify_sort_name_z_to_a()
    logged_in_inventory_page.verify_sort_name_a_to_z()
    logged_in_inventory_page.verify_sort_price_low_to_high()
    logged_in_inventory_page.verify_sort_price_high_to_low()


def test_add_all_to_cart(logged_in_inventory_page):
    logged_in_inventory_page.add_all_to_cart()
    assert "6" in logged_in_inventory_page.get_number_of_products_in_cart()


def test_remove_all_from_cart(logged_in_inventory_page):
    logged_in_inventory_page.add_all_to_cart()
    logged_in_inventory_page.remove_all_from_cart()
    assert logged_in_inventory_page.find_add_to_cart_btns
