import threading, os, socket, sys, time

"""

    F : 请求文件列表
    D : 请求下载文件
    U : 请求上传文件
    Q : 退出

"""

ADDR = ("127.0.0.1",9999)

class FtpServer(threading.Thread):
    def __init__(self, c):
        super().__init__()
        self.__file_list = os.listdir("06_network_programming/ftp_test/test")
        self.__normal_file_list = self.__get_filelist()
        self.c = c
    def __get_filelist(self):
        """
            获取服务器文件列表,文件为空,返回False,不为空,则返回所有正常文件组成的列表
        """
        normal_file_list = []
        for item in self.__file_list:
            if os.path.isfile("06_network_programming/ftp_test/test/%s"%item):
                normal_file_list.append(item)   
        return normal_file_list
    
    def __is_exist(self, file_name):
        return len(self.__normal_file_list) > 0 and (file_name in self.__normal_file_list)
            
    
    def __sendfile(self, filename):
        with open("06_network_programming/ftp_test/test/%s"%filename, "rb") as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                self.c.send(data)  
            self.c.send(b"##") 
    def __recvfile(self, filename):
        with open("06_network_programming/ftp_test/test/%s"%filename, "ab+") as f:
            while True:
                data = self.c.recv(1024)
                # print(data.decode())
                if not data:
                    break
                f.write(data)
                f.flush()
    
    def run(self):
        while True:
            data = self.c.recv(1024)
            if not data:
                break
            data = data.decode().split(" ")
            print(data)
            if data[0] == "F":
                self.c.send((" ".join(self.__normal_file_list)).encode())
            elif data[0] == "D":
                if not self.__is_exist(data[1]):
                    self.c.send(b"no")
                else:
                    self.c.send(b"yes")
                    self.__sendfile(data[1])
            elif data[0] =="U":
                if self.__is_exist(data[1]):
                    self.c.send(b"no")
                else:
                    self.c.send(b"yes")
                    self.__recvfile(data[1])
            elif data[0] == "Q":
                break


def main():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind(ADDR)
    s.listen(10)

    print("waiting for connect")

    while True:
        try:
            c, addr = s.accept()
        except KeyboardInterrupt:
            os._exit(1)
        except Exception as e:
            print(e)
            continue

        print(addr)
        t = FtpServer(c)
        t.setDaemon(True)
        t.start()
        
if __name__ == "__main__":
    main()
