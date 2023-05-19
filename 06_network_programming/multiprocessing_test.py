"""
    创建两个进程 ,分别复制一个文件的上下半部分,将复制内容放到两个新的文件中
"""
from multiprocessing import Process
import os

file = "06_network_programming/cat1.jpg"
print(os.path.getsize(file))

def get_(file, area):
    size = os.path.getsize(file)
    with open(file, "rb") as f:
        if area == "top":
            data = f.read(size//2)
            with open("06_network_programming/cat_top.jpg","wb") as f2:
                f2.write(data)
            print(os.path.getsize("06_network_programming/cat_top.jpg"))
        elif area == "bottom":
            f.seek(size//2,0)
            data = f.read()
            with open("06_network_programming/cat_bottom.jpg","wb") as f2:
                f2.write(data)
            print(os.path.getsize("06_network_programming/cat_top.jpg"))

p1 = Process(target = get_, args=(file, "top"))
p2 = Process(target = get_, args=(file, "bottom"))

p1.start()
p2.start()

p1.join()
p2.join()