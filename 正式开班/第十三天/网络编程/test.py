# -*- coding: UTF-8 -*-


# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/1/21 18:06
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


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    dest_addr = ('192.168.56.1', 8080)
    # 发送内容 以及发送ip
    whatYouWantToSend = input('请输入你要发送的内容:')
    udp_socket.sendto(whatYouWantToSend.encode('utf8'), dest_addr)

    udp_socket.close()


if __name__ == '__main__':
    main()
