# -*- coding: UTF-8 -*-


# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/1/25 9:43
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
import pymysql

# 连接数据库
conn = pymysql.connect('localhost', 'root', '1334',db='python')

# # 也可以使用关键字参数
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='yu_sq', charset='utf8')


c = conn.cursor()
sql = "select * from student "
c.execute(sql)  # 执行SQL语句
data = c.fetchall()  # 通过fetchall方法获得数据

print(data)
c.close()  # 关闭游标
conn.close()  # 关闭连接
