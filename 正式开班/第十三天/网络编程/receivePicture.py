# -*- coding: UTF-8 -*-


# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/1/21 19:20
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
import socket


def receivePicture():
    while 1:
        udp_data = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        local_addrs = ('', 8009)
        udp_data.bind(local_addrs)
        reva_data = udp_data.recvfrom(50)
        print(reva_data[0])
        with open('10.jpeg', 'ab') as f:
            f.write(reva_data[0])
        # if reva_data == None:
        #     break
        # data.append(reva_data[0])

        #

        udp_data.close()


if __name__ == '__main__':
    # receivePicture()
    # 4，    对压缩文件进行加密操作和解密操作
    # （提示，以字节形式读取指定压缩文件，交换两个
    # 固定位置的字节编码，再写到新位置，删除源文件，
    # 解密即为重复加密过程）
    import os
    def encryption():
        with open('test.txt','rb') as f:
            a = f.read()
        with open('test_encryption.txt','wb') as f :
            b = a[len(a)//2:] + a[:len(a)//2]
            f.write(b)
        os.remove('test.txt')
    def decrypt():
        with open('test_encryption.txt','rb') as f:
            a = f.read()
        with open('test_decrypt.txt', 'wb') as f:
            b = a[len(a) // 2:] + a[:len(a) // 2]
            f.write(b)
    # # encryption()
    # decrypt()
    # 5，    定义类A，A中具有属性，id
    # name
    # age
    # sex
    # 定义类B，B中具有方法add_excel(a), 其中参数a是类A的对象
    # 方法具有像excel表格中插入a数据的功能
    import pandas as pd


    class A:
        def __init__(self, id, name, age, sex):
            self.id = id
            self.name = name
            self.age = age
            self.sex = sex


    class B(A):
        def add_excel(self):
            data = pd.DataFrame([self.id, self.name, self.age, self.sex])
            data.to_excel('test.xls')
    b = B(1,'name',18,1)
    b.add_excel()
