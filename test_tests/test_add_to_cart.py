import pytest
from selenium.webdriver.common.by import By
from test_pages.test_login_page import LoginPage
from test_pages.test_cart_page import Cartpage

@pytest.mark.usefixtures("init_driver")
class TestAddToCart:
    def test_login_and_add_to_cart(self):
        # Step 1: Open the URL
        self.driver.get("https://www.saucedemo.com/")

        # Step 2: Create a LoginPage object
        login_page = LoginPage(self.driver)

        # Step 3: Perform login actions
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        # Step 4: Create a Cartpage object
        cart_page = Cartpage(self.driver)

        # Step 5: List of products to add
        products_to_add = [
            "sauce-labs-backpack",
            "sauce-labs-bike-light",
            "sauce-labs-bolt-t-shirt",
            "sauce-labs-fleece-jacket",
            "sauce-labs-onesie",
            "test.allthethings()-t-shirt-(red)"
        ]

        # Step 6: Add products to the cart
        for product in products_to_add:
            cart_page.add_to_cart(product)

        # Step 7: Add an assertion to verify the number of items in the cart
        cart_count = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert int(cart_count) == len(products_to_add), f"Expected {len(products_to_add)} items in cart, but got {cart_count}."
