import pytest
from selenium.webdriver.common.by import By
from  test_pages.test_drop_down_page import Dropdownpage

@pytest.mark.usefixtures("init_driver")
class TestDropDownPage:

    def test_drop_down_page(self):
        # Step 1: Open the URL
        self.driver.get("https://www.saucedemo.com/")

        # Step 2: Perform login first to access the dropdownpage
        from test_pages.test_login_page import LoginPage
        login_page = LoginPage(self.driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        # Step 3: Create an dropdownPage object
        dropdown_page = Dropdownpage(self.driver)

        # Step 4: Select the "Price (low to high)" option from the dropdown
        dropdown_page.select_sort_option("Price (low to high)")

        # Step 5: Add assertion to verify that the sorting option is applied correctly
        # (This could be checking that the items are sorted or some visible UI change)
        selected_option = self.driver.find_element(By.XPATH,"//select[@class='product_sort_container']/option[@value='lohi']")
        assert selected_option.is_selected()

        # Optionally, verify that prices appear sorted (this requires capturing product prices and verifying order)
