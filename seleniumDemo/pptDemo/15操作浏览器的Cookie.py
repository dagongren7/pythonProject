import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.sogou.com')
cookies = driver.get_cookies()
for cookie in cookies:
    print("%s > %s > %s > %s > %s" \
          %(cookie['domain'],cookie['name'],\
            cookie['value'],cookie['expiry'],\
            cookie['path']))
ck = driver.get_cookie('SUV')
print("%s > %s > %s > %s > %s" \
     %(cookie['domain'],cookie['name'],\
     cookie['value'],cookie['expiry'],\
     cookie['path']))
#driver.delete_cookie('ABTEST')
#driver.delete_all_cookies()
driver.add_cookie({'name':'laohu','value':'1234'})
cook = driver.get_cookie('laohu')
print(cook)
driver.close()
