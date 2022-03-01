import unittest
import os
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
import time
import datetime
import pandas as pd


class ConnAging(unittest.TestCase):

    def setUp(self):
        # Set up appium
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub',
            desired_capabilities={
                "platformName": "Android",
                "platformVersion": "11",
                "deviceName": "GTA3",
                "automationName": "Appium",
                "newCommandTimeout": 3000,
                "appPackage": "com.koamtac.ktsync",
                "appActivity": "com.koamtac.ktsync.MainActivity",
                "udid": "R54R1029CWB",
                "noReset": "True"  # app 데이터 유지
            })

    def test_search_field(self):
        # appiun의 webdriver를 초기화 합니다.
        driver = self.driver
        # selenium의 WebDriverWait을 사용합니다. element가 나올때 까지 최고 20초까지 기다립니다.
        wait = WebDriverWait(driver, 20)
        # 테스트 시나리오에 따라 selenium 작성
        sleep(5)

        # disconnect 버튼 누름
        el = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView[5]")
        el.click();
        sleep(1)
        # connect 버튼 누름
        el = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView[1]")
        el.click();
        sleep(1)
        # 페어링 된 KDC 선택
        el = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout")
        el.click();
        #5초 대기 후 연결 상태 확인
        sleep(5)
        el = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView[2]")
        conn_stat = el.text
        print(conn_Stat)
        #conn_stat_slice = conn_stat[]
        #if

    sleep(20)
    # 이후 테스트 시나리오 추가 가능


def tearDown(self):
    self.driver.quit()


if __name__ == '__main__':
    suite = ConnAging.TestLoader().loadTestsFromTestCase(kbdtest)
    ConnAging.TextTestRunner(verbosity=2).run(suite)
