from selenium import webdriver
import xlrd
import time
driver=webdriver.Chrome()
driver.maximize_window()
data=xlrd.open_workbook('C:\\Users\EDZ\Desktop\代码\百度搜索封装\数据驱动.xls')
table=data.sheet_by_name('Sheet1')
for i in range(0,table.nrows):
    a=table.row_values(i)
    break
if(str(a[0])!=''):
    driver.get(a[0])
    time.sleep(3)
if(str(a[2])=='输入'):
    if(str(a[1])=='id'):
        driver.find_element_by_id(a[3]).send_keys(a[4])
if(str(a[6])=='点击'):
    if(str(a[5])=='id'):
        driver.find_element_by_id(a[7]).click()
    time.sleep(5)
for i in range(1,table.nrows):
    b=table.row_values(i)
    break
driver.find_element_by_xpath(b[0]).click()
time.sleep(3)
driver.close()
