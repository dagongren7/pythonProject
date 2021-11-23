import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://127.0.0.1/selectlist.html')
select = driver.find_element_by_name('fruit')
all_options = select.find_elements_by_tag_name("option")
for option in all_options:
    print("选项显示的文本：",option.text)
    print("选项值为：",option.get_attribute("value"))
    option.click()
time.sleep(3)

driver.close()
