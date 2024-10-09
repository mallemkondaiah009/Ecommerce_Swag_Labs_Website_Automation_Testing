from selenium.webdriver.common.by import By

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    # Page Elements (locators)
    cart_link = (By.CLASS_NAME, "shopping_cart_link")
    checkout_button = (By.ID, "checkout")
    first_name_input = (By.ID, "first-name")
    last_name_input = (By.ID, "last-name")
    postal_code_input = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")
    back_to_products_button = (By.ID, "back-to-products")

    # Actions on the page
    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def click_finish(self):
        self.driver.find_element(*self.finish_button).click()

    def click_back_to_products(self):
        self.driver.find_element(*self.back_to_products_button).click()
