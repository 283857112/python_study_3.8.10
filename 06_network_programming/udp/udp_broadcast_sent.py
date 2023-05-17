"""
    udp应用 广播 发送端
    1. 创建udp套接字
    2. 设置套接字可以发送接收广播( socket.setsockopt())
    3. 选择接收的端口
    4. 接收广播    
"""
import socket
ADDR = ("192.168.2.255", 9999)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)



while True:
    data = input("Please input:")
    s.sendto(data.encode(), ADDR)
