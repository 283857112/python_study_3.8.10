from socket import *
import struct

ADDR = ("127.0.0.1", 9999)
s = socket(AF_INET, SOCK_DGRAM)


while True:
    id  = input("请输入学生ID:")
    if id == "":
        break
    name = input("请输入学生姓名:")
    age = int(input("请输入学生年龄"))
    score = float(input("请输入学生分数"))

    data = struct.pack("i6sif" ,int(id), name.encode(), age, score)

    s.sendto(data,ADDR)

s.close()