# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/31 15:15
from time import sleep


def test_baidu(driver):
    driver.get('http://www.baidu.com')
    driver.send_keys("id=>kw",'手机')
    sleep(3)
    assert '百度' in driver.driver.page_source
