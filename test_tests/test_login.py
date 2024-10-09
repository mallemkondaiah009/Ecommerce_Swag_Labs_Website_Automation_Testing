import pytest
from test_pages.test_login_page import LoginPage  # Ensure correct import path


@pytest.mark.usefixtures("init_driver")
class TestLogin:

    def test_login(self):
        # Step 1: Open the URL
        self.driver.get("https://www.saucedemo.com/")

        # Step 2: Create a LoginPage object
        login_page = LoginPage(self.driver)

        # Step 3: Perform login actions
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        # Step 4: Add an assertion to verify login success (e.g., checking the URL or title)
        assert "inventory" in self.driver.current_url
