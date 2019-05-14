from selenium import webdriver

# 调用键盘按键操作时需要引入的Keys包
from selenium.webdriver.common.keys import Keys
import sys

a = "呵呵"
driver = webdriver.Chrome()
# driver = webdriver.PhantomJS()

# driver.get("http://fanyi.com")
driver.get("https://fanyi.baidu.com/#zh/en/{}".format(a))


import time
# time.sleep(2)
# driver.find_element_by_id("baidu_translate_input").send_keys(a)
time.sleep(15)
# driver.save_screenshot("a.png")
# driver.find_element_by_id("baidu_translate_input").send_keys("a")

#导入 ActionChains 类


b = """//p[@class="ordinary-output target-output clearfix"]/span"""
data = driver.find_element_by_xpath(b).text
print(data)
print(333)

driver.quit()


