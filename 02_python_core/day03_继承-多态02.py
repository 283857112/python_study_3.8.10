
"""
设计:
        1.开闭原则 Open Closed Principle
          对拓展开放, 对修改关闭
          增加新功能, 不改变原有代码 

        2.类的单一职责(一个类的定义)
          一个类有且只有一个改变它的原因
        
        3.依赖倒置(依赖抽象)
          客户端代码(调用的类)尽量依赖(使用)抽象的组件.抽象是稳定的,实现是多变的.依赖父类.用父类隔离变化
          客户端 调用的是父类的方法,执行的是子类的方法
        
        4.组合复用原则
          如果仅仅为了代码复用优先选择组合复用,而非继承复用.组合的耦合性相对继承低.

        5.里氏替换
        
        6.迪米特法则(类与类交互的原则)
"""
"""
    多态:父类的同一种动作或者行为,在不同的子类上有不同的实现.
    作用:继承将相关概念的共性进行抽象,多态在共性的基础上,实现各自的变化
        增强程序扩展性.降低耦合.体现开闭原则
"""
"""
    重写:子类在实现了父类中相同的方法(方法名,参数),在调用该方法后,实际调用子类中的方法.
"""
#demo 
### 老张开车去东北

class Person:

    def __init__(self, name):
        self.name = name

    def goto(self, type, pos):
        """
        #没有隔离变化
        if isinstance(type, Car):
            type.drive(pos)
        else:
            type.fly(pos)
"""
        #隔离变化
        #调用的是父类 Vehicle的vehicle方法,实际执行子类car/plane/train的方法.
        #如果需要增加新的交通方式.只需要增加一个类即可,从父类继承重写方法即可.
        #可用用 isinstance 判断对象类型.限制调用的类对象必须从父类继承.如果传入的不是子类.则"处理"
        if isinstance(type, Vehicle):
            type.vehicle(self.name, pos)
        else:
            print("交通工具不符合要求")

class Vehicle():
    def vehicle(self,name,pos):
        #因为父类的方法是抽象的,所以没有具体代码实现.
        print("不要使用我的方法")
        raise NotImplementedError  #异常报错没有实现的错误.如果子类不重写,则异常

class Car(Vehicle):
    def vehicle(self,name,pos):
        print("%s"%name, "开车到","%s"%pos)

class Plane(Vehicle):
    def vehicle(self,name,pos):
        print("%s"%name, "坐飞机到","%s"%pos)

class Train():
    def vehicle(self,name,pos):
        print("%s"%name, "坐火车到","%s"%pos)

class Bike(Vehicle):
    def vehicle01(self,name,pos):
        print("%s"%name, "骑自行车到","%s"%pos)

lz = Person("老张")
car = Car()
plane = Plane()
train = Train()
bike = Bike()
lz.goto(car,"东北")
lz.goto(plane,"东北")
lz.goto(train,"东北")
lz.goto(bike, "东北")