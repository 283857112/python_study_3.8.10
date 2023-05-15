"""
    继承/多态
    继承:
        多个子类在概念上是一致的,所以就抽象出一个父类
        多个自类的共性,可以提取到父类中
    继承:
        变量
        1.子类若没有构造函数,使用父类的构造函数

        2.子类若有构造函数,则必须先调用父类的构造函数
         def __init__(self, name, score):
            super().__init__(name)
            self.score = score           
"""

#demo
class Person:
    def __init__(self,name):
        self.name = name 

    def say(self):
        print("说话")

class Student(Person):

   
    def __init__(self, name, score):
        super().__init__(name)
        self.score = score

    def study(self):
        print("学习")

class Teacher(Person):

    def __init__(self, name):
        super().__init__(name)

    def teach(self):
        print("教学")

p01 = Person("zs")
s01 = Student("ls", 100)
t01 = Teacher("ww")
#子类对象可以调用父类成员,父类对象不可以调用子类成员
s01.study()
s01.say()
t01.say()

#python内置函数
#isinstance()--判断对象是否属于一个类型

print(isinstance(s01, Teacher))
print(isinstance(s01, Person))

#issubclass()--判断一个类型是否属于另一个类型 
print(issubclass(Student, Person))
print(issubclass(Student, Teacher))

