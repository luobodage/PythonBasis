# -*- coding: UTF-8 -*-

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/05/11
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

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36'
}
# 弹幕的url地址
url = 'https://api.bilibili.com/x/v2/dm/list/seg.so?appkey=1d8b6e7d45233436&build=6235200&c_locale=zh_CN&channel=bili' \
      '&mobi_app=android&oid=336154773&pid=673024704&platform=android&s_locale=zh_CN&segment_index=1&statistics=%7B' \
      '%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%226.23.5%22%2C%22abtest%22%3A%22%22%7D&ts=1620712240' \
      '&type=1&sign=156e1da65fba7ac395aea349a55f8745 '

content = requests.get(
    url=url,
).content

print(content)
with open('danmu.txt', 'w') as f:
    f.write(content.decode('utf8'))
