import time
from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get('http://127.0.0.1/xuan_fu.html')
link1 = driver.find_element_by_partial_link_text("指向1")
link2 = driver.find_element_by_partial_link_text("指向2")
p = driver.find_element_by_xpath("//p")
print(link1.text,link2.text)
test = ActionChains(driver)
test.move_to_element(link1).perform()
time.sleep(2)
test.move_to_element(p).perform()
time.sleep(2)
driver.close()