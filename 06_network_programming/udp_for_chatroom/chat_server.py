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


def login(s, name, addr):
    if name not in userdict:
        s.sendto(b"OK", addr)
        msg = ("\n%s进入了聊天室"%name).encode()
        chat(s, name, msg)
        userdict[name] = addr
        print(userdict)
    else:
        s.sendto(b"name exist",addr)

def chat(s, name, msg):
    for p, addr in userdict.items():
        if p != name:
            s.sendto(msg, addr)

def quit(s, name, addr):
    s.sendto(b"EXIT", addr)
    del userdict[name]
   

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(ADDR)
    print("waiting for connect...")
    pid = os.fork()
    if pid == 0:
        while True:
            data,addr = s.recvfrom(2048)
            mark = data.decode().split(" ")[0]
            name = data.decode().split(" ")[1]
            content = " ".join(data.decode().split(" ")[2:]).strip()
            print(mark, name, content)

            if mark == "L":
                login(s, name, addr)

            elif mark == "M": 
                content = ("\n%s说:"%name + content).encode()
                chat(s, name, content)

            elif mark == "Q":
                quit(s, name, addr)
                msg = ("\n%s退出了聊天室"%name).encode()
                chat(s, name, msg)
    else:
        while True:
            msg = input("管理员消息:")
            msg = ("M 系统管理员 %s"%msg).encode()
            s.sendto(msg, ADDR)
    s.close()


if __name__ == "__main__":
    main()