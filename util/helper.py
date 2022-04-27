import time

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from config import constants


def scroll(driver):
    """Scrolls down till the bottom of the page"""
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(constants.Timeout.SCROLL_PAUSE_TIMEOUT)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def scroll_down_to_element(driver, element):
    """Scrolls down till the specified element is visible"""
    try:
        driver.execute_script("argument[0].scrollTop = 200", element)
    except Exception as e:
        print('error scrolling down to web element', e)


def wait_for_element_to_be_visible(driver, element):
    try:
        WebDriverWait(driver, constants.Timeout.LARGE_TIMEOUT).until(ec.visibility_of_element_located(element))
    except Exception as e:
        print(f'element {element} not found, {e}')


def scroll_up_to_element(driver, element):
    """Scrolls up till the specified element is visible"""
    element_location = None
    try:
        element_location = element.location["y"]
    except Exception:
        return False
    element_location = element_location - 130
    if element_location < 0:
        element_location = 0
    scroll_script = "window.scrollTo(0, %s);" % element_location
    try:
        driver.execute_script(scroll_script)
        return True
    except Exception:
        return False


def wait_until_alert_is_present(driver, element):
    # Wait for alert to appear
    try:
        WebDriverWait(driver, constants.Timeout.SMALL_TIMEOUT).until(ec.alert_is_present())
    except Exception as e:
        print(f'element {element} not found', {e})


def wait_sometime():
    try:
        time.sleep(10)
    except:
        pass

def wait_for_element_to_be_clicked(driver, element):
    # wait for element to appear
    try:
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable(element)).click()
    except:
        pass


def wait_for_element_presence(driver,element):
    try:
        WebDriverWait(driver, 20).until(ec.presence_of_element_located(element))
    except:
        pass


testData = {}


def addTestData(key, value):
    testData[key] = value


def getTestData(key):
    return testData[key]
