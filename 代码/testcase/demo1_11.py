from selenium import webdriver#导入网站驱动
from selenium.webdriver import ActionChains#导入动作链
import time
driver=webdriver.Chrome()#选择驱动浏览器
#百度logo右击
# driver.get('https://www.baidu.com/')#获取百度链接
# driver.maximize_window()#窗口最大化
# acobj=ActionChains(driver)#定义网站动作
# el=driver.find_element_by_xpath('//*[@id="lg"]')#定位百度图片元素
# acobj.context_click(el).perform()
# time.sleep(5)#线程停止时间
# driver.quit()
#百度双击
# driver.get('https://www.baidu.com/')#获取百度链接
# driver.maximize_window()#窗口最大化
# acobj=ActionChains(driver)#定义网站动作
# el=driver.find_element_by_xpath('//*[@id="s-top-left"]/a[4]')
# acobj.double_click(el).perform()
# time.sleep(5)
# driver.quit()
#百度保存设置解散警告框
# driver.get('https://www.baidu.com/')#获取百度链接
# driver.maximize_window()#窗口最大化
# el=driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')#定位设置元素
# acobj=ActionChains(driver)#定义网站动作
# acobj.move_to_element(el).perform()#悬停鼠标在设置
# time.sleep(3)
# driver.find_element_by_link_text('搜索设置').click()#定位搜索设置元素，点击
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="se-setting-7"]/a[2]').click()#定位保存设置元素，点击
# time.sleep(3)
# driver.switch_to.alert.dismiss()#解散所有弹窗警告
# driver.quit()
#淘宝目录遍历练习
# driver.get('https://www.taobao.com/')#获取淘宝网址
# time.sleep(3)
# a=driver.find_elements_by_css_selector('li.J_Cat.a-all')#获取目录元素
# abjoct=ActionChains(driver)#定义网站动作
# for i in a:                            #for循环获取目录元素
#     abjoct.move_to_element(i).perform() #添加鼠标悬浮动作
#     time.sleep(3)
# driver.close()
#下拉框
# driver.get('https://www.baidu.com/')#获取百度网址
# driver.maximize_window()#窗口最大化
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="s-usersetting-top"]').click()#点击，定位设置元素
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div/a[2]').click()#点击，定位高级搜索
# time.sleep(3)
# # from selenium.webdriver.support.select import Select#引言Select方法
# a=driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/div/div[2]/div/form/ul/li[2]/span[2]/div/div[1]/i[1]')#定位下拉框元素
# a.click()
# driver.find_element_by_xpath('//*[@id="adv-setting-gpc"]/div/div[2]/div[2]/p[2]').click()#定位元素，点击
# ###
# # b=Select(a)#定义一个对象
# # time.sleep(3)
# # b.select_by_index(0)#引用Select索引
# ###
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/span/i').click()#定位关闭元素.点击
# driver.quit()
#移动滚动条
# driver.get('https://www.hao123.com/')#获取url
# for i in range(100):#for函数取range生成数组的值
#     js='window.scrollTo(0,%s)'%(100*i)#window.scrollTo()方法用于设置浏览器窗口滚动条的水平和垂直位置
#     driver.execute_script(js)#执行js脚本
#     time.sleep(0.1)
#driver.implicitly_wait(3)#隐式等待时间
# driver.quit()













