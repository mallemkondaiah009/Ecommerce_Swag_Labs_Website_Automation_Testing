import pytest
from selenium.webdriver.common.by import By
from test_pages.test_logout_page import LogoutPage  # Ensure correct path

@pytest.mark.usefixtures("init_driver")
class TestProfilePage:

    def test_open_menu_and_logout(self):
        # Step 1: Open the URL
        self.driver.get("https://www.saucedemo.com/")

        # Step 2: Perform login
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()

        # Step 3: Create a LogoutPage object
        logout_page = LogoutPage(self.driver)

        # Step 4: Open the menu and click logout
        logout_page.open_menu()
        logout_page.click_logout()

        # Step 5: Add an assertion to check successful logout (back to login page)
        assert "login" in self.driver.current_url, "Logout was not successful"
