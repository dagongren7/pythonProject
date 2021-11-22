import time
from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get('http://127.0.0.1/double.html')
time.sleep(2)
inputBox=driver.find_element_by_id('inputBox')
time.sleep(2)
action_chains = ActionChains(driver)
action_chains.double_click(inputBox).perform()
time.sleep(3)
driver.close()
