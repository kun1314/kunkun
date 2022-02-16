import HTMLTestRunnerCN
import unittest
Testcase_dir='C:\\Users\EDZ\Desktop\代码\QQ'
dis=unittest.defaultTestLoader.discover(Testcase_dir,'qq.py')
filename='C:\\Users\EDZ\Desktop\代码\\result\\report.HTML'
fp=open(filename,'wb')
runner=HTMLTestRunnerCN.HTMLTestRunner(stream=fp,title='测试报告',description='描述')
runner.run(dis)