import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
input = driver.find_element_by_id("kw")
input.send_keys("selenium")
time.sleep(3)
ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').perform()
time.sleep(2)
driver.find_element_by_id("su").click()
driver.close()
