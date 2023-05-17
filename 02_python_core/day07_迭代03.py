"""
    练习: 定义 MyRange类,实现以下功能
        for item in range(10)
            print(item)
"""
"""
class IteratorMyRange():
    def __init__(self,number_range):
        self.__number_range = number_range
        self.__index = 0
    def __next__(self):
        if self.__index > len(self.__number_range) - 1:
            raise StopIteration
        temp = self.__number_range[self.__index]
        self.__index += 1
        return temp

class MyRange:
    def __init__(self,number):
        self.number = number
        self.__my_range = self.__get_range()

    ### 一次性生成几个极大数有可能导致内存不足.
    def __get_range(self):
        index = 0
        range = []
        while index < self.number:
            range.append(index)
            index += 1
        return range

    def __iter__(self):
        return IteratorMyRange(self.__my_range)
    
iterator = MyRange(10).__iter__()

while True:
    try:
        iter = iterator.__next__()
        print(iter)
    except:
        print("over")
        break
"""

"""
class IteratorMyRange():
    def __init__(self, end_number):
        self.__end_number = end_number
        self.__start_nmuber = 0
    def __next__(self):
        if self.__start_nmuber == self.__end_number:
            raise StopIteration
        temp = self.__start_nmuber
        self.__start_nmuber += 1
        return temp

class MyRange:
    def __init__(self,end_number):
        self.__end_number = end_number
   
    def __iter__(self):
        return IteratorMyRange(self.__end_number)
    
iterator = MyRange(10).__iter__()

while True:
    try:
        iter = iterator.__next__()
        print(iter)
    except:
        print("over")
        break
"""
"""
    迭代器 --> yield的转变
"""
class MyRange:
    def __init__(self,end_number):
        self.__end_number = end_number
   
    def __iter__(self):
        # return IteratorMyRange(self.__end_number)
        #### yield将以上代码改为迭代器模式 
        # yield 生成规则
        # 1.将 yield以前的语句定义在next方法中
        # 2.将 yield后面的数据作为next方法返回值      
        number = 0
        while number < self.__end_number:
            yield number
            number += 1


# iterator = MyRange(10).__iter__()

# while True:
#     try:
#         iter = iterator.__next__()
#         print(iter)
#     except:
#         print("over")
#         break

# for i in MyRange(10):
#     print(i)

"""
    exercise:图形管理器 --> yield
"""
class GraphicManage:
    
    def __init__(self):
        self.__list_graphic_manage = []

    def add_graphic_to_list(self,graphic):
        if isinstance(graphic, Graphic):
            self.__list_graphic_manage.append(graphic)

    def __calculate_graphic_area(self,graphic):
        return  graphic.calculate_area()
    
    def calculate_total_area(self):
        total_area = 0
        for item in self.__list_graphic_manage:
            total_area += self.__calculate_graphic_area(item)
        return total_area
    
    def __iter__(self):
        # return ItertatorGraphic(self.__list_graphic_manage )
        index = 0
        while index < len(self.__list_graphic_manage):
            yield self.__list_graphic_manage[index]
            index += 1


class Graphic:
    
    def calculate_area(self):
        pass

class Circular(Graphic):
    def __init__(self,radius):
        # super().__init__()
        self.radius = radius
    def calculate_area(self):
        return self.radius **2 * 3.14


class Rectangle(Graphic):
    def __init__(self, length, width):
        # super().__init__()
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
    
manage = GraphicManage()
manage.add_graphic_to_list(Circular(20))
manage.add_graphic_to_list(Rectangle(20,10))
total_area = 0
for item in manage:
    total_area += item.calculate_area()

print(total_area)