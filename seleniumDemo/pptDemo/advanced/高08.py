from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://ueditor.baidu.com/website/examples/completeDemo.html')

#driver.switch_to.frame('ueditor_0')  # 注意，这种editor一定有frame，一定要切frame

body_string = """Hello world again again!
Hello world again again!
Hello world again again!

Hello world again again!"""
print("body_string=",body_string)
driver.find_element_by_tag_name('body').send_keys(body_string)  # 直接往frame里的body里填内容
print(driver.find_element_by_tag_name('body').text)
driver.quit()