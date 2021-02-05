# -*- coding: UTF-8 -*-


# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/2/5 11:51
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
url = 'http://www.zguonew.com/56920.html'
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
}
import lxml.etree as le

content = requests.get(url=url,headers=headers).content
lxml_01 = lxml = le.HTML(content)
title = lxml_01.xpath("/html/body/div/div/div/div/h1/text()")
print(title)

# url = 'http://www.zguonew.com/news'
# print(url[:-5])