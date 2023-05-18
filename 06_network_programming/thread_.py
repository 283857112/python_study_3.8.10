"""
    线程 (Thread):
        1.线程被称为轻量级的进程
        2.线程也可以使用计算机多核资源
        3.线程时系统分配内核的最小单元
        4.线程可以理解为进程的分支任务
    线程特征:
        1.一个进程中可以包含多个线程
        2.线程也是一个运行行为,消耗计算机资源
        3.一个进程中的所有线程共享这个进程的资源
        4.多个线程之间的运行的互不影响
        5.线程的创建和销毁消耗的资源远小于进程
        6.各个线程也有自己的ID等特征
"""
#demo

from threading import Thread
from time import sleep, ctime
import os
"""
def fun1():
    print("This is a thread")
    global a
    print("a:",a)
    a = 10000
a = 1

th = Thread(target=fun1)
th.start()
print("This is main thread")

th.join()
print("main a:",a)
"""

"""
自定义线程类
    创建步骤:
        1.继承 Thread类
        2.重写 __init__方法添加自己的属性,使用super加载父类属性
        3.重写run方法
    使用方法:
        1.实例化对象
        2.调用 start自动执行run方法
        3.调用join回收线程
"""
#demo

class MyThread(Thread):
    def __init__(self, sec, song):
        super().__init__()
        self.sec = sec
        self.song = song
    def run(self):
        for i in range(3):
            print("Playing %s : %s"%(self.song, ctime()))
            sleep(self.sec)

t = MyThread(3, "凉凉")
t.start()
t.join()

