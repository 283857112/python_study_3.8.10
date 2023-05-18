import socket, os

def login(s):
    while True:
        name = input("Please input your name:")
        s.sendto(("L %s "%name).encode(), ADDR)
        msg,addr = s.recvfrom(128)
        if msg.decode() == "OK":
            print("你进入了聊天室")
            break
        elif msg.decode() == "name exist":
            print("Name exist! Please input again")
            continue
    return name

def chat(s, name):
    while True:
        msg = input("msg>>")
        if msg.strip() == "Q":
            s.sendto(("Q %s"%name).encode(), ADDR)
            print("退出聊天室")
            os._exit(1)
        else:
            s.sendto(("M %s %s"%(name, msg)).encode(), ADDR)
            
def recv(s):
    while True:
        msg, addr = s.recvfrom(1024)
        if msg.decode() == "EXIT":
            os._exit(1)
        print(msg.decode())
        print("msg>>", end = "")

ADDR = ("127.0.0.1",8888)
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    name = login(s)
    pid = os.fork()
    if pid == 0:
        recv(s)
    else:
        chat(s, name)

if __name__ == "__main__":
    main()
 