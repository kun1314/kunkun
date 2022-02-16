from appium import webdriver
import time
desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='4.4.2'
desired_caps['deviceName']='127.0.0.1:62001'
desired_caps['appPackage']='com.android.settings'
desired_caps['appActivity']='.Settings'
# desired_caps['unicodeKeyboard'] = True
# desired_caps['resetKeyboard'] = True
time.sleep(3)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(3)
driver.find_element_by_id('android:id/title').click()
time.sleep(3)
driver.tap([0,56][24,80],500)
time.sleep(3)
driver.close()
