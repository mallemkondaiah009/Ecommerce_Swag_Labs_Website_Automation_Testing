from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Dropdownpage:
    def __init__(self, driver):
        self.driver = driver

    # Page Elements (locators)
    sort_dropdown = (By.XPATH, "//select[@class='product_sort_container']")

    # Actions on the page
    def select_sort_option(self, option_text):
        dropdown_element = self.driver.find_element(*self.sort_dropdown)
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text(option_text)
