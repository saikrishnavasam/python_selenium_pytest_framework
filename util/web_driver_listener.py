import datetime
import logging
from selenium.webdriver.support.events import AbstractEventListener

log_filename = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
logging.basicConfig(
    filename=f"./logs/{log_filename}.log",
    format="%(asctime)s: %(levelname)s: %(message)s",
    level=logging.INFO
)


class WebDriverListner(AbstractEventListener):
    def __init__(self):
        self.logger = logging.getLogger()

    def before_navigate_to(self, url, driver):
        self.logger.info(f"Navigating to {url}")

    def after_navigate_to(self, url, driver):
        self.logger.info(f"Navigating to {url}")

    def before_find(self, by, value, driver):
        self.logger.info(f"Searching for element by {by} {value}")

    def after_find(self, by, value, driver):
        self.logger.info(f"Element by {by} {value} found")

    def before_click(self, element, driver):
        if element.get_attribute("test") is None:
            self.logger.info(f"Clicking on {element.get_attribute('class')}")
        else:
            self.logger.info(f"Clicking on {element.get_attribute('text')}")

    def after_click(self, element, driver):
        if element.get_attribute("test") is None:
            self.logger.info(f"Clicked {element.get_attribute('class')}")
        else:
            self.logger.info(f"Clicked  {element.get_attribute('text')}")

    def before_change_value_of(self, element, driver):
        self.logger.info(f"{element.get_attribute('text')} value changed")

    def before_quit(self, driver):
        self.logger.info("Driver quitting")

    def after_quit(self, driver):
        self.logger.info("Driver quit")

    def on_exception(self, exception, driver):
        self.logger.error(exception)
