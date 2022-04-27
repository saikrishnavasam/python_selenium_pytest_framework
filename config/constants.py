class Environment:
    QA = 'qa'
    DEV = 'dev'
    UAT = 'uat'


class WebdriverPath:
    CHROMEDRIVER = 'resources/chromedriver.exe'


class URL:
    QA = 'https://www.saucedemo.com/'
    DEV = 'https://'
    UAT = 'https://'


class Files:
    DOWNLOADS_FOLDER = 'downloaded_files'


class DB_Queries:
    "Write your db queries here"


class Timeout:
    IMPLICIT_WAIT_TIMEOUT = 15
    SCROLL_PAUSE_TIMEOUT = 0.5
    PAGE_LOAD_TIMEOUT = 10
    LARGE_TIMEOUT = 3600
    MIN_TIMEOUT = 2
    SMALL_TIMEOUT = 5
