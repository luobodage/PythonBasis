# -*- coding: UTF-8 -*-

import snownlp
import pandas as pd
# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/2/5 11:00
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

print(snownlp.SnowNLP("我真的好爱你").sentiments)
# values = []
# data = pd.read_csv('data.csv')
# for i in data['content']:
#     values.append(snownlp.SnowNLP(i).sentiments)
#
# data['values'] = values
# data.to_csv('data01.csv')
#
# print(data.head())