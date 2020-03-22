# coding=utf-8
"""
Author:zywen
Email：1004324878@qq.com

Date:2020/3/21 22:45
Desc:
"""
import time
import json
import os
from common.read_excel import get_data_list,excel_file_path
from common.sendCourseResquest import sendCourseRequest
from common.copy_excel import copy_excel


time_params = time.strftime("%Y%m%d%H%M%S",time.strptime(time.ctime()))
save_path = os.path.dirname(os.path.dirname(
            os.path.dirname(__file__)))  + rf"/report/testCase{time_params}.xls"

# 1、读取测试用例数据
test_case_list = get_data_list(excel_file_path)

# 2、复制一个excel表格
new_workbook = copy_excel(excel_file_path)
new_sheet = new_workbook.get_sheet(0)

# 3、执行测试用例
# for num in range(0,len(test_case_list)):
for num in range(0,17):
    row = test_case_list[num]
    response_ret = sendCourseRequest(row)
    my_assert = json.loads(row[6])
    if response_ret["retcode"] == my_assert["code"] == 0:
        print(row[0],"测试通过")
        # 将执行结果写入excel中
        new_sheet.write(num+1, 7, "PASS")
    else:
        print(row[0],"测试不通过")
        # 讲执行结果和原因写到excel中
        new_sheet.write(num+1, 7, "FAIL")
        if "reason" in response_ret.keys():
            new_sheet.write(num+1, 8, response_ret["reason"])

# 3、保存
new_workbook.save(save_path)
