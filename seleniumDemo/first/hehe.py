import requests

url = "http://www.baidu.com/s"
params = {
    'wd':'七一建党节'
}
r = requests.get(url=url,params=params)
print(r.content.decode('utf-8'))