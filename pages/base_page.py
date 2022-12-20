import math
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.locators import base_page_locators as loc


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_site(self, link):
        self.driver.get(link)

    def find_element(self, *args):
        element, value = args[0]
        return self.driver.find_element(element,  value)

    def find_elements(self, *args):
        element, value = args[0]
        return self.driver.find_elements(element,  value)

    def is_element_present(self, *args):
        element, value = args[0]
        try:
            self.driver.find_element(element, value)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x_num = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x_num))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, *args, timeout=4):
        element, value = args[0]
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located((element, value))
            )
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, *args, timeout=4):
        element, value = args[0]
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException).\
                until_not(ec.presence_of_element_located((element, value)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        self.find_element(loc.login_link).click()

    def should_be_login_link(self):
        assert self.is_element_present(loc.login_link)

    def go_to_cart(self):
        self.find_element(loc.cart_button).click()

    def should_be_authorized_user(self):
        assert self.is_element_present(loc.user_icon), "User icon is not presented," \
                                                                     " probably unauthorised user"
