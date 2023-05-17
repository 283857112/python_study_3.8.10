import os
from socket import *

ADDR = ("127.0.0.1", 18888)

s = socket(AF_INET, SOCK_STREAM)

s.bind(ADDR)

s.listen(5)

while True:
    print("waiting for connect...")
    try:
        c, addr = s.accept()
    except Exception as e:
        print(e)
        continue
    
    with open("06_network_programming/tcp/cat_copy.jpeg","ab+") as f:
        print("Receive file from",addr)
        while True:
            data = c.recv(1024)
            if not data:
                break
            f.write(data)
        c.close




