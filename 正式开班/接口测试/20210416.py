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

data = {

    "name": "luoboovo",
    "job": "python工程师"

}


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
    # assert 200 == content.status_code
    # assert 2 == content.json()['total_pages']
    # assert 'Michael' == content.json()['data'][0]['first_name']
    # assert 10 > content.elapsed.total_seconds()
    # print('GET没有错误..')
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
    )
    # print(content)
    assert 201 == content.status_code
    assert 'python工程师' == content.json()['job']
    assert 'luoboovo' == content.json()['name']
    assert 5 > content.elapsed.total_seconds()
    print('POST没有错误..')
    return content.json()


def delete_interface(url):
    """
    删除
    :param url: 删除的地址
    :return: 返回空
    """
    content = requests.delete(
        url=url
    )
    return content.text


def put_interface(data, url):
    content = requests.put(
        url=url,
        data=data
    )
    return content.json()


def patch_interface(data, url):
    content = requests.put(
        url=url,
        data=data
    )
    return content.json()


if __name__ == '__main__':
    # get请求
    get_result = get_interface('https://reqres.in/api/users?page=2')
    get_result_01 = get_interface('https://reqres.in/api/users?delay=3')
    print(get_result_01)
    # post接口
    post_result = post_interface(data, 'https://reqres.in/api/users')
    #delete接口
    delete_result = delete_interface('https://reqres.in/api/users/2')
    # put接口
    put_result = put_interface(data, 'https://reqres.in/api/users/2')
    # patch接口
    patch_result = patch_interface(data, 'https://reqres.in/api/users/2')
