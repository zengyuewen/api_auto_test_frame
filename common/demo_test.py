# coding=utf-8
"""
Author:zywen
Email：1004324878@qq.com

Date:2020/3/22 0:17
Desc:
"""
import time
import sys
import unittest



# save_path = os.path.dirname(
#     os.path.dirname(__file__)) + r"/report/testCase.xls"

# class TestMathFunc(unittest.TestCase):
#     """Test mathfuc.py"""
#     @classmethod
#     def setUpClass(cls):
#         print("This setUpClass() method only called once.")
#
#     @classmethod
#     def tearDownClass(cls):
#         print("This tearDownClass() method only called once too.")
#
#     def test_001(self):
#         print("测试1执行了")
#
#     def test_002(self):
#         print("测试2执行了")

class Test():
    def zyw(self):
        print(f"class name :{self.__class__.__name__}")
        print(f"method name:{sys._getframe().f_code.co_name}")

if __name__ == '__main__':
    t = Test().zyw()
