import time
from selenium.webdriver.common.by import By
from 百度搜索封装.baiduBasePage import BasePage

class BaiduPo(BasePage):
    baiduinput=(By.ID,'kw')
    baiduclick=(By.ID,'su')
    def input(self):
        return self.find(*BaiduPo.baiduinput)
    def submit(self):
        return self.find(*BaiduPo.baiduclick)
    def search(self,txt):
        self.input().send_keys(txt)
        self.submit().click()
        time.sleep(3)

