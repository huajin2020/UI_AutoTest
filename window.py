from selenium import  webdriver
import  time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()

#打印点击之前的窗口句柄列表
#print('点击之前的窗口句柄:',driver.window_handles)
#print('当前的url:',driver.current_url,'当前的标题:',driver.title)

# 获取‘新闻’的元素并打新闻页面
driver.find_element_by_xpath('//*[@id="s-top-left"]/a[1]').click()

#暂停3秒
time.sleep(3)

#获取所有窗口
handles =driver.window_handles
#切换到新窗口
driver.switch_to.window(handles[1])

#暂停3秒
time.sleep(3)

#在新页面上打开‘地图’页面
#driver.find_element_by_css_selector('#header-link-wrapper > li:nth-child(8) > a').click()
#在新页面上不打开‘地图’页面
driver.find_element_by_css_selector('#header-link-wrapper > li:nth-child(8) > a')
time.sleep(3)

#切换到主窗口
#driver.switch_to.window(handles[0])

try:
# 定位一个再新窗口页面上的元素，如果能够定位到，则表明当前在新窗口上，如果失败则表明现在不在新窗口上
    el=driver.find_element_by_css_selector('#header-link-wrapper > li:nth-child(8) > a')
    print(el.text)
    print('driver在新页面')
except:
    print('driver不在新页面')

driver.quit()