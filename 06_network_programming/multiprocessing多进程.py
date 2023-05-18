"""
    multiprocessing
    Process()
        创建进程对象
        参数: target 绑定要执行的目标函数
             args 元组,用于给 target函数位置传参
             kwargs  字典, 用于给target函数键值传参

    p.start()
        启动进程
    p.join([timeout])
        回收进程, 可设置超时回收时间
"""


import multiprocessing as mulpro

"""
    进程池
        创建一定数量的进程来处理时间,事件处理完进程不退出而是继续处理其他事件.直到所有事件全都处理完毕统一销毁.
    from  multiprocessing import pool
    Pool(processes):
        创建进程池对象
        参数,指定进程数量.默认根据系统自动判定

    pool.apply_async(fun, args, kwds):
        将事件加入进程池队列

    pool.close()
        关闭进程池

    pool.join()
        回收进程池中进程
"""

"""
    进程间通信(IPC)
        方式: 管道, 消息队列, 共享内存, 信号, 信号量, 套接字

"""
# 管道通信
"""
from multiprocessing import Pipe
    1.multiprocessing中管道通信只能用于有亲缘关系进程中
    2.管道对象在父进程中创建,子进程通过父进程获取

fd1,fd2 = Pipe(duplex=True)
    创建管道
    参数:默认表示双向管道,如果为False,表示单向管道
    返回值: 表示管道两端的读写对象
           双向管道均可读写, 单向管道, fd1只读, fd2只写
fd.recv()
    从管道中获得数据,返回值为获取到的数据

fd.send(data)
    向管道写入内容
"""
"""
fd1, fd2 = mulpro.Pipe()

def app1():
    print("启动app1,请登陆")
    print("请求app2 授权")
    fd1.send("app1 请求登录")#向管道写入数据
    data = fd1.recv()
    if data:
        print("登陆成功", data)

def app2():
    data = fd2.recv() #阻塞等待读取管道内容
    print(data)
    fd2.send(("Dave", "123"))

p1 = mulpro.Process(target=app1)
p2 = mulpro.Process(target=app2)
p1.start()
p2.start()
p1.join()
p2.join()
"""

#消息队列
"""
    在内存中建立队列模型,进程通过队列将消息存入,或值从队列取出完成进程间通信
    from multiprocessing import Queue
    q = Queue(maxsize = 0)
        创建队列对象
        参数为最多存放消息个数
        返回值为队列对象

    q.put(data, [block, timeout])
        向队列存入消息
        data 为要存入的内容
        block 设置是否阻塞 False为非阻塞
        timeout超时检测

    q.get([block,timeout])
        从队列取出消息
        block 设置是否阻塞 False为非阻塞
        timeout超时检测
    
    q.full()    判断队列是否为满
    q.empty()   判断队列是否为空
    q.qsize()   获取队列中消息个数
    q.close()   关闭队列
"""

#共享内存

#信号量