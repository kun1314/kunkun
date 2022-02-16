import requests
import unittest
class EasyBuylogin (unittest.TestCase):
    def test1(self):
        url='http://127.0.0.1:8080/EasyBuy/Login'
        data='loginName=admin&password=123456&action=login'
        res=requests.request('post',url=url,params=data)
        print(res.json())
        result=res.json()['status']
        print(result)
        self.assertEqual(1,result)
        self.assertIn('登陆成功',res.text)
        self.assertTrue('操作成功'in res.text)
if __name__ == '__main__':
    unittest.main


