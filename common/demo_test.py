# coding=utf-8
"""
Author:zywen
Email：1004324878@qq.com

Date:2020/3/22 0:17
Desc:
"""
import time
import os


save_path = os.path.dirname(
    os.path.dirname(__file__)) + r"/report/testCase.xls"
print(save_path)

print(time.strptime(time.ctime()))
print(time.strftime("%Y%m%d%H%M%S",time.strptime(time.ctime())))

print("cls的SetUp方法运行了\r\n")
print("cls的SetUp方法运行了\n")
print("cls的SetUp方法运行了\r\n")




