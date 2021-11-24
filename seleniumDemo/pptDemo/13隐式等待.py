import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.sogou.com')
driver.implicitly_wait(10)
#time.sleep(10)
driver.close()

# 注意事项
# 隐式等待只需设置一次，它将在driver整个生命周期中都起作用。
# 弊端：会等待所有内容加载完成后才会进行下一步。
