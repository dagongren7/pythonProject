import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
time.sleep(2)

element = driver.find_element_by_xpath(".//*[@id='lg']/img")
actionChains = ActionChains(driver)
actionChains.context_click(element).send_keys(Keys.ARROW_DOWN).perform()

# click(on_element=None) ——单击鼠标左键
# click_and_hold(on_element=None) ——点击鼠标左键，不松开
# context_click(on_element=None) ——点击鼠标右键
# double_click(on_element=None) ——双击鼠标左键
# drag_and_drop(source, target) ——拖拽到某个元素然后松开
# drag_and_drop_by_offset(source, xoffset, yoffset) ——拖拽到某个坐标然后松开
# key_down(value, element=None) ——按下某个键盘上的键
# key_up(value, element=None) ——松开某个键
# move_by_offset(xoffset, yoffset) ——鼠标从当前位置移动到某个坐标
# move_to_element(to_element) ——鼠标移动到某个元素

