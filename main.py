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
                "platformVersion": "11",# 실행할 폰에 맞추어 정보 수정 필요
                "deviceName": "GTA3",# 실행할 폰에 맞추어 정보 수정 필요
                "automationName": "Appium",
                "newCommandTimeout": 3000,
                "appPackage": "com.koamtac.ktsync",
                "appActivity": "com.koamtac.ktsync.MainActivity",
                "udid": "R54R1029CWB",# 실행할 폰에 맞추어 정보 수정 필요
                "noReset": "True"  # app 데이터 유지
            })

    def test_search_field(self):
        # appiun의 webdriver를 초기화 합니다.
        driver = self.driver
        # selenium의 WebDriverWait을 사용합니다. element가 나올때 까지 최고 20초까지 기다립니다.
        wait = WebDriverWait(driver, 20)
        # 테스트 시나리오에 따라 selenium 작성
        sleep(10)
        s = 0
        f = 0

        #KDC 연결끊기 - 연결 무한 반복
        while True:
            # disconnect 버튼 누름
            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView[5]").click()
            sleep(1)
            # connect 버튼 누름
            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView[1]").click()
            sleep(1)
            # 페어링 된 KDC 선택
            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout").click()
            #10초 대기 후 연결 상태 확인
            sleep(10)
            conn_stat = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView[2]").text
            #print(conn_stat)
            conn = conn_stat[-9:]
            #print(conn)
            if conn == "Connected":
                s = s+1
            else:
                f = f+1
            print("연결성공 " + str(s) + "회" + " / " + "연결실패 " + str(f) + "회")





    # 이후 테스트 시나리오 추가 가능


def tearDown(self):
    self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(ConnAging)
    unittest.TextTestRunner(verbosity=2).run(suite)
