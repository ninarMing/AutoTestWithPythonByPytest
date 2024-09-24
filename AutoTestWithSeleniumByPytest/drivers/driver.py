# -*- coding:utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Driver(webdriver.Chrome):

    def __init__(self,*args,**kwargs):
        options = webdriver.ChromeOptions()
        options.pageLoadSreategy = "eager"
        service = Service("../drivers/chromedriver_129.0.6668.58_x64.exe")
        # service = Service(r"D:\Program Files\Python312\chromedriver_127.0.6533.119_x64.exe")
        # driver = webdriver.Chrome(options=options, service=service)
        super().__init__(options=options, service=service,*args,**kwargs)
        # super().__init__(options=options,*args,**kwargs)


    def get_driver(self):
        return self

if __name__ == '__main__':
    driver = Driver().get_driver()
    driver.get("http://www.baidu.com")
    time.sleep(6)
    driver.quit()

