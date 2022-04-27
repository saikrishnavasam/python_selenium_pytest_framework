import logging
import time

from selenium.common.exceptions import StaleElementReferenceException

from pages.locators import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = LoginPageLocators
        # self.test_data = data

    def verify_home_page(self):
        return self.driver.find_element(*LoginPageLocators.login_logo).is_displayed()

    def verify_login(self):
        try:
            self.driver.find_element(*LoginPageLocators.username).send_keys('standard_user')
            self.driver.find_element(*LoginPageLocators.password).send_keys('secret_sauce')
            self.driver.find_element(*LoginPageLocators.login_button).click()
        except StaleElementReferenceException:
            pass
        return self.driver.find_element(*LoginPageLocators.products_logo).text




