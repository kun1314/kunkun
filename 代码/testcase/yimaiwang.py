from selenium import webdriver
import unittest
import time

class Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8080/EasyBuy/')

    @unittest.skip('不执行此用例')
    def test1(self):
        self.driver.find_element_by_xpath('/html/body/div[5]/div/ul/li[2]/a').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[2]/div[2]/ul/li[1]/div[4]/a[1]').click()
    def test2(self):
        self.driver.find_element_by_name('keyWord').send_keys('香水')
        #self.driver.find_element_by_xpath('//*[@id="searchBar"]/div/div[2]/form/input[2]').click()
    def tearDown(self):
        time.sleep(3)
        self.driver.close()
    # if __name__ == '__main__':
    #     unittest.main()
    #方法二
# suite=unittest.TestLoader().loadTestsFromTestCase(Test)
# unittest.TextTestRunner(verbosity=2).run(suite)
#方法三：
testunit = unittest.TestSuite()
testunit.addTest(Test("test2"))
unittest.TextTestRunner().run(testunit)