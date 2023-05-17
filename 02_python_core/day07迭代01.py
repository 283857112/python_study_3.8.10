"""
    迭代:每一次对过程的重复称为一次"迭代", 而每一次迭代得到的结果会作为下一次迭代的初始值.
        例如循环获取容器中的元素.
    
    可迭代对象 iterator --> 容器
    迭代过程 for循环的原理 容器具有 __iter__()方法
"""
# ------迭代的原理-----:
list01 = [1, 2, 15, 58, 30, 19]
# 1--> 获取迭代器
iterator = list01.__iter__()
# 2--> 循环获取下一个元素
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        print("停止迭代")
        break  
# 3--> 遇到异常停止迭代   # StopIteration:   print("停止迭代")

"""
    可迭代对象:具有__iter__()函数的对象,可以返回迭代器对象.
    语法:
        class 可迭代对象名称:
            def __iter__(self)
                return 迭代器
    使用:
        for 变量名 in 可迭代对象    
"""
#demo01

"""
#运用可迭代器原理获取元组中所有元素

turpe01 = ("铁扇公主","铁锤公主","扳手王子")

iterator01 = turpe01.__iter__()

while True:
    try:
        iterator = iterator01.__next__()
        print(iterator)
    except StopIteration:
        break

#运用可迭代器原理获取元组中所有元素

dict01 = {"铁扇公主":101,"铁锤公主":102,"扳手王子":103}

iterator01 = dict01.__iter__()

while True:
    try:
        iterator = iterator01.__next__()
        print(iterator,dict01[iterator])
    except StopIteration:
        break
"""