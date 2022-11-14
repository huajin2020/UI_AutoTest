from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.hao123.com/')
time.sleep(2)
driver.maximize_window()
time.sleep(3)

for i in range(100):
    js = 'window.scrollTo(0,%s)'%(100*i) #滚动到固定位置
    # 滚动到距离顶部指定长度
    #js = "var q=document.documentElement.scrollTop=%s"%(100*i)
    driver.execute_script(js)
    time.sleep(1)

time.sleep(5)
driver.quit()
