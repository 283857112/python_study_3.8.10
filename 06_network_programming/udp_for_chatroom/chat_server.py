"""
    类似QQ群功能
    1. 有人进入聊天室需要输入姓名,姓名不能重复
    2. 有人进入聊天室,其他人会受到通知: XXX进入了聊天室
    3. 有人发信息,其他人会受到: XXX: XXXXXXXX
    4. 有人退出聊天室,则其他人也会收到通知: XXX退出了聊天室
    5. 拓展功能: 服务器可以向所有用户发送公告:管理员消息:XXXXXX
"""
"""
    协议:
    "L":登陆
    "M":发言
    "Q":退出
"""

import socket, os, signal

signal.signal(signal.SIGCHLD, signal.SIG_IGN) #处理子进程退出,防止产生僵尸进程

ADDR = ("127.0.0.1",8888)
userdict = {}
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(ADDR)
print("waiting for connect...")
# pid = os.fork()
# if pid == 0:
while True:
    data,addr = s.recvfrom(2048)
    mark = data.decode().split(" ")[0]
    content = " ".join(data.decode().split(" ")[1:]).strip()
    if mark == "L":
        name = content
        if name not in userdict:
            s.sendto(b"OK", addr)
            userdict[name] = addr
        else:
            s.sendto(b"name exist",addr)
    elif mark == "M": 
        for name,addr in userdict.items():
            s.sendto(content.encode(),addr)

# else:
#     s.sendto(b"123")
s.close()