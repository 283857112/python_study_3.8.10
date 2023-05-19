import multiprocessing,signal,socket,os


def test(c):
    print("%d  -- %d"%(os.getpid(),os.getppid()))
    while True:
        data = c.recv(1024)
        if not data:
            break
        c.send(b"OK")
    c.close()

ADDR = ("127.0.0.1",9999)

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
s.bind(ADDR)
s.listen(5)

while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        os._exit(1)
    except:
        continue
    
    p = multiprocessing.Process(target = test, args=(c,))
    p.daemon = True #父进程退出则子进程退出
    p.start()
    
    




