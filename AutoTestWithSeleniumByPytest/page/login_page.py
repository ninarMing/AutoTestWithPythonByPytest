import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def get_element_input_username(self):
        element = self.driver.find_element(By.NAME, "loginName")
        return element

    def get_element_input_password(self):
        element = self.driver.find_element(By.NAME, "passwd")
        return element

    def get_element_btn_login(self):
        element = self.driver.find_element(By.CLASS_NAME, "login-submit-btn")
        return element

    def get_element_text_username(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ant-dropdown-trigger")))
        # element = self.driver.find_element(By.CLASS_NAME, "ant-dropdown-trigger")
        return element

    def get_element_to_change_password(self):
        element = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/ul/li[1]/span")
        return element

    def get_element_to_personal_information(self):
        element = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/ul/li[2]/span")
        return element

    def get_element_to_logout(self):
        element = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/ul/li[4]/span")
        return element

    def get_element_to_cancel_logout(self):
        # elements = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
        time.sleep(2)
        elements = self.driver.find_elements(By.TAG_NAME, "button")
        for element in elements:
            if element.text == "取 消":
                return element

    def get_element_to_sure_logout(self):
        # elements = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
        time.sleep(2)
        elements = self.driver.find_elements(By.TAG_NAME, "button")
        for element in elements:
            if element.text == "退 出":
                return element

