"""
    将函数赋值给变量，通过变量，调用函数。
    将函数作为函数的参数进行传递，将一个函数的逻辑代码，注入到另一个函数中。使该方法的适用性更广.

    def fun01():
        pass
    
    def fun02(func):
        func()

    fun02(fun01)  #执行 fun01()

"""
"""
    定义: 用一系列函数解决问题;
    ----函数可以赋值给变量,赋值后变量绑定函数
    ----允许函数作为参数传入另一个函数
    ----允许函数返回一个函数
    高阶函数: 将函数作为参数或返回值的函数
"""
#demo 
def fun01():
    print("fun01执行")
re = fun01
re()

#demo02 

list01 = [2, 10, 6, 7, 9, 18, 23, 55, 100, 3]

"""       
def find01():
    for item in list01:
        if item % 2 == 0:
            yield item

def find02():
    for item in list01:
        if item >= 10:
            yield item

def find03():
    for item in list01:
        if  10 <= item <= 50:
            yield item
""" 
def condition01(item):
    return item % 2 == 0

def condition02(item):
    return item >= 10

def condition03(item):
    return 10 <= item <= 50

def find(func):
    for item in list01:
        # "多态"
        # 调用: 具体条件的抽象
        # 执行:具体条件的函数
        if func(item):
            yield item

"""
for item in find01():
    print(item, end=" ")
print("--------------------")

for item in find02():
    print(item, end=" ")
print("--------------------")

for item in find03():
    print(item, end=" ")
print("--------------------")
"""
for item in find(condition01):
    print(item, end=" ")
print("\n")

for item in find(condition02):
    print(item, end=" ")
print("\n")

for item in find(condition03):
    print(item, end=" ")    
print("\n")

"""
    lambda  匿名函数
        语法: lambda 参数列表:函数体
        注意: 函数体自带return

    语法:
    ----定义:
        变量 = lambda 形参: 方法体
    ----调用:
        变量(实参)
    
    说明:
    ----形参没有可以不填
    ----方法体只能有一条语句,且不支持赋值语句.
"""
list02 = [2, 10, 6, 7, 9, 18, 23, 55, 100, 3]

def find_lambda(target_list, func):
    for item in target_list:
        if func(item):
            yield item


for item in find_lambda(list02, lambda item: item % 2 == 0):
    print(item, end=" ")
print("\n")

for item in find_lambda(list02, lambda item: 10 < item < 50):
    print(item, end=" ")
print("\n")