from selenium.webdriver.common.by import By

class SocialProfilePage:
    def __init__(self, driver):
        self.driver = driver

    # Locators for social profile links
    twitter_link = (By.XPATH, "//a[normalize-space()='Twitter']")
    facebook_link = (By.XPATH, "//a[normalize-space()='Facebook']")
    linkedin_link = (By.XPATH, "//a[normalize-space()='LinkedIn']")

    # Actions on the page
    def open_twitter(self):
        self.driver.find_element(*self.twitter_link).click()

    def open_facebook(self):
        self.driver.find_element(*self.facebook_link).click()

    def open_linkedin(self):
        self.driver.find_element(*self.linkedin_link).click()

    # Handle window switching
    def switch_to_window(self, window_index):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[window_index])

    def close_additional_windows(self, start_index=1):
        """Closes all browser windows starting from the specified index."""
        window_handles = self.driver.window_handles
        windows_to_close = window_handles[start_index:]
        for window_handle in windows_to_close:
            self.driver.switch_to.window(window_handle)
            self.driver.close()

    def switch_to_main_window(self):
        """Switch back to the main window (index 0)."""
        self.switch_to_window(0)
