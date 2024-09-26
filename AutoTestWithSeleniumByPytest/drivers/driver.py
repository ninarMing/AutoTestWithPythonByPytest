# -*- coding:utf-8 -*-
import os.path
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

current_path = os.path.dirname(os.path.abspath(__file__))
class Driver(webdriver.Chrome):

    def __init__(self,*args,**kwargs):
        options = webdriver.ChromeOptions()
        options.pageLoadSreategy = "eager"
        service = Service(current_path+ "\\chromedriver_129.0.6668.58_x64.exe")
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

