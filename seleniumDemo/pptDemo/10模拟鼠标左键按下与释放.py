import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('http://127.0.0.1/left_down.html')
div = driver.find_element_by_id("div1")
test = ActionChains(driver)
test.click_and_hold(div).perform()
time.sleep(2)
test.release(div).perform()
time.sleep(2)
driver.close()