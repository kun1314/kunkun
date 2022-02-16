from duanyan import EasyBuylogin
import unittest
import HTMLTestRunnerCN
if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(EasyBuylogin('test1'))
with open('HTMLreport.html','wb') as f:
    runner=HTMLTestRunnerCN.HTMLTestRunner(stream=f,verbosity=2,title='自动化测试报告',description='描述')
    runner.run(suite)