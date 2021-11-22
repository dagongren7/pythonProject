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

#方法：通过选项的显示文本选择文本为"猕猴桃"选项
select_element.select_by_visible_text("猕猴桃")
print(select_element.all_selected_options[0].text)
assert select_element.all_selected_options[0].text=="猕猴桃","选项异常"
time.sleep(3)

#方法：通过选项的value属性值选择value="shanzha"选项
select_element.select_by_value("shanzha")
print(select_element.all_selected_options[0].text)
assert select_element.all_selected_options[0].text=="山楂","选项异常"
driver.close()
