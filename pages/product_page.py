import time

from selenium.common.exceptions import StaleElementReferenceException

from pages.locators import ProductPageLocators
from util.helper import wait_for_element_to_be_visible


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = ProductPageLocators
        # self.test_data = data

    def verify_product_page(self):
        return self.driver.find_element(*ProductPageLocators.products_logo).text

    def add_product_to_cart(self):
        try:
            self.driver.find_element(*ProductPageLocators.product).click()
        except StaleElementReferenceException:
            pass
        try:
            self.driver.find_element(*ProductPageLocators.add_to_cart).click()
        except StaleElementReferenceException:
            pass
        try:
            self.driver.find_element(*ProductPageLocators.back_to_products).click()
        except StaleElementReferenceException:
            pass
        return self.verify_product_page()
