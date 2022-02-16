# try:
#     f=open('C:\\Users\EDZ\Desktop\\小记.txt')
# except Exception as f :
#     print('error')
# else:
#     print('success')

# import requests
#
# url='http://localhost:8080/EasyBuy/Login'
# data='loginName=admin&password=123456&action=login'
# t=requests.post(url=url,params=data)
# import json
#
# print(json.dumps(t.json(),indent=4,ensure_ascii=False))
import requests
import json
import jsonpath
url='http://localhost:8000/login'
data={
    'username':'admin',
    'password':'admin'
}
req=requests.post(url,json=data)
print(json.dumps(req.json(),indent=4,ensure_ascii=False))
print('**************************************************')
url1='http://localhost:8000/auth/hello'
token='Bearer '+jsonpath.jsonpath(req.json(),'$..token')[0]
handers = {
    'Authorization':token
}
req1=requests.get(url=url1,headers=handers)
print(json.dumps(req1.json(),indent=4,ensure_ascii=False))
print("**************************************************")
url2='http://httpbin.org/post'
file=open('C:\\Users\\EDZ\\Desktop\\小记.txt','rb')
files={
    'file':file
}
req2=requests.post(url=url2,files=files)
print(json.dumps(req2.json(),indent=4,ensure_ascii=False))
