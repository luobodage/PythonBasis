# -*- coding: UTF-8 -*-
import requests
import pymongo
import lxml.etree as le
import pandas as pd

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/2/5 9:11
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
c = pymongo.MongoClient().get_database("豆瓣").get_collection("2021/2/5")


def dataCollection():
    url = 'https://movie.douban.com/subject/35068230/comments?status=P'
    headers = {
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://www.wikipedia.org/',
        'Connection': 'keep-alive',
    }
    content = requests.get(
        url=url,
        headers=headers
    ).content
    lxml = le.HTML(content)
    data = {}
    data['id'] = lxml.xpath("//*[@id=\"comments\"]/div/div/h3/span[2]/a/text()")
    data['grade'] = lxml.xpath("//*[@id=\"comments\"]/div/div/h3/span[2]/span[2]/@title")
    data['content'] = lxml.xpath("//*[@id=\"comments\"]/div/div[2]/p/span/text()")

    return data


def convertData():
    data = dataCollection()
    data_df = pd.DataFrame(data)
    data_df.to_csv('data.csv', index=False)


# def exportTodb():
#     with open('data.json', 'r') as f:
#         data = f.read()
#     c.insert_many(dict(json.dumps(data)))


if __name__ == '__main__':
    # dataCollection()
    convertData()
