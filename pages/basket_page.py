from pages.base_page import BasePage
from pages.locators import basket_page_locators as loc


class BasketPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def message_the_cart_is_empty_is_displayed(self):
        return self.find_element(loc.message_the_cart_is_empty).is_displayed()

    def the_product_is_not_in_the_cart(self):
        assert self.is_not_element_present(loc.product_in_the_cart)

    def the_product_in_the_cart(self):
        assert self.find_element(loc.product_in_the_cart).is_displayed()
