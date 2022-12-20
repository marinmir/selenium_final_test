from pages.base_page import BasePage
from pages.locators import main_page_locators as loc


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login_link_is_displayed(self):
        return self.find_element(loc.login_link).is_displayed()

    def should_be_login_link(self):
        return self.find_element(loc.login_link)
