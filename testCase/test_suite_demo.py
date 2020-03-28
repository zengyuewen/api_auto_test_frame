# coding=utf-8
"""
Author:zywen
Email：1004324878@qq.com

Date:2020/3/22 16:29
Desc:
"""
import unittest
import os
import time
from HTMLTestRunner import HTMLTestRunner
from testCase.unit_test_demo import UnittestDemo



# 构建测试套件
suite = unittest.TestSuite()   # 定一个测试套件类对象

# 方法一： 逐个添加
# suite.addTest(UnittestDemo("test_001"))
# suite.addTest(UnittestDemo("test_002"))
# suite.addTest(UnittestDemo("test_003"))

# 方法二，先将用例添加到一个列表，在添加到suite执行
# tests = [UnittestDemo("test_001"), UnittestDemo("test_002"), UnittestDemo("test_003")]
# suite.addTests(tests)

# 方法三，通过TestLoader类的discover方法构建套件
# 使用方法unittest.defaultTestLoader.discover("用例所在模块",pattern="*通配符*.py")
test_path = os.path.abspath(os.path.dirname(__file__))
discover = unittest.defaultTestLoader.discover(test_path, pattern="unit*.py")

# 执行测试套件
# 方法一，使用unittest自带的报告导出
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(discover)

# 方法二，使用HTMLTestRunner导出报告
time_params = time.strftime("%Y%m%d%H%M%S",time.strptime(time.ctime()))
report_path = os.path.dirname(os.path.dirname(__file__))  + rf"/report/testReport{time_params}.html"

with open(report_path,"wb") as report_file:
    runner = HTMLTestRunner(title="接口自动化测试报告",
                            description="自动执行",
                            stream=report_file,
                            verbosity=2)
    runner.run(discover)

