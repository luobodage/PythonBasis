# -*- coding: UTF-8 -*-
import requests
import pymongo
import lxml.etree as le
import pandas as pd

proxies = {
    'http:':''
}

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
# c = pymongo.MongoClient().get_database("豆瓣").get_collection("2021/2/5")


def dataCollection(page):
    """
    :return: 返回dict类型数据
    """
    data = {}
    id = []
    grade = []
    content_p = []
    headers = {
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://www.wikipedia.org/',
        'Connection': 'keep-alive',
    }
    # 二十页
    for i in range(page):
        url = f'https://movie.douban.com/subject/35068230/comments?start={i * 20}&limit=20&status=P&sort=new_score'

        content = requests.get(
            url=url,
            headers=headers
        ).content
        lxml = le.HTML(content)

        a = [id.append(i) for i in lxml.xpath("//*[@id=\"comments\"]/div/div/h3/span[2]/a/text()")]
        b = [grade.append(i) for i in lxml.xpath("//*[@id=\"comments\"]/div/div/h3/span[2]/span[2]/@title")]
        c = [content_p.append(i) for i in lxml.xpath("//*[@id=\"comments\"]/div/div[2]/p/span/text()")]
    data['id'] = id
    data['grade'] = grade
    data['content'] = content_p

    return data


def convertData(page):
    """
    :return: 输出data.csv文件 用pandas比较快
    """
    data = dataCollection(page)
    data_df = pd.DataFrame(data)
    data_df.to_csv('data.csv', index=False)


# def exportTodb():
#     with open('data.json', 'r') as f:
#         data = f.read()
#     c.insert_many(dict(json.dumps(data)))


if __name__ == '__main__':
    # dataCollection()
    convertData(20)

print([f'https://movie.douban.com/subject/35068230/comments?start={i * 20}&limit=20&status=P&sort=new_score' for i in
       range(10)])