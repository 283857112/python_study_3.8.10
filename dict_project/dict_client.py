from socket import socket

sockfd = socket()
sockfd.connect(("127.0.0.1", 18888))

while True:
    sockfd.send("eff".encode())
    print(sockfd.recv(1024).decode())
    break

sockfd.close()

