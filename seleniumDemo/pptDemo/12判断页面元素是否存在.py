import time
from selenium import webdriver

def is_ele_find(by,value):
    from selenium.common.exceptions import NoSuchElementException
    try:
        check = driver.find_element(by=by, value=value)
    except NoSuchElementException as e:
        return False
    else:
        return True

driver = webdriver.Chrome()
driver.get('http://www.sogou.com')
res = is_ele_find('id','query')
print(res)
if res is True:
    print("查到了")
else:
    print('没找到')
driver.close()


