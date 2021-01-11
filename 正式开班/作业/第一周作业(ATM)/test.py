
import csv
import os

import pandas as pd
import pymongo
import codecs

client = pymongo.MongoClient()
c = client.get_database("ATM").get_collection('userInfo')

# c = client.ceis_nlp
# my_collection = c.twitter_tweet
def getDataFromTheDatabase():
    """
    从数据库获取数据并且生成csv文件
    :return:
    """
    # 获取数据库数据
    gen = c.find()
    data = pd.DataFrame(list(gen))
    data.to_csv('userInfo2.csv',index=None)

getDataFromTheDatabase()