from selenium.webdriver.common.by import By

reg_form = (By.CSS_SELECTOR, '#register_form')
reg_form_text = (By.CSS_SELECTOR, '#register_form h2')
reg_fild_email = (By.CSS_SELECTOR, '#id_registration-email')
reg_fild_passwd = (By.CSS_SELECTOR, '#id_registration-password1')
reg_fild_confirm_passwd = (By.CSS_SELECTOR, '#id_registration-password2')
register_button = (By.NAME, 'registration_submit')

log_in_form = (By.CSS_SELECTOR, '#login_form')
log_in_form_text = (By.CSS_SELECTOR, '#login_form h2')
log_in_email = (By.CSS_SELECTOR, '#id_login-username')
log_in_passwd = (By.CSS_SELECTOR, '#id_login-password')
log_in_button = (By.NAME, 'login_submit')
