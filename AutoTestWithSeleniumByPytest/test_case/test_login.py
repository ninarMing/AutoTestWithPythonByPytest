# -*- coding:utf-8 -*-
import time

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from business.login_business import LoginBusiness
from config.build_config import BuildConfig
from drivers.driver import Driver
from util.log_util import LogUtil


class TestLogin:
    def setup_class(self):
        self.driver = Driver().get_driver()
        self.login_business = LoginBusiness(self.driver)
        self.driver.maximize_window()
        self.driver.get(BuildConfig.TESTED_URL)
        self.driver.implicitly_wait(10)



    @pytest.fixture()
    def accept_alert(self):
        yield
        print(type(self.driver))
        self.driver.switch_to.alert.accept()
        print("关闭alert")

    @pytest.fixture()
    def sure_logout(self):
        yield
        self.login_business.logout()
        time.sleep(5)
        print("退出登录")

    @pytest.mark.skip
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("username,password",[("1000010","**20231"),("10000011","123456")])
    def test_login_username_or_password_error(self,username, password,accept_alert):
        try:
            self.login_business.login(username, password)
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            str_alert = self.driver.switch_to.alert.text
            print(str_alert)
            assert str_alert == "用户名或密码错误"
            time.sleep(2)
        except Exception as e:
            LogUtil.error(e)

    @pytest.mark.run(order=2)
    # pytest插件：pytest-rerunfailures=用例执行失败后重跑，装饰器或者用运行的时机，选择一个
    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_login_username_or_password_success(self,sure_logout):
        username = "laijm"
        password = "laijm"
        self.login_business.login(username, password)
        #time.sleep(1)
        current_url = self.driver.current_url
        print(current_url)
        print(BuildConfig.ALREADY_LOGGED_URL)
        # assert current_url == BuildConfig.ALREADY_LOGGED_URL
        # pytest.assume进行断言，即使第一个失败了，后面的代码也会继续执行
        pytest.assume(current_url == BuildConfig.ALREADY_LOGGED_URL)
        time.sleep(11)


    @pytest.mark.run(order=-1)
    def test_end_class(self):
        print("结束")
        self.driver.quit()
        print("quit")
        print("**********")





if __name__ == '__main__':
    pytest.main(['-vs',"test_case/test_login.py"])

