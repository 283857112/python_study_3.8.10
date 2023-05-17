from socket import *
import struct

ADDR = ("0.0.0.0", 9999)
s = socket(AF_INET, SOCK_DGRAM)
s.bind(ADDR)

while True:
    print("waiting for recv...")
    data, addr = s.recvfrom(1024)

    data_tuple =  struct.unpack("i6sif" ,data)
    print(data_tuple)
    with open("06_network_programming/udp/student.txt", "a+") as f:
        # f.write("123")
        f.write(str(data_tuple[0])+str(data_tuple[1].decode())+str(data_tuple[2])+str(data_tuple[3])+"\n")

s.close()