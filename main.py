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
        #wait = WebDriverWait(driver, 20)
        # 테스트 시나리오에 따라 selenium 작성
        sleep(10)
        bar_da = "9300647000342"
        cs = 0 #연결성공 카운트
        cf = 0 #연결실패 카운드
        ss = 0 #스캔성공 카운트
        nm = 0 #스캔데이터 불일치 카운트
        sf = 0 #스캔실패 카운드
        cfc = 0 #연결실패 연속 카운트

        #KDC 연결끊기 - 연결 - 스캔 반복 수행
        #연결 실패 연속 10회 발생하면 중단
        while cfc < 10:
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
                cs = cs+1
                #연결 성공하면 바코드 스캔 동작
                try:
                    #스캔버튼 클릭
                    driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView").click()
                    #스캔 데이터 대기(3초 기다려도 안나타나면 에러 발생)
                    wait = WebDriverWait(driver, 3)
                    element = wait.until(EC.visibility_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.TextView")))
                    scan_da = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.TextView").text
                    #appium으로 땡겨온 text에 이상한값(보이지 않음)이 있어 슬라이싱으로 마지막 2글자를 자름
                    scan_da_slice = scan_da[0:len(scan_da)-2]
                    #스캔된 바코드 결과값 비교
                    if scan_da_slice == bar_da:
                        # 데이터 일치하면 스캔성공 증가
                        ss = ss + 1
                    else:
                        # 데이터 불일치하면 불일치 증가
                        nm = nm + 1
                    cfc = 0
                except:
                    #try문 에러 발생시 스캔실패 증가
                    sf = sf + 1




                #interal viewer clear
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView[3]").click()

            else:
                cf = cf+1
                cfc = cfc + 1
            #IDE 콘솔창에 결과 출력
            result = "연결성공 " + str(cs) + "회" +"(스캔성공 " + str(ss) + "회, " + "데이터불일치 " + str(nm) + "회, " + "스캔실패 " + str(sf) + "회" + ")" +" / " + "연결실패 " + str(cf) + "회"
            print(result)
            f = open("ConnAgingResult.txt","w")
            f.write(result)
            f.close()





def tearDown(self):
    self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(ConnAging)
    unittest.TextTestRunner(verbosity=2).run(suite)
