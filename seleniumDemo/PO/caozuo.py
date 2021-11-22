from selenium import webdriver
from PO.element import Eleme
def sousuo(neirong):
    driver = webdriver.Firefox()
    driver.get("http://www.baidu.com/")
    driver.find_element_by_xpath(Eleme().shuru).send_keys(neirong)
    driver.find_element_by_id(Eleme().sou).click()
    driver.quit()
def gou():
    print("加入购物车")
def jie():
    print("结算")