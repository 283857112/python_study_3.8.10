import socket, os

ADDR = ("127.0.0.1",9999)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect(ADDR)

class FtpClient:
    def __init__(self, s):
        self.s = s

    def get_filelist(self):
        self.s.send(b"F")
        msg = self.s.recv(1024)
        if msg.decode() == "":
            return None
        else:
            return (msg.decode()).split(" ")
        
    def download(self, filename):
        self.s.send(("D %s"%filename).encode())
        msg = self.s.recv(1024)
        print(msg.decode())
        if msg.decode() == "no":
            return False
        else:
            print("downloading.....")
            with open("/home/z/git_python_study/06_network_programming/ftp_test/test_client/%s"%filename, "ab+") as f:
                while True:
                    data = self.s.recv(1024)
                    if data == b"##":
                        break
                    f.write(data)
                    
            print("download success")

    def upload(self, filename):
        self.s.send(("U %s"%filename).encode())
        msg = self.s.recv(1024)
        print(msg.decode())
        if msg.decode() == "no":
            return False
        else:
            print("uploading.....")
            filepath = "06_network_programming/ftp_test/test_client/%s"%filename
            with open(filepath, "rb") as f:
                while True:
                    data = f.read(1024)                  
                    if not data:
                        break
                    self.s.send(data)
            print("upload success")
    def quit(self):
        self.s.send(b"Q")

class View:
    def __init__(self, s):
        self.fc = FtpClient(s)
    
    def file_view(self):
        data = self.fc.get_filelist()
        if not data:
            while True:
                print("======服务器文件列表======")
                print("** 服务器暂时没有任何文件! ")
                print("===========================")
                print(">>> 1 返回 | 2 上传文件")
                se1 = input("请输入选项:")
                if se1 == "1":
                    return
                elif se1 == "2":
                    self.upload_view()
                else:
                    print("请输入正确选项")
                    continue
        else:
            while True:
                print("======服务器文件列表======")
                for item in data:
                    print("** %s"%item)
                print("===========================")
                print(">>> 1 返回 | 2 下载文件 | 3 上传文件")
                se1 = input("请输入选项:")
                if se1 == "1":
                    return
                elif se1 == "2":
                    self.download_view()
                elif se1 == "3":
                    self.upload_view()
                else:
                    print("请输入正确选项")
                    continue

    def download_view(self):    
        while True:
            file_name = input("请输入要下载的文件名字:")
            if not self.fc.download(file_name.strip()):
                print("要下载的文件安不存在,请重新输入")
                continue
            else:
                self.fc.download(file_name.strip())
                break
    
    def upload_view(self):
        # while True:
        #     file_name = input("请输入需要上传文件名字:")
        #     if not self.fc.upload(file_name.strip()):
        #         print("服务器存在该名字文件,请确认后重新输入!")
        #         continue
        #     else:
        #         self.fc.upload(file_name.strip())
        #         break
        file_name = input("请输入需要上传文件名字:")
           
        self.fc.upload(file_name.strip())
             

    def quit(self):
        self.fc.quit()
    
    def main_view(self):
        while True:
            print("======欢迎登录ftp服务======")
            print("**  1  查看服务器文件")
            print("**  2  上传文件至服务器")
            print("**  3  退出")
            print("===========================")
            se = input("请输入选项:")
            if  se == "1":
                self.file_view()
            elif se == "2":
                self.upload_view()
            elif se == "3":
                self.quit()
                os._exit(1)
            else:
                print("请输入正确选项!")
                continue
        
if __name__ == "__main__":
    view = View(s)
    view.main_view()