class LoginPage:
    textbox_username_css = '#email'
    textbox_password_css = '#password'
    button_login_css = 'div>button'

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element_by_css_selector(self.textbox_username_css).clear()
        self.driver.find_element_by_css_selector(self.textbox_username_css).send_keys(username)

    def set_password(self, password):
        self.driver.find_element_by_css_selector(self.textbox_password_css).clear()
        self.driver.find_element_by_css_selector(self.textbox_password_css).send_keys(password)

    def click_loginbutton(self):
        self.driver.find_element_by_css_selector(self.button_login_css).click()