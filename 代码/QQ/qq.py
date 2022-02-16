
from common.login import Login
import time
import unittest
from selenium import webdriver

class LogQQ(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://mail.qq.com/')
        self.driver.maximize_window()

    def test_qq1(self):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="login_frame"]'))
        time.sleep(10)
        self.driver.find_element_by_id('switcher_plogin').click()
        Login(self.driver).login('452990633','452990633cxm')
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="composebtn"]').click()
        time.sleep(10)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="mainFrame"]'))
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys('1048596163@qq.com;')
        time.sleep(10)
        self.driver.find_element_by_name('UploadFile').send_keys('C:\\1.txt')
        time.sleep(10)
        self.driver.find_element_by_css_selector('#toolbar > div.toolbg.toolbgline > a:nth-child(2)').click()
        self.driver.back()
    def test_qq2(self):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="login_frame"]'))
        time.sleep(10)
        self.driver.find_element_by_id('switcher_plogin').click()
        Login(self.driver).login('1048596163','lhz312613')
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="composebtn"]').click()
        time.sleep(10)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="mainFrame"]'))
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys('452990633@qq.com;')
        time.sleep(10)
        self.driver.find_element_by_name('UploadFile').send_keys('C:\\1.txt')
        time.sleep(10)
        self.driver.find_element_by_css_selector('#toolbar > div.toolbg.toolbgline > a:nth-child(2)').click()
    def tearDown(self) :
        time.sleep(3)
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
