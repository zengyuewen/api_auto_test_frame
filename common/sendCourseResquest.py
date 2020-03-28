# coding=utf-8
"""
Author:zywen
Email：1004324878@qq.com

Date:2020/3/21 11:40
Desc:
"""
import json
import time
import requests
from common.read_excel import get_data_list
from api_lib.courseMrg import courseMrg
from global_params import data_path



cm = courseMrg()

def sendCourseRequest(row):
    """
    传一行数据，返回请求结果：字典格式
    :param row: 传入一行数据，测试用例中一个用例就是一行
    :return: 一个字典
    """
    if row[4] == "add":
        excel_data = json.loads(row[5])
        random_num = str(int(time.time()) * 10000)
        time.sleep(1)
        if "{{onoce}}" in excel_data["name"]:
            course_name = excel_data["name"].replace("{{onoce}}",random_num)
        else:
            course_name = excel_data["name"]
        response_ret = cm.add_course(course_name,excel_data["desc"],excel_data["display_idx"])
        return  response_ret
    elif row[4] == "delete":
        pass
    elif row[4] == "modify":
        pass
    elif row[4] == "list":
        # cm.list_courses()
        pass



if __name__ == '__main__':
    data_list = get_data_list(data_path)
    # print(data_list)
    for one in range(1,len(data_list)):
        sendCourseRequest(data_list[one])
        time.sleep(0.5)
