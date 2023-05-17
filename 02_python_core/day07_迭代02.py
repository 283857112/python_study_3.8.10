"""
    迭代器
"""
"""
class Skill:
    pass

class SkillIterator:
    def __init__(self, skill):
        self.__skill = skill
        self.__index = 0
    def __next__(self):
        #获取下一个数据,如果没有数据了,则抛出异常
        if self.__index > len(self.__skill)-1:
            raise StopIteration
        #返回下一个数据
        temp =  self.__skill[self.__index]
        self.__index += 1
        return temp
        

class SkillManage:
    def __init__(self):
        self.__skills = []

    def add_skill(self,skill):
        self.__skills.append(skill)

    def __iter__(self):
        # 创建一个__iter__()函数,返回一个可迭代器对象.并且传递需要的数据
        return SkillIterator(self.__skills)

manager = SkillManage()
manager.add_skill(Skill())
manager.add_skill(Skill())
manager.add_skill(Skill())

iterator = manager.__iter__()

while True:
    try:
        item = iterator.__next__()
        print(item)
    except:
        print("迭代结束")
        break
        
"""

class ItertatorGraphic:
    def __init__(self, graphics):
        self.__graphics = graphics
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__graphics) - 1:
            raise StopIteration
        temp = self.__graphics[self.__index]
        self.__index += 1
        return temp

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
        return ItertatorGraphic(self.__list_graphic_manage )

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

iterator = manage.__iter__()
total_area = 0

while True:
    try:
        total_area += iterator.__next__().calculate_area()
    except StopIteration:
        print(total_area)
        print(20*20*3.14 + 20 * 10)
        break

