import logging

from pages.shopping_cart_page import ShoppingCartPage


class TestShoppingCart:
    def test_verify_product_page(self, setup, data):
        """This method verifies that product page is displayed after login"""
        logging.info('---test_verify_product_page started---')
        cart_page = ShoppingCartPage(setup)
        assert cart_page.verify_cart_page() == data['CART_PAGE_TXT']
        logging.info('---test_verify_product_page ended---')

    def test_add_product_to_cart(self, setup,data):
        """Verifies add to cart functionality"""
        logging.info('---test_add_product_to_cart started---')
        cart_page = ShoppingCartPage(setup)
        assert cart_page.verify_product_in_cart() == data['PRODUCT_NAME']
        cart_page.checkout()
        logging.info('---test_add_product_to_cart ended---')