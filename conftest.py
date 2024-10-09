import pytest
from selenium import webdriver
import os
import datetime

# Create a screenshots directory if it doesn't exist
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

@pytest.fixture(params=["chrome", "firefox", "edge"], scope="class")
def init_driver(request):
    global driver
    if request.param == "chrome":
        from selenium.webdriver.chrome.service import Service
        driver_path = "Browsers/chromedriver.exe"
        driver = webdriver.Chrome(service=Service(driver_path))
    elif request.param == "firefox":
        from selenium.webdriver.firefox.service import Service
        driver_path = "Browsers/geckodriver.exe"
        driver = webdriver.Firefox(service=Service(driver_path))
    elif request.param == "edge":
        from selenium.webdriver.edge.service import Service
        driver_path = "Browsers/msedgedriver.exe"
        driver = webdriver.Edge(service=Service(driver_path))

    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()

# Hook to take a screenshot on test failure
def pytest_runtest_makereport(item, call):
    if call.excinfo is not None:  # Check if the test failed
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = f"screenshots/{item.name}_{timestamp}.png"
        item.instance.driver.save_screenshot(screenshot_name)
        print(f"Screenshot saved to {screenshot_name}")
