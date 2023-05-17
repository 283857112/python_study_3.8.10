"""
面向对象技术简介

    类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
    方法：类中定义的函数。
    类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
    数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
    方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
    局部变量：定义在方法中的变量，只作用于当前实例的类。
    实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
    继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
    实例化：创建一个类的实例，类的具体对象。
    对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

和其它编程语言相比，Python 在尽可能不增加新的语法和语义的情况下加入了类机制。

Python中的类提供了面向对象编程的所有基本功能：类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。

对象可以包含任意数量和类型的数据。 
"""
"""
    面向对象 Oject Oriented
        面向过程:
                分析解决问题的步骤,逐步实现
        面向对象:
                设计解决问题的对象,分配职责
"""
"""
    类:一个抽象的概念,类别
    对象:类的具体实例
    类是创建对象的模板
        --数据成员
        --方法成员
    类与类行为不同,对象与对象数据不同
"""

#demo

class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def print_info(self):
        print("%s的年龄是%d,性别是%s" %(self.name, self.age, self.sex))

p01 = Person("zs",18,"男")
p01.print_info()

"""
    类变量
    在类中，方法外定义变量。用 类名.变量名 调用
    描述所有对象的共有数据    
"""
"""
    类方法
    @classmethod
    def 方法名称(cls,其他参数):

    通过 类名.方法名 调用
    
    用来操作类变量
"""

###demo
class Pesrson:
    
    person_count = 0  #定义类变量  
    
    @classmethod      #定义类方法
    def fun(cls):
        pass

    def __init__(self) -> None:
        pass

"""
    静态方法
    静态方法既不需要操作类变量也不需要操作实例变量
    调用：通过类名调用静态方法  类名.静态方法
    面向对象开发，将函数放进类中，静态方法
"""

###demo

list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
    ["30", "31", "32", "33"]
]

class Vector2:
    """
        可以表示位置，也可以表示方向
    """
    def __init__(self,x,y):
        self.x = x
        self.y = y

    #静态方法：表示左边方向
    @staticmethod
    def left(): 
        return Vector2(0,-1)   
    
    #静态方法：表示右边方向
    @staticmethod
    def right():
        return Vector2(0,1)
    
    @staticmethod
    def up():
        return Vector2(-1,0)
    
    @staticmethod
    def down():
        return Vector2(1,0)

 #在二维列表中获取指定位置，指定方向的，指定数量的元素   
 #例如：获取list01 中 “10”，右边 3个元素 “11”，“12”，“13”
 #  vect_pos,vect_dir用类Vector2表示

class TwoDimensionalListHelper:

    @staticmethod
    def get_elements(target, vect_pos,vect_dir,count):
        re = []
        for i in range(count):
            vect_pos.x += vect_dir.x
            vect_pos.y += vect_dir.y
            element = target[vect_pos.x][vect_pos.y]
            re.append(element)
        return re

re = TwoDimensionalListHelper.get_elements(list01,Vector2(1,0),Vector2.right(),3)
print(re)

re = TwoDimensionalListHelper.get_elements(list01,Vector2(3,0),Vector2.up(),3)
print(re)
