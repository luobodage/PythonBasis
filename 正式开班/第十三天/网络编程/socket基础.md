## socket基础

###### 首先导入socket库

~~~python
import socket
~~~

###### 创建一个udp套接字

~~~python
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
~~~

###### 先写一个发送信息的

~~~python
# 从键盘获取发送数据
whatYouWantToSend = input('请输入你要发送的内容:')
# 你要发送的ip地址以及端口port 这里的ip是我的ip 端口port是自己设置的
dest_addr = ('192.168.56.1', 8080)
# 发送信息给这个ip地址
udp_socket.sendto(whatYouWantToSend.encode('gbk'), dest_addr)
~~~

###### 最后关闭这个套接字

~~~python
udp_socket.close()
~~~

###### 另起一个文件进行接收

~~~python
# 创建一个udp套接字
udp_receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 设置一个默认端口port 因为接受的时候一定要这个端口才可以接收到 而发送的话可以任意接口
local_addr = ('', 8899)
# 锁定端口为8899
udp_receive.bind(local_addr)
# 每次接收文件最大的限制单位字节(byte)
recv_data = udp_receive.recvfrom(1024)
# 返回的数据recv_data是元组类型 所以可以用下标的方式进行打印输出
print(f'{recv_data[1][0]}:{recv_data[1][1]}向你发送了:{recv_data[0].decode("gbk")}')
# 最后关闭ubp套接字
udp_receive.close()
~~~

###### 最后呈现的效果

![image-20210121195323515](https://cdn.jsdelivr.net/gh/luobodage/myimage/myimage/image-20210121195323515.png)

用我的linux系统发送内容

![image-20210121195253570](https://cdn.jsdelivr.net/gh/luobodage/myimage/myimage/image-20210121195253570.png)

windows进行接收

ps:我写了循环所以可以发送很多次 可以看出每次接受的时候端口号都是不同的 因为我们没有锁定发送的端口号 但是接收的端口号是必须锁定的 不然是发送不到的哦~

