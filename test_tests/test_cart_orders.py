import pytest
from test_pages.test_order_page import OrderPage


@pytest.mark.usefixtures("init_driver")
class TestCheckoutPage:

    def test_checkout_process(self):
        # Step 1: Open the URL
        self.driver.get("https://www.saucedemo.com/")

        # Step 2: Perform login to proceed to the checkout
        from test_pages.test_login_page import LoginPage
        login_page = LoginPage(self.driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()


        # Step 4: Create a CheckoutPage object and perform the checkout actions
        checkout_page = OrderPage(self.driver)
        checkout_page.go_to_cart()
        checkout_page.click_checkout()
        checkout_page.enter_first_name("Zoro")
        checkout_page.enter_last_name("Roronoa")
        checkout_page.enter_postal_code("524134")
        checkout_page.click_continue()
        checkout_page.click_finish()

        # Step 5: Add assertion to verify the order completion
        assert "checkout-complete" in self.driver.current_url
