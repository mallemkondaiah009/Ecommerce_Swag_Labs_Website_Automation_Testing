from selenium.webdriver.common.by import By

class Cartpage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_id):
        add_to_cart_button = (By.XPATH, f"//button[@id='add-to-cart-{product_id}']")
        self.driver.find_element(*add_to_cart_button).click()
