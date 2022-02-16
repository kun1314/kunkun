'''
name = "卢信坤"
age = 12
weight = 60
print("我的名字叫%s,今年已经%d了,体重大概%.2f"%(name,age,weight))
'''
# name = input("请输入你的名字；")
# print("欢迎%s先生"%name)
'''
age = input("请输入你的年纪")
age = int(age)
if age > 18:
    print("你可以去网吧了")
else:
    print("你还是回家写作业吧")

user = input("请输入你的名字；")
passwd = input("请输入你的密码；")
if user == "曹操" and passwd == "123456":
    print("登录成功")
else :
    print("用户信息或密码输入错误")

gao = input("高吗？输入Y/N: ")
fu = input("富吗？输入Y/N: ")
shuai = input("帅吗？输入Y/N: ")
if gao== "Y" and fu == "Y" and shuai == "Y":
    print("今晚去我家")
else:
    print("晚上家里门禁") 

score = input("请输入你的成绩；")
score = int(score)
if score > 90 and score <= 100:
    print ("成绩优秀")
elif score >80 and score <=90:
    print ("成绩良好")
elif score > 60 and score <= 80:
    print("成绩一般")
else:
    print("成绩不及格")

no1 = input ("请输入一个数字：")
no2 = input ("请再输入一个数字：")
if no1 > no2 :
    print("较大的数为%s" % no1)
else:
    print("较大的数为%s"% no2)  
no1 = input ("请输入一个数字：")
no2 = input ("请再输入一个数字：")
no3 = input ("请再输入一个数字：")
if no1 > no2 and no1 > no3:
    print("最大的数为%s" %no1)
elif no2 > no1 and no2 < no3:
    print("最大的数为%s" %no3)
else:
    print("最大的数为%s" %no2)

a = 10
b = 20 
a = a + b
b = a - b
a = a - b 
print("a的值为%d,b的值为%d" %(a,b) )

a = 10
b = 20 
m = a
a = b
b = m
print("a的值为%d,b的值为%d" %(a,b) )

a = 10
b = 20 
(a,b)=(b,a)
print("a的值为%d,b的值为%d" %(a,b) )

i = 1
while i < 101:
    print (i)
    i = i + 1

i = 1
while i <= 100 :
    if i % 3 == 0 and i % 7 == 0:
        print(i)
    i = i + 1

i = 1 
u = 0
while i < 101 :
    u  = i + u 
    i = i + 1
print( u )

i = 1
u = 1
while i <= 10:
    u = i * u 
    i = i + 1
print (u)    

i = 0 
count=0
while i < 100 :
    i = i + 1
    if i % 3 == 0 and i % 7 == 0:
        print (i)
        count = count + 1
    if count == 2:
        break


i = 0 
while i < 100:
    i = i + 1
    if i % 3 == 0 :
        continue
    print(i )

num1 = 1
num2 = 1
num3 = num1 + num2
time = 3
while  time < 12:
    num1 = num2
    num2 = num3
    num3 = num1 + num2
    time = time + 1
print(num3)

i = 0 
while i < 100:
    i = i + 1
    if i % 2 == 0 or i % 3 == 0 :
        continue
    print(i)

count = 3
print("用户信息或密码只有%d次机会，请谨慎输入"%count)
while True:
    user = input("请输入用户名：")
    passwd = input("请输入你的密码；")
    if user == "曹操" and passwd == "123456":
        print("登录成功")
        break
    else:
        count = count - 1
        if count < 1:
            print("账号已锁定，无法登录")
            break
        print("用户信息或密码输入错误，还有%d机会请重新输入："%count)

num = int(input("请输入一个自然数： "))
if num == 1:
    print("1不是质数")
if num == 2:
    print("2是质数")
chushu = 2
while chushu < (num - 1):
    if num % chushu == 0:
        print("%d不是质数" % num)
        break
    else:
        print("%d是质数" % num)
        break
    chushu = chushu + 1

num = 0
while num < 100:
    num = num + 1
    if num == 1:
        continue
    if num == 2:
        print(num)
    chushu = 2
    while chushu <= (num - 1):
        if num % chushu == 0:
            break
        if chushu == num - 1 :
            print(num)
            break
        chushu = chushu + 1

class Prople():
    def hand(self):
        return print('我是你爸爸')
print(Prople().hand())
a=Prople()
print(a.hand())
'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()
time.sleep(3)
# driver.find_element_by_id('kw').send_keys('帅哥')
# driver.find_element_by_id('su').click()
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/a[1]').click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[-1])
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[3]/div[1]/div/ul/li[1]/strong/a').click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[2])
time.sleep(3)
driver.close()


