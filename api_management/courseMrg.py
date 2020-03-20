# coding=utf-8
"""
Author:zywen
Email：1004324878@qq.com

Date:2020/3/17 22:52
Desc:
"""
import os
import requests
from pprint import pprint
from read_yaml_file import read_file


# 返回当前文件的上级目录的上级目录
config_path = os.path.dirname(os.path.dirname(__file__)) + r"/config.yml"

class courseMrg():
    def __init__(self):
        self.url = read_file(config_path)['course_url']

    # list course
    def list_courses(self, pagenum=1,pagesize=20):
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
        response = requests.get(self.url,params=params)
        response_result = response.json()
        pprint(response_result)

        return response_result

    # add course
    def add_course(self, course_name, course_des, course_rank):
        """
        添加课程
        :param course_name: 课程名称
        :param course_des: 课程描述
        :param course_rank: 课程序号
        :return: 添加结果
        """
        headers = {
            "Content-Type":"application/x-www-form-urlencoded"
        }
        payload = {
            "action" : "add_course",
            "data":f"""{{
                "name": "{course_name}",
                "desc": "{course_des}",
                "display_idx": {course_rank}}}"""
            }
        response = requests.post(self.url, headers=headers,data=payload)
        response_result = response.json()
        pprint(response_result)

        return response_result

    # add course json
    def add_course_json(self, course_name, course_des, course_rank):
        """
        添加课程-json请求头
        :param course_name: 课程名称
        :param course_des: 课程描述
        :param course_rank: 课程序号
        :return: 添加结果
        """
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
             "action" : "add_course_json",
             "data"	 : {
                  "name":f"{course_name}",
                  "desc":f"{course_des}",
                  "display_idx":f"{course_rank}"
            }
        }
        # pprint(type(payload))
        # url =  r'http://localhost/apijson/mgr/sq_mgr/'
        response = requests.post(self.url.replace("api","apijson"), headers=headers, json=payload)
        response_result = response.json()
        pprint(response_result)

        return response_result
    # modify course
    def modify_course(self,course_name, course_des, course_rank,course_id):
        """
        修改课程
        :param course_name: 课程名称
        :param course_des: 课程描述
        :param course_rank: 课程序号
        :param course_id: 课程id号
        :return:  修改结果
        """
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        payload = {
            "action": "modify_course",
            "id":course_id,
            "newdata": f"""{{
                        "name": "{course_name}",
                        "desc": "{course_des}",
                        "display_idx": {course_rank}}}"""
        }
        response = requests.put(self.url, headers=headers, data=payload)
        response_result = response.json()
        pprint(response_result)

        return response_result

    # delete course
    def delete_course(self, course_id):
        """
        删除课程
        :param course_id: 课程id号
        :return:  修改结果
        """
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        payload = {
            "action": "delete_course",
            "id": course_id,
        }
        response = requests.delete(self.url, headers=headers, data=payload)
        response_result = response.json()
        pprint(response_result)

        return response_result

def main():
    cm = courseMrg()
    list_ret = cm.list_courses()
    cm.add_course("初中数学012","数学描述",1)
    # cm.add_course_json("abcd","abcde",2)

    # for one in list_ret["retlist"]:
    #     if one["name"] == "abcd":
    #         c_id = one["id"]
              # cm.modify_course("abcd","abcde",2, c_id)
    #         cm.delete_course(c_id)
    # cm.list_courses()

if __name__ == '__main__':
    main()
