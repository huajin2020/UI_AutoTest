import HTMLTestRunnerCN
import unittest
import time

#此脚本对接了CI(jenkins)做自动化定时任务构建，读取文件地址不能用相对路径，只能用绝对路径，相对路径持续集成找不到文件
#文件路径
Testcase_dir = 'C:\\Users\\EDY\\PycharmProjects\\AutoTest\\ui_test'
#Testcase_dir="../ui_test"

#获取该文件路径下的文件
dis = unittest.defaultTestLoader.discover(Testcase_dir,'ui_unittest_dome.py')

#测试报告名称前加时间戳
#now=time.strftime("%Y-%m-%d %H_%M_%S")

# 定义报告存放路径
filename = r"C:\Users\EDY\PycharmProjects\AutoTest\ui_test\ui_autotest_result.html"
#filename = "C:\\Users\\EDY\\PycharmProjects\\AutoTest\\ui_test\\"+now+"ui_autotest_result.html"
#filename="../ui_test/ui_autotest_result.html"

# 定义报告存放路径，如果没有，创建
fp = open(filename, 'wb')

# 定义测试报告
runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='测试', description="描述：")

# 运行测试用例
runner.run(dis)

#关闭报告文件
#fp.close()

#注：不要直接在用例脚本里调用HTMLTestRunnerCN生成报告，如果调用可以生成测试报告但没有数据