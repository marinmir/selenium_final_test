from selenium.webdriver.common.by import By

add_to_cart_button = (By.CSS_SELECTOR, '[value="Add to basket"]')
product_name = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
product_price = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
information_by_add = (By.CSS_SELECTOR, '.alertinner  strong')
massage_add_product = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-success.fade.in')
message_cart = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-info.fade.in')
