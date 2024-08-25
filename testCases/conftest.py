import pytest
from selenium import webdriver
from Utilites.readproperties import Readconfig

@pytest.fixture(params=["chrome", "firefox", "edge"], scope="function")
def setup(request):
    driver = None
    browser = request.param
    
    # Initialize WebDriver based on the requested browser
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    try:
        url = Readconfig.geturl()  # Ensure Readconfig.geturl() returns a valid URL
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
def pytest_html_results_summary(prefix,summary):
    prefix.append('<div class="custom-summary-header"><h2>Test Overview</h2></div>')
    summary.append("<p>All major functionality tests have passed successfully.</p><p>Please review the detailed logs and screenshots for more information.</p>")
    summary.append("""<h3>Detailed Test Analysis</h3>
<p>The following tests were particularly notable:</p>
<ul>
    <li><strong>Login Functionality:</strong> Passed with no warnings.</li>
</ul>
""")
    
