"""
    udp应用 广播 接收端
    1. 创建udp套接字
    2. 设置套接字可以发送接收广播( socket.setsockopt())
    3. 选择接收的端口
    4. 接收广播    
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

s.bind(("0.0.0.0", 9999))

while True:
    msg, addr = s.recvfrom(1024)
    print(msg.decode())

