from time import time
from pages.base_page import BasePage
from pages.locators import login_page_locators as loc


class LogInPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def should_be_login_url(self):
        return self.driver.current_url

    def should_be_login_form_is_displayed(self):
        return self.find_element(loc.log_in_form).is_displayed()

    def should_be_register_forms_is_displayed(self):
        return self.find_element(loc.reg_form).is_displayed()

    def register_new_user(self):
        self.go_to_login_page()
        email = str(time()) + "@fakemail.org"
        passwd = 'qaz12345z'
        self.find_element(loc.reg_fild_email).send_keys(email)
        self.find_element(loc.reg_fild_passwd).send_keys(passwd)
        self.find_element(loc.reg_fild_confirm_passwd).send_keys(passwd)
        self.find_element(loc.register_button).click()
        self.should_be_authorized_user()

    def check_driver_correct_url(self):
        url = self.driver.current_url
        assert '/accounts/login/' in url
