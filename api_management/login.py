# coding=utf-8
"""
Author:zywen
Email：1004324878@qq.com

Date:2020/3/20 21:37
Desc:
"""
import os
import requests
from pprint import pprint
from read_yaml_file import read_file


# 返回当前文件的上级目录的上级目录
config_path = os.path.dirname(os.path.dirname(__file__)) + r"/config.yml"
login_info = read_file(config_path)["login_info"]
url = login_info["login_url"]
username = login_info["username"]
password = login_info["password"]


def login_system(username,password):
    """
    登录系统
    :param username: 用户名
    :param password: 密码
    :return:
    """
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {
        "username":username,
        "password":password
    }
    response = requests.post(url,headers=headers,data=payload)
    response_result = response.json()
    pprint(response_result)

    return response_result

def main():
    login_system(username,password)

if __name__ == '__main__':
    main()