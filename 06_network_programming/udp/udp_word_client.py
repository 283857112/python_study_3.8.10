from socket import *
ADDR = ("127.0.0.1",18889)
s = socket(AF_INET, SOCK_DGRAM)

while True:
    word = input("Please input a word:")
    if word == "":
        break
    s.sendto(word.encode(),ADDR)
    msg, addr = s.recvfrom(1024)
    print(msg.decode())

