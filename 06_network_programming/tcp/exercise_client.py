from socket import socket

s = socket()
s.connect(("127.0.0.1",9999))

while True:
    msg = input("msg>>")
    s.send(msg.encode())
    print(s.recv(1024))