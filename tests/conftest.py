import pytest
from selenium import webdriver
from utilities.read_properties import ReadConfig
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException

@pytest.fixture(params=["chrome", "firefox", "edge"], scope="function")
def setup(request):
    driver = None
    browser = request.param
    
    # Initialize WebDriver based on the requested browser
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    try:
        url = ReadConfig.get_url()  # Ensure Readconfig.geturl() returns a valid URL
        driver.get(url)
        driver.implicitly_wait(10)  # Set implicit wait
        yield driver
    finally:
        driver.quit()  # Quit the driver to close the browser

######### HTML Reports ###########

def pytest_html_report_title(report):
    report.title = "Login Page Testing Report"

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    # Customize the environment information here
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
    metadata.pop('Platform', None)
    metadata.pop('Packages', None)
    metadata.pop('Python', None)
    
    metadata['Project Name'] = 'ecommerce'
    metadata['Module Name'] = 'customers'
    metadata['Tester'] = 'Karim'

@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.append('<div class="custom-summary-header"><h2>Test Overview</h2></div>')

    
