# coding=utf-8
"""
Author:zywen
Email：1004324878@qq.com

Date:2020/3/20 21:37
Desc:
"""
import requests
import time
from pprint import pprint
from global_params import yaml_content
from common.log import Log


login_info = yaml_content["login_info"]
url = login_info["login_url"]
username = login_info["username"]
password = login_info["password"]
logger = Log()


def login_system(username,password):
    """
    登录系统
    :param username: 用户名
    :param password: 密码
    :return:
    """
    t1 = time.time()
    logger.info("开始调用登录接口".center(50,"#"))
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    logger.info(f"the headers = {headers}")
    payload = {
        "username":username,
        "password":password
    }
    logger.info(f"the body = {payload}")
    response = requests.post(url,headers=headers,data=payload)
    response_result = response.json()
    # pprint(response_result)
    logger.info(f"response result is {response_result}, spend time {time.time() - t1}")
    logger.info("login success".center(50,"#"))
    return response_result

def main():
    login_system(username,password)

if __name__ == '__main__':
    main()