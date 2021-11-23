import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('http://www.sogou.com')
query = driver.find_element_by_id("query")
print("Keys.F12=%s\n",Keys.F12)
query.send_keys(Keys.F12)
time.sleep(3)
query.send_keys(Keys.F12)
query.send_keys("selenium")
query.send_keys(Keys.ENTER)
print("Keys.ENTER=%s\n" % Keys.ENTER)
time.sleep(3)
driver.close()
