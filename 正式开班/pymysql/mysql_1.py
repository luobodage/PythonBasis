# -*- coding: UTF-8 -*-

import pymysql
import pandas as pd
import time

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/1/29 10:46
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

data_before = 'housing.xls'


def dataCleaning():
    """
    数据清洗
    :return: 新的csv文件
    """
    df = pd.read_excel(data_before)
    print(df.isnull().sum())
    for column in list(df.columns[df.isnull().sum() > 0]):
        mean_val = df[column].mean()
        df[column].fillna(mean_val, inplace=True)
    print(df.isnull().sum())
    df.to_csv('housing.csv')


def login_mysql(user, password):
    """
    mysql登录
    :param user: 用户名
    :param password: 密码
    :return: 返回一个游标
    """
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor,  # 指定类型
        user=user,
        password=password, )
    cursor = conn.cursor()
    cursor.execute('CREATE database house')
    cursor.execute('use house')
    return cursor, conn


def reboot_mysql(user, password):
    """
    mysql登录
    :param user: 用户名
    :param password: 密码
    :return: 返回一个游标
    """
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor,  # 指定类型
        user=user,
        password=password, )
    cursor = conn.cursor()
    cursor.execute('use house')
    return cursor, conn



def create_database():
    """
    创建数据库
    :return:
    """
    cursor, conn = reboot_mysql('root', '1334')

    try:
        cursor.execute("""
            CREATE table housing(ID INT PRIMARY KEY,
                   longitude float not null  ,
                   latitude float not null ,
                   housing_median_age int not null ,
                   total_rooms int not null ,
                   total_bedrooms float not null ,
                   population int not null ,
                   households int not null ,
                   median_income float not null,
                   median_house_value varchar(10) not null )
    """)
    except:
        print('创建失败')
    cursor.close()
    conn.close()


def readAndWriteData():
    cursor, conn = reboot_mysql('root', '1334')
    with open('housing.csv', 'r') as csv:
        data = csv.read()
        print(data.split('\n'))
        a = data.split('\n')
        print(type(data))
        for i in range(len(a) - 1):
            # print(i.split())
            print(a[i])
            b = a[i].split(',')
            print(b)
            print(b[0])
            sql = f'INSERT into house.housing VALUES({b[0]},{b[1]},{b[2]},{b[3]},{b[4]},{b[5]},{b[6]},{b[7]},{b[8]},{b[9]}) '
            cursor.execute(sql)

        # for i in data:
        #     a = i.split(',')
        #     print(a)
        #     # print(len(a))
        #     print(type(a[10]))

        # sql = f'INSERT into house.housing VALUES({str(a[0])},{str(a[1])},{str(a[2])},{str(a[3])},{str(a[4])},{str(a[5])},{a[6]},{a[7]},{str(a[8])},{str(a[9])},{str(a[10])}) '
        # sql = f'INSERT into house.housing VALUES({a}) '
        # cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    # dataCleaning()
    # login_mysql('root', '1334')
    readAndWriteData()
    # create_database()
