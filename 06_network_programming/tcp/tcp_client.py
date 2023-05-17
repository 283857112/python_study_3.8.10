"""
    tcp套接字客户端流程
    socket --> bind()(可选) --> connect() --> receive/send --> close()
"""

import socket

#创建 tcp 套接字 //只有相同类型的套接字才能进行通信
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#绑定地址(可选),客户端可以不用绑定地址端口
# sockfd.bind(("127.0.0.1", 18888))

#请求连接 sockfd.connect( server_addr )
print("Waiting for connect......")
sockfd.connect(("127.0.0.1", 18888))

#发送消息
while True:
    data = input("Msg>>")
    if not data:
        break
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    print("Receive data:", data.decode())

#关闭套接字
sockfd.close()
