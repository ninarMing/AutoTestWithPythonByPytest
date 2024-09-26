# -*- coding:utf-8 -*-
import time

import pytest
from flaky import flaky
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from business.login_business import LoginBusiness
from config.build_config import BuildConfig
from drivers.driver import Driver
from util.log_util import LogUtil
from util.wait_util import delay_rerun

# 增加失败重试
@flaky(max_runs=2, min_passes=1,rerun_filter=delay_rerun)
class TestLogin:
    def setup_class(self):
        self.driver = Driver().get_driver()
        self.login_business = LoginBusiness(self.driver)
        self.driver.maximize_window()
        self.driver.get(BuildConfig.TESTED_URL)
        self.driver.implicitly_wait(10)

    @pytest.fixture()
    def fixture_accept_alert(self):
        yield
        print(type(self.driver))
        self.driver.switch_to.alert.accept()
        print("关闭alert")

    @pytest.fixture()
    def fixture_sure_logout(self):
        yield
        self.login_business.logout()
        time.sleep(5)
        print("退出登录")

    def test_00_start_must_success_first(self):
        print("必过")
        assert 1==1

    #@pytest.mark.skip
    @pytest.mark.parametrize("username,password",[("1000010","**20231"),("10000011","123456")])
    def test_login_username_or_password_error(self,fixture_accept_alert,username, password):
        print(type(self.driver))
        self.login_business.login(username, password)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        str_alert = self.driver.switch_to.alert.text
        print(str_alert)
        assert str_alert == "用户名或密码错误"
        time.sleep(2)

    #@pytest.mark.skip
    def test_login_username_or_password_success(self, fixture_sure_logout):
        username = "laijm"
        password = "laijm"
        self.login_business.login(username, password)
        #time.sleep(1)
        current_url = self.driver.current_url
        print(current_url)
        print(BuildConfig.ALREADY_LOGGED_URL)
        # assert current_url == BuildConfig.ALREADY_LOGGED_URL
        # pytest.assume进行断言，即使第一个失败了，后面的代码也会继续执行
        assert current_url == BuildConfig.ALREADY_LOGGED_URL
        time.sleep(11)

    #@pytest.mark.skip()
    def test_zz_end_must_success_last(self):
        assert 1==1


    def teardown_class(self):
        self.driver.quit()
        print("结束class测试")



if __name__ == '__main__':
    pytest.main(['-vs',"test_login.py"])

