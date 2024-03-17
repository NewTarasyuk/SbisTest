import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestUntitled():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_untitled(self):
        self.driver.get("https://sbis.ru/")
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "Контакты").click()
        #element = self.driver.find_element(By.CSS_SELECTOR,"")
        tt =0
        self.driver.find_element(By.CSS_SELECTOR, ".ml-16 > .sbis_ru-Region-Chooser__text").click()
        if self.driver.title.find("Тюменская область")!= -1:
            tt = tt + 1
        else:
            print("Ошибка")

        er = self.driver.find_element(By.CSS_SELECTOR, ".sbisru-Contacts-City__container-inner:nth-child(20) > .sbisru-Contacts-City__item").text.split("\n")[1]
        iu = 1
        for tr in range(2,int(er)+2):
            element = self.driver.find_element(By.CSS_SELECTOR, f'.controls-ListView__itemV-relative:nth-child({tr}) .sbisru-Contacts-List__name')

        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, '.sbis_ru-Region-Panel__item:nth-child(43) > .sbis_ru-link > span').click()
        time.sleep(2)
        erkam =self.driver.find_element(By.CLASS_NAME,"sbisru-Contacts-City__item").text.split("\n")[1]

        for ter in range(2, int(erkam)+2):
            element = self.driver.find_element(By.CSS_SELECTOR,f'.controls-ListView__itemV-relative:nth-child({ter}) .sbisru-Contacts-List__name')
        if self.driver.find_element(By.CSS_SELECTOR, ".ml-16 > .sbis_ru-Region-Chooser__text").text=="Камчатский край":
            tt = tt + 1
        else:
            print("Ошибка")
        self.driver.close()