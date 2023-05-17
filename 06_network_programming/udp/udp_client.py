"""
    udp套接字客户端
"""
import socket

#服务器地址
ADDR = ("127.0.0.1", 18889)

#创建数据报套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#消息收发
"""
    data, addr = sockfd.recvfrom(buffersize)
    data: 接收到的内容
    addr: 发送消息的地址

    n = sockfd.sendto(data, addr)
    data: 发送的消息
    addr: 目标地址
    返回值 n : 发送的字节数
"""
while True:
    data = input("Msg>>")
    if not data:
        break
    sockfd.sendto(data.encode(), ADDR)

    msg, addr = sockfd.recvfrom(1024)
    print("收到的消息",addr, msg.decode())

    

#关闭套接字
sockfd.close()