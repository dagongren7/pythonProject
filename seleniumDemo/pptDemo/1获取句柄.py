# coding:utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://bj.ganji.com/")
h = driver.current_window_handle
print(h)  # 打印首页句柄

driver.find_element_by_link_text("招聘求职").click()
all_h = driver.window_handles
print(all_h)  # 打印所有的句柄

# 方法一：判断句柄，不等于首页就切换
# for i in all_h:
#     if i != h:
#         driver.switch_to.window(i)
#         print(driver.title)

driver.switch_to.window(all_h[1])
print(driver.title)
# 关闭新窗口
driver.close()
# 切换到首页句柄
driver.switch_to.window(h)
# 打印当前的title
print(driver.title)
