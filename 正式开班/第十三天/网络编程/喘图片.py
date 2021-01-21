import socket


def uploadPictures():
    udp_data = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest_addrs = ('192.168.56.1', 8800)
    with open('1.jpeg', 'rb') as f:
        content = f.read()
    udp_data.sendto(content, dest_addrs)
    udp_data.close()


if __name__ == '__main__':
    uploadPictures()
