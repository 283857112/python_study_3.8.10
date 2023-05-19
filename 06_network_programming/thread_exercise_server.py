import threading, os
from socket import *

def test(c):
    print("%d  -- %d"%(os.getpid(),os.getppid()))
    while True:
        data = c.recv(1024)
        if not data:
            break
        c.send(b"OK")
    c.close()

ADDR = ("127.0.0.1",9999)

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

s.bind(ADDR)
s.listen(5)

while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        os._exit(1)
    except:
        continue
    
    t = threading.Thread(target = test, args=(c,))
    t.setDaemon(True) #父进程退出则子进程退出
    t.start()
    