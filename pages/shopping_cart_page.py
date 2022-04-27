from selenium.common.exceptions import StaleElementReferenceException

from pages.locators import ShoppingCartPageLocators


class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = ShoppingCartPageLocators
        # self.test_data = data



    def verify_cart_page(self):
        try:
            self.driver.find_element(*ShoppingCartPageLocators.cart_button).click()
        except StaleElementReferenceException:
            pass
        try:
            return self.driver.find_element(*ShoppingCartPageLocators.cart_page_title).text
        except StaleElementReferenceException:
            pass

    def verify_product_in_cart(self):
        return self.driver.find_element(*ShoppingCartPageLocators.product).text

    def checkout(self):
        try:
            self.driver.find_element(*ShoppingCartPageLocators.checkout_button).click()
        except StaleElementReferenceException:
            pass
