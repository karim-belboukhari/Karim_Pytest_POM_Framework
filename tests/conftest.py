import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities.read_properties import ReadConfig
from selenium.webdriver.chrome.options import Options

@pytest.fixture(params=["chrome", "firefox", "edge"], scope="function")
def setup(request):
    driver = None
    browser = request.param
    
    # Initialize WebDriver based on the requested browser
    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    elif browser == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    try:
        url = ReadConfig.get_url()  # Ensure ReadConfig.get_url() returns a valid URL
        driver.get(url)
        driver.implicitly_wait(10)  # Set implicit wait
        yield driver
    finally:
        driver.quit()  # Quit the driver to close the browser

######### HTML Reports ###########

def pytest_html_report_title(report):
    report.title = "Login Page Testing Report"

@pytest.hookimpl(tryfirst=True)
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

@pytest.hookimpl(tryfirst=True)
def pytest_html_results_summary(prefix):
    prefix.append('<div class="custom-summary-header"><h2>Test Overview</h2></div>')

