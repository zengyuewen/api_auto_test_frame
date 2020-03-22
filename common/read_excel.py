# coding=utf-8
"""
Author:zywen
Email：1004324878@qq.com

Date:2020/3/21 11:11
Desc:
"""
import xlrd
import os
from pprint import pprint

# 读取Excel文件所在路径
excel_file_path =  os.path.dirname(
                  os.path.dirname(__file__)) + r"/data/testCase1.xls"

def get_data_list(file):
    """
    获取excel文件中的数据
    :param file:
    :return:
    """
    # open excel file
    data = xlrd.open_workbook(file)
    # 根据表名获取表,excel中从0开始计数
    table = data.sheet_by_index(0)
    # 获取表中的行数
    my_rows = table.nrows
    # print(my_rows)
    data_list = []    # 用来存放Excel中的用例数据，
                      # 每行作为一个列表，在组成一个大大列表
    for one in range(1,my_rows):
        data_list.append(table.row_values(one))

    return data_list

if __name__ == '__main__':
    data_list = get_data_list(excel_file_path)
    # pprint(data_list)