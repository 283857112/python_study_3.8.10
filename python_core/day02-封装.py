"""
    封装
    数据角度：将一些基本数据类型复合成一个自定义类型
    行为角度：向类外提供必要的功能，隐藏实现的细节
    设计角度：分而治之，变则疏之，高内聚，低耦合
"""

"""
    __slots__= ("name","age")
    放在声明的类中，只允许类创建的对象 有 固定的实例变量
"""
#demo
class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.set_hp(hp)
       
        self.atk = atk
        self.defense = defense
    #使用方法封装变量
    def get_hp(self):
        return self.__hp
    
    def set_hp(self, value):
        if  100 <= value <= 200: 
            self.__hp = value
        else:
            raise ValueError("wrong")
    ##使用方法2封装  使用 property封装    
    def get_atk(self):
        return self.__atk
    
    def set_atk(self, value):
        if  100 <= value <= 200: 
            self.__atk = value
        else:
            raise ValueError("wrong")
        
    atk = property(get_atk,set_atk)

    #----------------
    @property 
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, value):
        if  100 <= value <= 200: 
            self.__defense = value
        else:
            raise ValueError("wrong")    



e01 = Enemy("灭霸", 140, 150,200)
print(e01.atk)
e01.atk = 180

print(e01.__dict__)