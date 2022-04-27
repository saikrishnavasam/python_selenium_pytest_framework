import logging

from pages.product_page import ProductPage


class TestProduct:
    def test_verify_product_page(self, setup, data):
        """This method verifies that product page is displayed after login"""
        logging.info('---test_verify_product_page started---')
        product_page = ProductPage(setup)
        assert product_page.verify_product_page() == data['PRODUCT_PAGE_TXT']
        logging.info('---test_verify_product_page ended---')

    def test_add_product_to_cart(self, setup,data):
        """Verifies add to cart functionality"""
        logging.info('---test_add_product_to_cart started---')
        product_page = ProductPage(setup)
        assert product_page.add_product_to_cart() == data['PRODUCT_PAGE_TXT']
        logging.info('---test_add_product_to_cart ended---')
