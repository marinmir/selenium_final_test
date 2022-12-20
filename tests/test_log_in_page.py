# import allure
# from pages.main_page import MainPage
# from pages.login_page import LogInPage
#
#
# LINK = 'http://selenium1py.pythonanywhere.com/'
#
#
# @allure.feature('Login page')
# @allure.story('Should be login in the url')
# def test_should_be_login_in_the_url(driver):
#     with allure.step('Open site'):
#         main_page = MainPage(driver)
#         main_page.open_site(LINK)
#     with allure.step('Click for Login or register link'):
#         main_page.go_to_login_page()
#     with allure.step('Check if the URL has a login'):
#         log_in_page = LogInPage(driver)
#         assert 'login' in log_in_page.should_be_login_url()
#
#
# @allure.feature('Login page')
# @allure.story('Should be login form')
# def test_login_form_is_displayed(driver):
#     with allure.step('Open site'):
#         main_page = MainPage(driver)
#         main_page.open_site(LINK)
#     with allure.step('Click for Login or register link'):
#         main_page.go_to_login_page()
#     with allure.step('Check login form is displayed'):
#         login_page = LogInPage(driver)
#         assert login_page.should_be_login_form_is_displayed()
#
#
# @allure.feature('Login page')
# @allure.story('Should be register form')
# def test_register_form_is_displayed(driver):
#     with allure.step('Open site'):
#         main_page = MainPage(driver)
#         main_page.open_site(LINK)
#     with allure.step('Click for Login or register link'):
#         main_page.go_to_login_page()
#     with allure.step('Check register form is displayed'):
#         logi_page = LogInPage(driver)
#         assert logi_page.should_be_register_forms_is_displayed()
