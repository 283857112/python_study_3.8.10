from socket import *
import os

def find(word):
    with open("/home/z/git_python_study/06_network_programming/udp/dict.txt") as f:
            for item in f:
                if word < item.split(" ")[0]:
                    senddata = "not found"
                    break
                elif word == item.split(" ")[0]:
                    senddata = item
                    break
            else:
                senddata = "not found"
    return senddata

ADDR = ("127.0.0.1",18889)
s = socket(AF_INET, SOCK_DGRAM)
s.bind(ADDR)

while True:
    print("waiting for connect...")
    word, addr = s.recvfrom(1024)
    word = word.decode()
    print("Receive from", addr, word)
    s.sendto(find(word).encode(), addr)        

