# -*- coding: UTF-8 -*-

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/04/16
# software: PyCharm
#         =    =     =
#          =   =   =
#           =  =  =
#         ===========
#         =   萝    =
#         =   卜    =
#         =   神    =
#         =   保    =
#         =   佑    =
#         =   永    =
#         =   无    =
#         =   bug  =
#          =      =
#           =    =
#              =

import requests


def get_interface(url):
    """
    源地址https://reqres.in get接口测试
    :param url:get的url
    :return:返回json
    """
    content = requests.get(
        url=url
    )
    # print(content)
    # print(content.status_code)
    # print(content.json()['total_pages'])
    # print(content.json()['data'][0]['first_name'])
    assert 200 == content.status_code
    assert 2 == content.json()['total_pages']
    assert 'Michael' == content.json()['data'][0]['first_name']
    assert 1 > content.elapsed.total_seconds()
    print('没有错误..')
    return content.json()


def post_interface(data, url):
    """
    源地址https://reqres.in post接口测试
    :param data: post的数据
    :param url: post的url
    :return: 返回jason
    """
    content = requests.post(
        url=url,
        data=data
    ).json()
    # print(content)
    return content


if __name__ == '__main__':
    # get请求
    get_result = get_interface('https://reqres.in/api/users?page=2')

    data = {

        "name": "luoboovo",
        "job": "python工程师"

    }
    # post接口
    post_result = post_interface(data, 'https://reqres.in/api/users')
