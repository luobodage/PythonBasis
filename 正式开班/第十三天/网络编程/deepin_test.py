import socket


def main():
    # while True:
    ip_addrs = ('192.168.56.1', 8899)
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cotent = input('请输入您要发送的内容:')
    udp.sendto(cotent.encode('gbk'), ip_addrs)
    udp.close()


if __name__ == '__main__':
    main()
