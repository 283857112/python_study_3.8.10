import os
from socket import *
ADDR = ("127.0.0.1", 18888)
s = socket()
s.connect(ADDR)

with open("/home/z/git_python_study/06_network_programming/tcp/cat.jpeg","rb") as f:
    while True:
        data = f.read(1024)
        if not data:
            break
        
        s.send(data)
    print("send success")

s.close()