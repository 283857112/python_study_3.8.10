
"""
    类与类的关系
    1.泛化
        子类与父类的关系,概念的复用,耦合度最高
        B类泛化A类,意味着B类是A类的一种, B类 继承于 A类
    2.关联(聚合/组合)
        部分与整体的关系.功能的复用,变化影响一个类
        A与B关联,意味着B 是A 的一部分;在A类中包含B类型的成员
    3.依赖
        合作关系,一种相对松散的协作,变化影响一个方法
        A类依赖B类,意味A类的某些功能靠B类实现; B类型作为A类中方法的参数.并不是A的成员.

    
"""


"""
    继承多态 exercise
"""

"""
    定义图形管理器类
        1.管理所有图形
        2.提供计算所有图形总面积的方法
    具体图形: 圆形,矩形

"""
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

gm01 = GraphicManage()
circular01 = Circular(10)
rectangle01 = Rectangle(10,20)
gm01.add_graphic_to_list(circular01)
gm01.add_graphic_to_list(rectangle01)
print(gm01.calculate_total_area())

"""

"""
    定义员工管理器 employee
        1.管理所有员工
        2.计算所有员工工资

    员工:
        程序员 programmer:底薪 base_pay + 项目分红 bonus
        销售marketer:底薪 + 销售额 sales_volume
        软件测试 software_tester:底薪 + bug * 5

"""

class EmployeeManage:

    def __init__(self):
        self.__list_manage = []

    def add_to_manage(self,employee):
        self.__list_manage.append(employee)
    
    def __calculate_employee_salary(self, employee):
        return employee.calculate_salary()

    def calculate_total_salary(self):
        total_salary = 0
        for item in self.__list_manage:
            total_salary += self.__calculate_employee_salary(item)
        return total_salary
    
class Employee:
    
    def calculate_salary(self):
        pass

class Programmer(Employee):

    def __init__(self, base_pay, bonus):
        self.base_pay = base_pay
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_pay + self.bonus

class Marketer(Employee):
    def __init__(self, base_pay, sales_volume):
        self.base_pay = base_pay
        self.sales_volume = sales_volume

    def calculate_salary(self):
        return self.base_pay + self.sales_volume * 0.05

class SoftwareTester(Employee):
    def __init__(self, base_pay, bugs_count):
        self.base_pay = base_pay
        self.bugs_count = bugs_count

    def calculate_salary(self):
        return self.base_pay + self.bugs_count * 5
    
em01 = EmployeeManage()
pro01 = Programmer(10000,100000)
ma01 = Marketer(1000,2000000)
st01 = SoftwareTester(8000,1000)

em01.add_to_manage(pro01)
em01.add_to_manage(ma01)
em01.add_to_manage(st01)

print(em01.calculate_total_salary())