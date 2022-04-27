from selenium.webdriver.common.by import By


class LoginPageLocators:
    username = (By.XPATH, "//input[@id='user-nam']")
    password = (By.XPATH, "//input[@id='password']")
    login_button = (By.XPATH, "//input[@id='login-button']")
    login_logo = (By.XPATH, "//input[@value='Login']")
    products_logo = (By.XPATH, "//span[text()='Products']")


class ProductPageLocators:
    products_logo = (By.XPATH, "//span[@class='title' and text() = 'Products']")
    product = (By.XPATH, "//div[@class='inventory_item_name' and text() = 'Sauce Labs Backpack']")
    add_to_cart = (By.XPATH, "//button[text()='Add to cart']")
    back_to_products = (By.XPATH, "//button[@id='back-to-products']")
    login_logo = (By.XPATH, "//div[@class='inventory_details_price']")


class ShoppingCartPageLocators:
    cart_button = (By.XPATH, "//a[@class='shopping_cart_link']")
    cart_page_title = (By.XPATH, "//span[@class='title']")
    product = (By.XPATH, "//div[@class='inventory_item_name' and text() = 'Sauce Labs Backpack']")
    checkout_button = (By.XPATH, "//button[@id='checkout']")


class CheckoutPageLocators:
    first_name = (By.XPATH, "//input[@id='first-name']")
    last_name = (By.XPATH, "//input[@id='last-name']")
    continue_button = (By.XPATH, "//input[@name='continue']")
    product = (By.XPATH, "//div[@class='inventory_item_name']")
    finish_button = (By.XPATH, "//button[@name='finish']")
    checkout_complete = (By.XPATH, "//span[@class='title']")
