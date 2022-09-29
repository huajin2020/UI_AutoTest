from selenium import webdriver
import time

#非单元测试，类的名字不要带有test字样，带有test右键执行会默认单元测试，执行报错
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


# class Mylib(object):
#
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#
#     def delay(self):
#         self.driver.implicitly_wait(5)
#
#     def open_url(self, url):
#
#         self.driver.get(url)
#         self.delay()
#
#     #元素定位
#     def locate_element(self, locate_type, value):
#         return self.driver.find_element_by_id(value)
#
#     def click_element(self, locate_type, value):
#         #调用元素定位方法传参
#         self.locate_element(locate_type, value).click()
#
#     def input_date(self, locate_type, value, data):
#         #调用元素定位方法传参
#         self.locate_element(locate_type, value).send_keys(data)
#
#     def __del__(self):
#         time.sleep(5)
#         self.driver.close()
#
# if __name__ == '__main__':
#     web = Mylib()
#     web.open_url('http://www.baidu.com')
#     web.input_date('id', 'kw', 'selenium')
#     web.click_element('id', 'su')