# -*- coding: UTF-8 -*-


# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/1/21 18:59
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
    while True:
        udp_receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        local_addr = ('', 8899)
        udp_receive.bind(local_addr)
        recv_data = udp_receive.recvfrom(1024)
        print(f'{recv_data[1][0]}:{recv_data[1][1]}向你发送了:{recv_data[0].decode("gbk")}')
        udp_receive.close()


if __name__ == '__main__':
    main()
