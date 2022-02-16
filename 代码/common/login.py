
import time
class Login():
    def __init__(self,diver):
        self.diver= diver

    def login(self,name,passwd):
        self.diver.find_element_by_xpath('//*[@id="u"]').send_keys(name)
        self.diver.find_element_by_xpath('//*[@id="p"]').send_keys(passwd)
        time.sleep(3)
        self.diver.find_element_by_xpath('//*[@id="login_button"]').click()
