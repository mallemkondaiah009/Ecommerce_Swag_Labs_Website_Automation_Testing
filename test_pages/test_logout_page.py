from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds for elements

    # Page Elements (locators)
    burger_menu_button = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    logout_button = (By.XPATH, "//a[@id='logout_sidebar_link']")

    # Actions on the page
    def open_menu(self):
        # Wait until the menu button is clickable and click it
        self.wait.until(EC.element_to_be_clickable(self.burger_menu_button)).click()

    def click_logout(self):
        # Wait until the logout button is clickable and click it
        self.wait.until(EC.element_to_be_clickable(self.logout_button)).click()
