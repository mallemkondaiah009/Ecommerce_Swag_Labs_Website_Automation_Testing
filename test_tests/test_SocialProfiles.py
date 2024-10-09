import pytest
from test_pages.test_social_profile_page import SocialProfilePage

@pytest.mark.usefixtures("init_driver")
class TestSocialProfile:

    def test_social_profile_links(self):
        # Step 1: Open the URL
        self.driver.get("https://www.saucedemo.com/")

        # Step 2: Perform login to access social profile links
        from test_pages.test_login_page import LoginPage
        login_page = LoginPage(self.driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        # Step 3: Create a SocialProfilePage object
        social_profile_page = SocialProfilePage(self.driver)

        # Step 4: Open Twitter, Facebook, and LinkedIn
        social_profile_page.open_twitter()
        social_profile_page.switch_to_main_window()  # Switch back to main window

        social_profile_page.open_facebook()
        social_profile_page.switch_to_main_window()  # Switch back to main window

        social_profile_page.open_linkedin()
        social_profile_page.switch_to_main_window()  # Switch back to main window

        # Step 5: Close additional windows (social media windows)
        social_profile_page.close_additional_windows()

        # Add assertion to verify the main window is still open
        assert len(self.driver.window_handles) == 1
