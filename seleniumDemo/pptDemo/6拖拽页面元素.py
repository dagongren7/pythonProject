import time
from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get('http://jqueryui.com/resources/demos/draggable/scroll.html')
onePosition = driver.find_element_by_id("draggable")
twoPosition = driver.find_element_by_id("draggable2")
sanPosition = driver.find_element_by_id("draggable3")
action_chains = ActionChains(driver)
action_chains.drag_and_drop(onePosition, twoPosition).perform()
for i in range(5):
    action_chains.drag_and_drop_by_offset(sanPosition, 10, 10).perform()
    time.sleep(2)
driver.close()
