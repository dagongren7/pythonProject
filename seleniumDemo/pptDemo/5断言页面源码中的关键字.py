import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_id("kw").send_keys("软达启航")
driver.find_element_by_id("su").click()
time.sleep(3)
#页面源码中有‘软达启航’正确，否则报‘页面源码中不存在该关键字’
assert "软达启航" in driver.page_source, "页面源码中不存在该关键字"
driver.close()
