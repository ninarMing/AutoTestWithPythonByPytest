#-*-coding:utf-8-*-
import os
import time
from pathlib import Path


# 设置flaky出错重试开启下一次重试时间间隔
def delay_rerun(*args):
    time.sleep(1)
    return True



