"""
    闭包
    ----三要素:
        ----必须有一个内嵌函数.
        ----内嵌函数必须引用外部函数中变量
        ----外部函数返回值必须是内嵌函数
    ----语法:
        def 外部函数名(参数):
            外部变量
            def 内部函数名(参数):
                使用外部变量
            return 内部函数名
    ----调用:
        变量 = 外部函数名(参数)
        变量(参数)    

"""
#demo 01

# def fun01():
#     a = 1
#     def fun02():
#         print(a)
#     return fun02

"""
    函数装饰器
"""
"""
def permission():
    print("权限验证")

def enter_back():
    print("进入后台")

def del_order():
    print("删除订单")

permission()
enter_back()
permission()
del_order()
"""

def permission(func):
    def wrapper(*args, **kwargs):
        print("权限验证")
        func(*args, **kwargs)
    return wrapper

@permission
def enter_back(name):
    print("%s进入后台"%name)

@permission
def del_order(name,id):
    print("%s删除了%d订单"%(name, id))

enter_back("zs")
del_order("zs", 1001)
print("----------------------------------------")
#demo 02

def dwpermission(fun):
    def wrapper(*args, **kwargs):
        print("权限验证通过")
        return fun(*args, **kwargs)
    return wrapper
@dwpermission
def deposit(name,money):
    print("%s存了%.2f钱"%(name,money))
@dwpermission
def withdraw(login_id,pwd,money):
    print("%d输入了密码%s取了%.2f钱"%(login_id,pwd, money))

def login():
    print("登陆")

deposit("zs",124.4)
withdraw(1001, "sdwf", 123.4)

login = dwpermission(login)
login()
print("----------------------------------------")

import time

def get_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        return print("程序执行了%f秒"%(end_time - start_time))
    return wrapper

@get_time
def fun01():
    time.sleep(2)
    print("fun01执行完毕")
@get_time
def fun02(a):
    time.sleep(1)
    print("fun02执行完毕,参数是", a)

fun01()
fun02(1000)