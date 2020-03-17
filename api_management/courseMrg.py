# coding=utf-8
"""
Author:zywen
Email：1004324878@qq.com

Date:2020/3/17 22:52
Desc:
"""
import requests
from read_yaml_file import read_file
import os

config_path = os.path.dirname(os.path.dirname(__file__))  # 返回当前文件的上级目录的上级目录
# print(config_path)
base_url = read_file(config_path)['url']
print(base_url)

# list course
def list_courses(pagenum=1,pagesize=20):
    """

    :param pagenum: 页码数
    :param pagesize: 每页显示记录数
    :return:
    """
    params = {
        "action":"list_course",
        "pagenum":pagenum,
        "pagesize":pagesize
    }

    response = requests.get()

