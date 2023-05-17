"""
    httpserver.py  Version1.0

    1. 获取来自浏览器的请求
    2. 判断如果请求内容是 / 将 index.html返回给客户端
    3. 如果是其他, 返回内容为 404
"""
import os
from socket import *

ADDR = ("127.0.0.1",8800)

def get(data):
    return data.split("/n")[0].split(" ")[1]

def get_index(filename):
    with open(filename) as f:
        return f.read()

def response(c):
    data  = c.recv(4096)
    if get(data.decode()) == "/":
        response = """HTTP/1.1 200 OK
Content-Type:text/html

""" + get_index("06_network_programming/http/index.html")
    else:
        response = """HTTP/1.1 404 NOT
Content-Type:text/html

<h1>Not found</h1>
"""
    c.send(response.encode())


s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

while True:
    c, addr = s.accept()
    response(c)

