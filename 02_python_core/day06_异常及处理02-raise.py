"""
    raise 语句:
    1.作用:抛出一个错误,让程序进入异常状态
    2.目的:在程序调用层数较深时,向主函数传递错误信息.通过人为抛出异常,可以直接传递错误信息.
"""
"""
    自定义异常类
    class 类名Error(Exception):
        def __init__(self, 参数):
            super().__init__(参数)
            self.数据 = 参数
    
    调用:

"""
"""
    学生信息管理系统,异常处理.
"""
#demo
class PersonErron(Exception):
    def __init__(self, msg, age, line):
        self.msg = msg
        self.age = age
        self.line = line

class Person:
    def __init__(self, age):
        self.age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        if 20 < value <30:
            self.__age = value
        else:
            # raise ValueError("年龄不在范围内") #主动抛出一个异常
            raise PersonErron("错了","年龄不对","37行代码错误")  
                  #用自定义异常类PersonErron封装需要传递的数据

#获取异常,将age异常直接传递给一个对象
try:  
    p01 = Person(100)
# except ValueError:
#     print("年龄不在范围内")
except PersonErron as p:
    print(p.age, p.msg, p.line)

