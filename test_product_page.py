import allure
import pytest
from pages.product_page import ProductPage
from pages.login_page import LogInPage
from pages.main_page import MainPage
from pages.basket_page import BasketPage


@allure.feature('Product page')
@allure.story('Product addition message')
def test_the_product_was_added_with_the_name_correctly(driver):
    link = \
        'http://selenium1py.pythonanywhere.com/' \
        'catalogue/the-shellcoders-handbook_209/?promo=newYear'
    with allure.step('Open product page'):
        product_page = ProductPage(driver)
        product_page.open_product_page(link)
        title_book = product_page.product_title()
    with allure.step('Click button: Add to cart'):
        product_page.add_to_cart_button_click()
    with allure.step('Check alert'):
        product_page.alert_check()
    with allure.step('Check message'):
        assert title_book == product_page.product_title()


@allure.feature('Product page')
@allure.story('The product was added correctly')
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1'
    with allure.step('Open product page'):
        product_page = ProductPage(driver)
        product_page.open_product_page(f'{link}')
    with allure.step('Click button: Add to cart'):
        product_page.add_to_cart_button_click()
    with allure.step('Check alert'):
        product_page.alert_check()
    with allure.step('Check message'):
        product_page.check_price_add_to_cart()
        product_page.check_title_add_to_cart()


@allure.feature('Product page')
@allure.story('Login link in the product page')
def test_guest_should_see_login_link_on_product_page(driver):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    with allure.step('Open the product page'):
        product_page = ProductPage(driver)
        product_page.open_product_page(link)
    with allure.step('Login link in product page'):
        product_page.should_be_login_link()


@allure.feature('Product page')
@allure.story('No product in the cart')
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    link = 'http://selenium1py.pythonanywhere.com/'
    with allure.step('Open product page'):
        main_page = MainPage(driver)
        main_page.open_site(f'{link}/catalogue/coders-at-work_207/')
    with allure.step('Open the shopping cart'):
        main_page.go_to_cart()
        cart_page = BasketPage(driver)
    with allure.step('Check product is not in the cart'):
        cart_page.the_product_is_not_in_the_cart()
        cart_page.message_the_cart_is_empty_is_displayed()


@allure.feature('Product page')
@allure.story('No product in the cart')
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    with allure.step('Open the product page'):
        product_page = ProductPage(driver)
        product_page.open_product_page(link)
    with allure.step('Click login button'):
        product_page.go_to_login_page()
        login_page = LogInPage(driver)
        login_page.check_driver_correct_url()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        link = 'http://selenium1py.pythonanywhere.com/'
        main_page = MainPage(driver)
        main_page.open_site(link)
        new_user = LogInPage(driver)
        new_user.register_new_user()

    @allure.feature('Product page')
    @allure.story('Product addition message')
    def test_user_cant_see_success_message(self, driver):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        with allure.step('Open the product page'):
            product_page = ProductPage(driver)
            product_page.open_product_page(link)
        with allure.step('Check message'):
            product_page.should_not_be_success_message()

    @allure.feature('Product page')
    @allure.story('The product was added correctly')
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, driver):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        with allure.step('Open the product page'):
            product_page = ProductPage(driver)
            product_page.open_product_page(link)
        with allure.step('Click button: Add to cart'):
            product_page.add_to_cart_button_click()
        with allure.step('Check alert'):
            product_page.alert_check()
        with allure.step('Check message'):
            product_page.check_price_add_to_cart()
            product_page.check_title_add_to_cart()
