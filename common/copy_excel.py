# coding=utf-8
"""
Author:zywen
Email：1004324878@qq.com

Date:2020/3/21 23:12
Desc:
"""
import time
import os
import xlrd
import xlwt
from xlutils.copy import copy
from common.read_excel import excel_file_path


def copy_excel(excel_path):
    """
    复制excel文件
    :param excel_path: 源excel路径
    :return: 复制的excel文件
    """
    # 打开待复制的工作薄
    workbook = xlrd.open_workbook(excel_path, formatting_info=True)
    # 复制一个新的excel
    new_workbook = copy(workbook)
    return  new_workbook


if __name__ == '__main__':
    # print(excel_file_path)
    save_path = os.path.dirname(
        os.path.dirname(__file__)) + r"/report/testCase.xls"
    new_workbook = copy_excel(excel_file_path)
    work_sheet = new_workbook.get_sheet(0)



