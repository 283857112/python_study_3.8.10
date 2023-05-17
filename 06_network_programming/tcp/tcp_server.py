"""
    tcp套接字服务端流程
    socket --> bind() --> listen() --> accept --> receive/send --> close()
"""

import socket

ADDR = ("127.0.0.1", 18888)
#创建 tcp 套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 当socket关闭后,本地端用于该socket的端口号立刻就可以重用.通常来说,只有经过系统定义一段时间后才能被重用
sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  

#绑定地址
sockfd.bind(ADDR)

#设置监听 一个监听套接字可以同时连接多个客户端,也能够重复被连接
sockfd.listen(5)

while True:
#阻塞等待处理连接
    print("Waiting for connect......")
    try:
        connfd, addr = sockfd.accept() 
        print("Connect from",addr)
    except KeyboardInterrupt:
        print("Server exit")
        break
    except Exception as e:
        print(e)
        continue

    #收发消息
    while True:
        data = connfd.recv(1024)
        if not data: #如果客户端中断连接,另一端如果阻塞在recv(),此时recv会立即返回一个空字符串
            break
        print("Receive data:", data.decode())
        n = connfd.send(b"Thanks")  #如果另一段已经不存在,仍然试图通过send发送消息,则会产生 BrokenPipeErron
        print("send %d bytes"%n)

    #关闭专属客户端套接字
    connfd.close()
#关闭套接字
sockfd.close()
