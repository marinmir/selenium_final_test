# import allure
# from pages.main_page import MainPage
# from pages.basket_page import BasketPage
#
# LINK = 'http://selenium1py.pythonanywhere.com/'
#
#
# @allure.feature('Home page')
# @allure.story('Login link is displayed')
# def test_guest_should_see_login_link(driver):
#     with allure.step('Open web site'):
#         main_page = MainPage(driver)
#         main_page.open_site(LINK)
#     with allure.step('Login link is displayed'):
#         assert main_page.should_be_login_link()
#
#
# @allure.feature('Home page')
# @allure.story('No product in the cart')
# def test_guest_cant_see_product_in_basket_opened_from_main_pages(driver):
#     with allure.step('Open web site'):
#         main_page = MainPage(driver)
#         main_page.open_site(LINK)
#     with allure.step('Open the shopping cart'):
#         main_page.go_to_cart()
#         cart_page = BasketPage(driver)
#     with allure.step('Check product is not in the cart'):
#         assert cart_page.the_product_is_not_in_the_cart()
#         assert cart_page.message_the_cart_is_empty_is_displayed()
