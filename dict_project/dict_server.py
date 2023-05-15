import socket
import os

socketfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socketfd.bind(("127.0.0.1",18888))
socketfd.listen(5)

while True:
    print("waiting for connect...")
    try:
        connfd, addr = socketfd.accept()
        print("connect from", addr)
    except KeyboardInterrupt:
        print("Server exit")
        break
    except Exception as e:
        print(e)
        continue

    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print("receiver data", data.decode())
        connfd.send(b"OK")
    
    connfd.close()

socketfd.close()