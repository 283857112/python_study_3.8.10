import socket, os

ADDR = ("127.0.0.1",8888)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    name = input("Please input your name:")
    s.sendto(("L %s"%name).encode(), ADDR)
    msg,addr = s.recvfrom(128)
    if msg.decode() == "OK":
        print("你进入了聊天室")
        break
    elif msg.decode() == "name exist":
        print("Name exist! Please input again")
        continue
while True:
    msg = input("msg>>>")
    if msg.strip == "Q":
        s.sendto(("Q"%msg).encode(), ADDR)
        os._exit()
    else:
        s.sendto(("M %s"%msg).encode(), ADDR)
    


# while True:
#     s.sendto("data",ADDR)

#     msg,addr = s.recvfrom(2048)
# s.close