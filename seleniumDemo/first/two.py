import requests

url = 'http://192.168.1.42:7001/api/user/login'
data = {
    'loginName':'admin',
    'password':'1',
    'source':'web',
    'token':'null'
}
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Referer':'http://192.168.1.42:7001/index.html',
    'Content-Type':'application/x-www-form-urlencoded'
}
r = requests.post(url=url,data=data,headers=header)
print(r.json()['msg'])

