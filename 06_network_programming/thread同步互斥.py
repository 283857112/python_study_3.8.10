"""
    线程可以通过全局变量进行通信
    同步: 同步是一种协作关系,为完成操作,多进程或者线程之间形成一种协调,按照必要的步骤有序执行操作
    互斥: 互斥是一种制约关系,当一个进程或者线程占有资源时会进行加锁处理,此时其他进程或者线程就无法操作该资源,直到解锁后才能操作
"""

# event
from threading import Thread, Event
# e = Event() #创建线程 event对象
# e.wait()    #阻塞等待e被set,可设置超时时间参数
# e.set()     #设置e,使wait结束阻塞
# e.clear()   #使e回到未被设置状态
# e.is_set()  #查看当前e是否被设置

"""
s = None
e = Event()

def yangzirong():
    print("子荣前来拜山头:")
    global s
    s = "天王盖地虎"
    e.set()  # 擦作完共享资源 e

t = Thread(target=yangzirong)
t.start()
print("土匪盘问中......")
e.wait()  #等待 e.set()后结束阻塞
if s == "天王盖地虎":
    print("宝塔镇河妖")
    print("有惊无险,通过敌人盘问,成功打入敌人内部")
else:
    print("出现问题") 
"""
# lock
from threading import Lock

# lock = Lock() #创建锁对象
# lock.acquire() #上锁,如果lock已经上锁再调用会阻塞
# lock.release() #解锁
"""
a = b = 0 

lock = Lock()

def  fu():
    global a, b
    while True:
        lock.acquire()
        if a != b:
            print("a: %d, b: %d"%(a,b))
        lock.release()
t = Thread(target=fu)
t.start()
while True:
    # with 语句,执行上锁解锁
    with lock:
        a += 1
        b += 1

t.join()
"""

"""
死锁及其处理
    死锁时指两个或两个以上线程在执行过程中,由于竞争资源或者由于彼此通信而造成的一种阻塞的现象.若无外力作用,他们都无法推进下去.
"""