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
    udp_data = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_addrs = ('', 8800)
    udp_data.bind(local_addrs)
    reva_data = udp_data.recvfrom(4096)
    with open('2.jpeg', 'wb') as f:
        f.write(reva_data[0])
    udp_data.close()


if __name__ == '__main__':
    receivePicture()
