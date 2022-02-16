import time
import unittest

from ddt import ddt,data
from 百度搜索封装.po import BaiduPo
@ddt
class Badutext(unittest.TestCase):
    @data('爸爸','妈妈')
    def test1(self,arg):
        BaiduPo().search(arg)
        time.sleep(3)
if __name__ == '__main__':
    unittest.main()
