from selenium import webdriver
import time
class baidu():
    def __init__(self):
        self.driver=webdriver.Chrome()#初始化浏览器对象
    def delay(self):
        self.driver.implicitly_wait(3)
    def openurl(self,url):
        self.driver.get(url)
        self.driver.maximize_window()
        self.delay()
    def locate_element(self,locate_type,value):
        return self.driver.find_element(locate_type,value)
    def __del__(self):
        time.sleep(3)
        self.driver.quit()
if __name__ == '__main__':
    web = baidu()
    web.openurl('https://www.baidu.com/')
    sousu=web.locate_element('id','kw')
    sousu.send_keys('新冠')
    anniu=web.locate_element('id','su')
    anniu.click()
