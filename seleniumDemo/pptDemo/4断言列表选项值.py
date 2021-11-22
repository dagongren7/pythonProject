import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get('http://127.0.0.1/selectlist.html')
select_element = Select(driver.find_element_by_xpath("//select"))
all_options = select_element.options
option_list = ['桃子','西瓜','桔子','猕猴桃','山楂','荔枝']
#使用python内置的map()获取页面中下拉列表成员对象
src_list = map(lambda option:option.text,all_options)
assert option_list==list(src_list),"选项不符"
print(option_list)
driver.close()
