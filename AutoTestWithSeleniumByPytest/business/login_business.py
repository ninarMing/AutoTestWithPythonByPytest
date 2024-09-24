import time

from handle.login_handle import LoginHandle


class LoginBusiness:
    def __init__(self,driver):
        self.driver = driver
        self.login_handle = LoginHandle(self.driver)
        self.driver.implicitly_wait(10)

    def login(self,username,password):
        self.login_handle.clear_input_username()
        self.login_handle.send_keys_to_username(username)
        self.login_handle.clear_input_password()
        self.login_handle.send_keys_to_password(password)
        self.login_handle.click_btn_login()

    def logout(self):
        self.login_handle.click_text_username()
        self.login_handle.click_to_logout()
        self.login_handle.click_to_sure_logout()

