from selenium import webdriver
class BasePage:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
    def find(self,*args):
        return self.driver.find_element(*args)