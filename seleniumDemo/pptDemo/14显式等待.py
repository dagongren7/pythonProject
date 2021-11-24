import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
# driver.get('https://www.csdn.net/')
# wait = WebDriverWait(driver,10,0.2)
# element = driver.find_element_by_xpath\
#     ('//*[@id="floor-www-index_558"]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div[1]/a[1]')
# element.click()
# print(driver.title)
# wait.until(EC.title_is('CSDN - 专业开发者社区'))

element = WebDriverWait(driver,10,0.2).until\
    (lambda x: x.find_element_by_xpath\
    ('//*[@id="floor-www-index_558"]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div[1]/a[1]'))
element.click()
driver.close()
