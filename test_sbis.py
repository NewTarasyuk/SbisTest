# Generated by Selenium IDE
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSbis():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_sbis(self):
        self.driver.maximize_window()
        self.driver.get("https://sbis.ru/")
        self.driver.find_element(By.LINK_TEXT, "Контакты").click()
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, ".sbisru-Contacts__border-left--border-xm img").click()
        self.vars["win1242"] = self.wait_for_window(2500)
        self.vars["root"] = self.driver.current_window_handle
        self.driver.switch_to.window(self.vars["win1242"])
        self.driver.find_element(By.CSS_SELECTOR,".tensor_ru-Index__block4-content > .tensor_ru-Index__card-text:nth-child(3)").click()
        element = self.driver.find_element(By.CSS_SELECTOR,".tensor_ru-Index__block4-content > .tensor_ru-Index__card-title")
        er = 0
        if element.text=="Сила в людях":
            element = self.driver.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg")
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            self.driver.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__block4-content .tensor_ru-link").click()
        else:
            er = er + 1
        element = self.driver.find_element(By.CSS_SELECTOR, ".s-Grid-col:nth-child(1) .tensor_ru-About__block3-image-filter")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element1 = self.driver.find_element(By.CSS_SELECTOR, ".s-Grid-col:nth-child(2) .tensor_ru-About__block3-image-filter")
        element2 = self.driver.find_element(By.CSS_SELECTOR, ".s-Grid-col:nth-child(3) .tensor_ru-About__block3-image-filter")
        element3 = self.driver.find_element(By.CSS_SELECTOR, ".s-Grid-col:nth-child(4) .tensor_ru-About__block3-image-filter")
        if element.size['height'] == element1.size['height'] and element1.size['height'] == element2.size['height'] and element2.size['height'] == element3.size['height'] \
            and element.size['width'] == element1.size['width'] and element1.size['width'] == element2.size['width'] and element2.size['width'] == element3.size['width']:
            print("Тест пройден")
        else:
            er = er + 1
            print("Тест завершён с "+ str(er) +" ошибкой")


        time.sleep(3)
        self.driver.close()
        self.driver.switch_to.window(self.vars["root"])
        self.driver.close()
        # self.driver.switch_to.window(self.vars["undefined"])

