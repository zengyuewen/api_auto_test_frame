# coding=utf-8
"""
Author:zywen
Email：1004324878@qq.com

Date:2020/3/24 23:05
Desc:
"""
import os
from read_yaml_file import read_file

# 读取yaml文件
file_path = os.path.join(os.path.dirname(__file__),"config.yml")
yaml_content = read_file(file_path)

prj_path = yaml_content["prj_path"]   # 项目路径

# 日志路径
log_path = os.path.join(prj_path, 'report', 'logfile')

# 测试报告路径
report_path = os.path.join(prj_path, 'report')

# 测试数据路径
data_path = os.path.join(prj_path, 'data', 'testCase1.xls')


if __name__ == '__main__':
    print(prj_path)
    print(log_path)
    print(report_path)
    print(data_path)
    print(yaml_content["course_url"])
