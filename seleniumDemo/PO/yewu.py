import requests

def deng():
    url='http://192.168.1.42:7001/api/user/login'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    body ={
        'loginName':'admin',
        'password':'1',
        'source':'web',
        'token':'null'
    }
    r = requests.post(url=url,data=body,headers=header)
    token = r.json()['data']['token']
    print(token)
    return token

def chuan(token):
    url = 'http://192.168.1.42:7001/api/file/upload'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Content-Type': 'multipart/form-data; boundary=----this is laohu'
    }
    body = {
        'token':token,
        'fileData':'tupian.png'

    }
    file = {
        'file': ('d:/tupian.png', open('d:/tupian.png', 'rb'), 'image/png', {'Expires': '0'})
    }
    r = requests.post(url=url,data=body,headers=header,files=file)
    print(r.text)
    return 0
chuan(deng())
# print(chuan(deng()))