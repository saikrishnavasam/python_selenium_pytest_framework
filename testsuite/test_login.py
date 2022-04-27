"""
This is a login page
"""
import logging

import pytest

from pages.login_page import LoginPage

@pytest.mark.regression
@pytest.mark.smoke
class TestLogin:

    def test_home_page(self, setup, data):
        """This method verifies that user is landed on login"""
        logging.info('---test home page started---')
        login_page = LoginPage(setup)
        assert login_page.verify_home_page() == True
        logging.info('---test home page ended---')

    def test_user_login(self, setup, data):
        """ Verify that user is able to log in """
        logging.info('---test_user_login started---')
        login_page = LoginPage(setup)
        assert login_page.verify_login() == data['PRODUCT_PAGE_TXT']
        logging.info('---test_user_login ended---')
