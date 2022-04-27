import json
import os
import time
import pytest
import selenium
from py.xml import html
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from config import constants
from util import download_helper
from util.dbinteraction import DatabaseManager
from util.web_driver_listener import WebDriverListner

baseurl = None
driver = None

@pytest.fixture
def data():
    with open('testdata/testdata.json') as val:
        test_data = json.load(val)
    return test_data


@pytest.fixture(scope='session', autouse=True)
def setup(request) -> EventFiringWebDriver:
    options = Options()
    prefs = {'download.default_directory': download_helper.get_downloads_folder()}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("ignore-certificate-errors")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--disable-gpu")
    global driver
    driver = EventFiringWebDriver(selenium.webdriver.Chrome(constants.WebdriverPath.CHROMEDRIVER, options=options),WebDriverListner())
    driver.implicitly_wait(constants.Timeout.IMPLICIT_WAIT_TIMEOUT)
    download_helper.create_downloads_folder()
    driver.maximize_window()
    driver.set_page_load_timeout(constants.Timeout.PAGE_LOAD_TIMEOUT)
    driver.get(getBaseUrl(request))
    yield driver
    driver.quit()
    return driver


# @pytest.fixture(scope='session')
# def db_setup():
#     db_instance = DatabaseManager()
#     yield db_instance
#     db_instance.close_db()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_name = "Test_Execution_Summary.html"
    create_folder(os.getcwd() + "/reports")
    config.option.htmlpath = os.getcwd() + "/reports/" + report_name


@pytest.hookimpl(tryfirst=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.h1("Automation Report(UI and API Tests")])


@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = "Test Automation Report"


#@pytest.mark.hookwrapper
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    report.error_message = ''
    setattr(item, "rep" + report.when, report)
    report.error_message = str(call.excinfo.value) if call.excinfo else ""
    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = get_current_test_name() + '_' + time.strftime('%y%m%d_%H%M%S') + ".png"
            _capture_screenshot(file_name)

            if file_name:
                html_scr = '<div><img src = "./screenshots/%s" alt = "screnshot" style="width:600px;height:228px;" onclick ="window.open(this.src)" align ="right"/></div>'%file_name  # file_name
                extra.append(pytest_html.extras.html(html_scr))
        report.extra = extra


def pytest_addoption(parser):
    parser.addoption(
        '--env',
        action='store',
        dest='environment',
        type=str.lower,
        choices=(
            constants.Environment.DEV,
            constants.Environment.QA,
            constants.Environment.UAT

        ),
        default=constants.Environment.QA
    )


def getBaseUrl(request):
    env = request.config.getoption('environment')
    if constants.Environment.DEV == env:
        baseurl = constants.URL.DEV
    elif constants.Environment.QA == env:
        baseurl = constants.URL.QA
    elif constants.Environment.UAT == env:
        baseurl = constants.URL.UAT
    else:
        baseurl = constants.URL.QA
    return baseurl


def get_current_test_name():
    name = os.environ.get('PYTEST_CURRENT_TEST').split('::')
    test_case_name = name[-1].split(' ')
    return test_case_name[0]


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        try:
            os.mkdir(folder_path)
        except Exception:
            pass


def _capture_screenshot(name):
    create_folder(os.getcwd() + "/reports/screenshots")
    if driver is not None:
        driver.get_screenshot_as_file(os.getcwd() + "/reports/screenshots/" + name)
    else:
        pass


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    env = session.config.getoption('environment')
    session.config._metadata['Environment'] = env.upper()
    # session.config._metadat['DB Server'] = constants.DBConnect.SERVER
