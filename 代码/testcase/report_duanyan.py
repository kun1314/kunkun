import HTMLTestRunnerCN
import unittest
TestCase_dir='C:\\Users\EDZ\Desktop\代码\\testcase'
dir=unittest.defaultTestLoader.discover(TestCase_dir,'duanyan.py')
filename='C:\\Users\EDZ\Desktop\代码\\result\\duanyan.html'
fp=open(filename,'wb')
runner=HTMLTestRunnerCN.HTMLTestRunner(stream=fp,title='测试报告',description='描述',)
runner.run(dir)