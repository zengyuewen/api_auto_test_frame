# coding=utf-8
"""
Author:zywen
Email：1004324878@qq.com

Date:2020/3/17 22:52
Desc:
"""
import sys
import time
import requests
from pprint import pprint
from common.log import Log
from global_params import yaml_content


class courseMrg():
    def __init__(self):
        self.url = yaml_content['course_url']
        self.log = Log()

    def _my_log(self, msg):
        return self.log.info(msg)

    # list course
    def list_courses(self, pagenum=1,pagesize=20):
        """

        :param pagenum: 页码数
        :param pagesize: 每页显示记录数
        :return:
        """
        t1 = time.time()
        self._my_log(f"方法：{sys._getframe().f_code.co_name} 开始运行")
        params = {
            "action":"list_course",
            "pagenum":pagenum,
            "pagesize":pagesize
        }
        self._my_log(f"请求参数为：{params}")

        try:
            response = requests.get(self.url,params=params)
            response_result = response.json()
            self._my_log(f"方法：{sys._getframe().f_code.co_name} 请求成功")
            self._my_log(f"响应内容是：{response_result}, 耗时{time.time() - t1}" )
            return response_result
        except Exception:
            self._my_log(f"方法：{sys._getframe().f_code.co_name} 请求出现异常")
            return {"retcode": 1000, "reason": "出现异常"}

    # add course
    def add_course(self, course_name, course_des, course_rank):
        """
        添加课程
        :param course_name: 课程名称
        :param course_des: 课程描述
        :param course_rank: 课程序号
        :return: 添加结果
        """
        t1 = time.time()
        self._my_log(f"方法：{sys._getframe().f_code.co_name} 开始运行")
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
        self._my_log(f"请求头是：{headers}")
        self._my_log(f"请求体是：{payload}")
        try:
            response = requests.post(self.url, headers=headers,data=payload)
            response_result = response.json()
            self._my_log(f"方法：{sys._getframe().f_code.co_name} 请求成功")
            self._my_log(f"响应内容是：{response_result}, 耗时{time.time() - t1}")
            return response_result
        except Exception:
            self._my_log(f"方法：{sys._getframe().f_code.co_name} 请求出现异常")
            return {"retcode": 1000, "reason": "出现异常"}

    # add course json
    def add_course_json(self, course_name, course_des, course_rank):
        """
        添加课程-json请求头
        :param course_name: 课程名称
        :param course_des: 课程描述
        :param course_rank: 课程序号
        :return: 添加结果
        """
        t1 = time.time()
        self._my_log(f"方法：{sys._getframe().f_code.co_name} 开始运行")
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
        self._my_log(f"请求头是：{headers}")
        self._my_log(f"请求体是：{payload}")
        try:
            response = requests.post(self.url.replace("api","apijson"), headers=headers, json=payload)
            response_result = response.json()
            self._my_log(f"方法：{sys._getframe().f_code.co_name} 请求成功")
            self._my_log(f"响应内容是：{response_result}, 耗时{time.time() - t1}")
            return response_result
        except Exception:
            self._my_log(f"方法：{sys._getframe().f_code.co_name} 请求出现异常")
            return {"retcode": 1000, "reason": "出现异常"}

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
        t1 = time.time()
        self._my_log(f"方法：{sys._getframe().f_code.co_name} 开始运行")
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
        self._my_log(f"请求头是：{headers}")
        self._my_log(f"请求体是：{payload}")
        try:
            response = requests.put(self.url, headers=headers, data=payload)
            response_result = response.json()
            self._my_log(f"方法：{sys._getframe().f_code.co_name} 请求成功")
            self._my_log(f"响应内容是：{response_result}, 耗时{time.time() - t1}")
            return response_result
        except Exception:
            self._my_log(f"方法：{sys._getframe().f_code.co_name} 请求出现异常")
            return {"retcode": 1000, "reason": "出现异常"}

    # delete course
    def delete_course(self, course_id):
        """
        删除课程
        :param course_id: 课程id号
        :return:  修改结果
        """
        t1 = time.time()
        self._my_log(f"方法：{sys._getframe().f_code.co_name} 开始运行")
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        payload = {
            "action": "delete_course",
            "id": course_id,
        }
        self._my_log(f"请求头是：{headers}")
        self._my_log(f"请求体是：{payload}")
        try:
            response = requests.delete(self.url, headers=headers, data=payload)
            response_result = response.json()
            self._my_log(f"方法：{sys._getframe().f_code.co_name} 请求成功")
            self._my_log(f"响应内容是：{response_result}, 耗时{time.time() - t1}")
            return response_result
        except Exception:
            self._my_log(f"方法：{sys._getframe().f_code.co_name} 请求出现异常")
            return {"retcode": 1000, "reason": "出现异常"}

    # 删除所有课程
    def delete_all_course(self):
        t1 = time.time()
        self._my_log("delete all course")
        while True:
            list_course = self.list_courses()
            if len(list_course["retlist"]) == 0:
                self._my_log("课程已清空")
                self._my_log(f"delete all courses spend time {time.time() - t1}")
                break
            for one in list_course["retlist"]:
                # print(one['id'])
                self.delete_course(one["id"])
                time.sleep(0.5)


def main():
    cm = courseMrg()
    # cm.delete_all_course()
    list_ret = cm.list_courses()
    # cm.add_course("abcd","abcde",2)
    # cm.add_course_json("abcd","abcde",2)

    # for one in list_ret["retlist"]:
    #     if one["name"] == "abcd":
    #         c_id = one["id"]
              # cm.modify_course("abcd","abcde",2, c_id)
    #         cm.delete_course(c_id)
    # cm.list_courses()

if __name__ == '__main__':
    main()
