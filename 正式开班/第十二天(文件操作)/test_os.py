# -*- coding: UTF-8 -*-


# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/1/19 13:09
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
# #              =
# 1.使用os,判断一个文件是否存在,如果不存在,则创建.如果存在,则显示这个文件的大小,路径,最后修改时间.
import os


# path = 'test.txt'
# if os.path.exists(path):
#     print(f"大小为:{os.path.getsize(path)}")
#     print(f"路径为:{os.path.abspath(path)}")
#     print(f"最后修改时间为:{os.path.getmtime(path)}")
# else:
#     with open(path,'w') as f:
#         f.write('我就创建一下')

# 2.创建一个多层目录 "f:/java/java1/java2"
# os.makedirs('data/data1')

# 3.删除一个给定的目录,这上目录不为空目录,使用递归来实现

# def removeDirectory(path):
#     filenames = os.listdir(path)
#     for filename in filenames:
#
#         filepath = os.path.join(path, filename)
#         if os.path.isdir(filepath):
#             removeDirectory(filepath)
#         else:
#             os.remove(filepath)
#
#
# removeDirectory('data1')
# os.removedirs('data1')

# 这个代码主要删除的是目录下的所有文件

# 4.写一个方法,可以复制一个文件
# def copy(path, copy_path):
#     with open(path, 'r') as f:
#         conten = f.read()
#     with open(copy_path, 'w') as f:
#         f.write(conten)
#
#
# copy('1.txt', '2.txt')

# 5.写一个方法,可以复制一个目录,(此目录不为空)
# os.makedirs('data/data1')
#
# # 6.写一个方法,可以将一个非空目录中的所有文件的层次显示出来；
path = 'data1'


def leve(path):
    file = os.listdir(path)
    for i in file:
        print(file)
        if os.path.isdir(os.path.join(path, i)):
            leve(os.path.join(path, i))


leve(path)
#
# def digui(index):
#     if index>0:
#         digui(index-1)
#     print(index)
# digui(10)