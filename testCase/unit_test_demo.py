# coding=utf-8
"""
Author:zywen
Email：1004324878@qq.com

Date:2020\3\22 15:45
Desc:
"""
import unittest


class UnittestDemo(unittest.TestCase):
    # 测试环境初始化
    @classmethod
    def setUpClass(cls):
        print("cls的SetUp方法运行了\r\n")

    def setUp(self):
        print("SetUp方法运行了\n")

    # 清除初始化
    @classmethod
    def tearDownClass(cls):
        print("cls的tearDown方法运行了\r\n")

    def tearDown(self):
        print("tearDown方法运行了\n")

    # 测试用例
    def test_001(self):
        print(">>>>执行用例1")

    @unittest.skip("跳过执行用例2")
    def test_002(self):
        self.assertEqual(1,2,"1不等于2")
        print(">>>>执行用例2")

    def test_003(self):
        print(">>>>执行用例3")

    def test_004(self):
        print(">>>>执行用例4")

    def test_005(self):
        print(">>>>执行用例5")


