from page.login_page import LoginPage


class LoginHandle:
    def __init__(self,driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)

    def clear_input_username(self):
        self.login_page.get_element_input_username().clear()

    def send_keys_to_username(self,username):
        self.login_page.get_element_input_username().send_keys(username)

    def send_keys_to_password(self,password):
        self.login_page.get_element_input_password().send_keys(password)

    def clear_input_password(self):
        self.login_page.get_element_input_password().clear()

    def click_btn_login(self):
        self.login_page.get_element_btn_login().click()

    def click_text_username(self):
        self.login_page.get_element_text_username().click()

    def click_to_change_password(self):
        self.login_page.get_element_to_change_password().click()

    def click_to_personal_information(self):
        self.login_page.get_element_to_personal_information().click()

    def click_to_logout(self):
        self.login_page.get_element_to_logout().click()

    def click_to_cancel_logout(self):
        self.login_page.get_element_to_cancel_logout().click()

    def click_to_sure_logout(self):
        self.login_page.get_element_to_sure_logout().click()