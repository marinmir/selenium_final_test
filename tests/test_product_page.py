# import allure
# import pytest
# from pages.product_page import ProductPage
# from pages.login_page import LogInPage
# from pages.main_page import MainPage
# from pages.basket_page import BasketPage
#
#
# @allure.feature('Product page')
# @allure.story('Add to cart button')
# def test_add_to_cart_button_is_displayed(driver):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     with allure.step('Open product page'):
#         product_page = ProductPage(driver)
#         product_page.open_product_page(link)
#     with allure.step('Add to cart button is displayed'):
#         assert product_page.add_to_cart_button_is_displayed()
#
#
# @allure.feature('Product page')
# @allure.story('Product addition message')
# def test_messages_that_the_product_has_been_added_is_displayed(driver):
#     link = \
#         'http://selenium1py.pythonanywhere.com/' \
#         'catalogue/the-shellcoders-handbook_209/?promo=newYear'
#     with allure.step('Open product page'):
#         product_page = ProductPage(driver)
#         product_page.open_product_page(link)
#     with allure.step('Click button: Add to cart'):
#         product_page.add_to_cart_button_click()
#     with allure.step('Check alert'):
#         product_page.alert_check()
#     with allure.step('Check message'):
#         assert product_page.product_addition_messages_is_displayed()
#
#
# @allure.feature('Product page')
# @allure.story('Product addition message')
# def test_message_with_the_cost_of_the_cart_is_displayed(driver):
#     link = \
#         'http://selenium1py.pythonanywhere.com/' \
#         'catalogue/the-shellcoders-handbook_209/?promo=newYear'
#     with allure.step('Open product page'):
#         product_page = ProductPage(driver)
#         product_page.open_product_page(link)
#     with allure.step('Click button: Add to cart'):
#         product_page.add_to_cart_button_click()
#     with allure.step('Check alert'):
#         product_page.alert_check()
#     with allure.step('Check message'):
#         assert product_page.message_with_the_cost_of_the_cart_is_displayed()
#
#
# @allure.feature('Product page')
# @allure.story('Product addition message')
# def test_the_product_was_added_with_the_name_correctly(driver):
#     link = \
#         'http://selenium1py.pythonanywhere.com/' \
#         'catalogue/the-shellcoders-handbook_209/?promo=newYear'
#     with allure.step('Open product page'):
#         product_page = ProductPage(driver)
#         product_page.open_product_page(link)
#         title_book = product_page.product_title()
#     with allure.step('Click button: Add to cart'):
#         product_page.add_to_cart_button_click()
#     with allure.step('Check alert'):
#         product_page.alert_check()
#     with allure.step('Check message'):
#         assert title_book == product_page.product_title()
#
#
# @allure.feature('Product page')
# @allure.story('The product was added correctly')
# @pytest.mark.parametrize('links', [
#     0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
# @pytest.mark.need_review
# def test_guest_can_add_product_to_basket(driver, links):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
#     with allure.step('Open product page'):
#         product_page = ProductPage(driver)
#         product_page.open_product_page(f'{link}{links}')
#     with allure.step('Click button: Add to cart'):
#         product_page.add_to_cart_button_click()
#     with allure.step('Check alert'):
#         product_page.alert_check()
#     with allure.step('Check message'):
#         assert product_page.product_price() == product_page.check_price_add_to_cart()
#         assert product_page.product_title() == product_page.check_title_add_to_cart()
#
#
# @allure.feature('Product page')
# @allure.story('Product addition message')
# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     with allure.step('Open product page'):
#         product_page = ProductPage(driver)
#         product_page.open_product_page(link)
#     with allure.step('Click add to cart'):
#         product_page.add_to_cart_button_click()
#     with allure.step('Check message'):
#         assert product_page.should_not_be_success_message()
#
#
# @allure.feature('Product page')
# @allure.story('Product addition message')
# def test_guest_cant_see_success_message(driver):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     with allure.step('Open product page'):
#         product_page = ProductPage(driver)
#     with allure.step('Open the shopping cart'):
#         product_page.open_product_page(link)
#     with allure.step('Check message'):
#         assert product_page.should_not_be_success_message()
#
#
# @allure.feature('Product page')
# @allure.story('Product addition message')
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(driver):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     with allure.step('Open the product page'):
#         product_page = ProductPage(driver)
#         product_page.open_product_page(link)
#     with allure.step('Open the shopping cart'):
#         product_page.add_to_cart_button_click()
#     with allure.step('Check message'):
#         assert product_page.the_element_disappears()
#
#
# @allure.feature('Product page')
# @allure.story('Login link in the product page')
# def test_guest_should_see_login_link_on_product_page(driver):
#     link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
#     with allure.step('Open the product page'):
#         product_page = ProductPage(driver)
#         product_page.open_product_page(link)
#     with allure.step('Login link in product page'):
#         assert product_page.should_be_login_link()
#
#
# @allure.feature('Product page')
# @allure.story('No product in the cart')
# @pytest.mark.need_review
# def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
#     link = 'http://selenium1py.pythonanywhere.com/'
#     with allure.step('Open product page'):
#         main_page = MainPage(driver)
#         main_page.open_site(f'{link}/catalogue/coders-at-work_207/')
#     with allure.step('Open the shopping cart'):
#         main_page.go_to_cart()
#         cart_page = BasketPage(driver)
#     with allure.step('Check product is not in the cart'):
#         assert cart_page.the_product_is_not_in_the_cart()
#         assert cart_page.message_the_cart_is_empty_is_displayed()
#
#
# @allure.feature('Product page')
# @allure.story('No product in the cart')
# @pytest.mark.need_review
# def test_guest_can_go_to_login_page_from_product_page(driver):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     with allure.step('Open the product page'):
#         product_page = ProductPage(driver)
#         product_page.open_product_page(link)
#     with allure.step('Click login button'):
#         product_page.go_to_login_page()
#         assert '/accounts/login/' in driver.current_url
#
#
# @allure.feature('Home page')
# @allure.story('Open login page')
# def test_guest_can_go_to_login_page(driver, language_options):
#     link = 'http://selenium1py.pythonanywhere.com/'
#     with allure.step('Open web site'):
#         main_page = MainPage(driver)
#         main_page.open_site(link)
#     with allure.step('Login link is displayed'):
#         assert main_page.login_link_is_displayed()
#     with allure.step('Click login button'):
#         main_page.go_to_login_page()
#     if language_options == 'en':
#         assert driver.current_url == f'{link}en-gb/accounts/login/'
#     else:
#         assert driver.current_url == f'{link}{language_options}/accounts/login/'
#
#
# class TestUserAddToBasketFromProductPage:
#
#     @pytest.fixture(scope="function", autouse=True)
#     def setup(self, driver):
#         link = 'http://selenium1py.pythonanywhere.com/'
#         main_page = MainPage(driver)
#         main_page.open_site(link)
#         new_user = LogInPage(driver)
#         new_user.register_new_user()
#
#     @allure.feature('Product page')
#     @allure.story('Product addition message')
#     def test_user_cant_see_success_message(self, driver):
#         link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#         with allure.step('Open the product page'):
#             product_page = ProductPage(driver)
#             product_page.open_product_page(link)
#         with allure.step('Check message'):
#             assert product_page.should_not_be_success_message()
#
#     @allure.feature('Product page')
#     @allure.story('The product was added correctly')
#     @pytest.mark.need_review
#     def test_user_can_add_product_to_basket(self, driver):
#         link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
#         with allure.step('Open the product page'):
#             product_page = ProductPage(driver)
#             product_page.open_product_page(link)
#         with allure.step('Click button: Add to cart'):
#             product_page.add_to_cart_button_click()
#         with allure.step('Check alert'):
#             product_page.alert_check()
#         with allure.step('Check message'):
#             assert product_page.product_price() == product_page.check_price_add_to_cart()
#             assert product_page.product_title() == product_page.check_title_add_to_cart()
