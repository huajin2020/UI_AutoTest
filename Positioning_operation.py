from selenium import webdriver
import time

class Mylib():

    #python自带的__init__方法，在（非）main主方法下无须手工调用都可以执行
    def __init__(self):
    #def start_driver(self):
        #初始化浏览器对象
        self.driver = webdriver.Chrome()
        #窗口最大化
        self.driver.maximize_window()

    def delay(self):
        #延迟等待
        self.driver.implicitly_wait(5)

    def open_url(self, url):
        #访问网站
        self.driver.get(url)
        self.delay()
        print('访问:%s成功'%url)
        time.sleep(2)

    def locate_element(self,locate_type,value):
        #涉及元素定位封装，要用return返回给函数，不然调用会报错；如果封装的是send_keys()，可以不返回
        return self.driver.find_element(locate_type,value)

    #如果在（非）main主方法下不想手工调用自定义的关闭浏览器的函数（方法），可以使用python自带的__def__方法（自动调用），
    # 不然执行不了close()或quit()
    def __del__(self):
    #def close(self):
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    web = Mylib()
    #web.start_driver()
    web.open_url('https://www.baidu.com')
    web.locate_element('id','kw').send_keys('selenium')
    web.locate_element('id','su').click()
    #web.close()
