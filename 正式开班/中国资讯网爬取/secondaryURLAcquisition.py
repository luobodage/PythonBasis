# -*- coding: UTF-8 -*-

import requests
import lxml.etree as le

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/2/5 11:34
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
url = 'http://www.zguonew.com/news'
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
}


def get_reult(url):
    content = requests.get(url=url, headers=headers).content
    lxml = le.HTML(content)
    return lxml


if __name__ == '__main__':

    lxml = get_reult(url)
    level2url = lxml.xpath("/html/body/div[1]/div/div[2]/div[1]/div/a[1]/@href")
    for i, v in enumerate(level2url):
        if i == 0:
            continue
        two_url = url[:-5] + v
        print(two_url)
        lxml_01 = get_reult(two_url)
        title = lxml_01.xpath("/html/body/div/div/div/div/h1/text()")
        print(title)
