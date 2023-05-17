
"""
    内置函数
"""

class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
    
    #内置函数 __str__  将对象转换成自定义格式的字符串
    def __str__(self):  
        return "%s,%d,%d,%d"%(self.name, self.hp, self.atk, self.defense)

    #内置函数 __repr__ 将对象转换成解释器可以识别的字符串   
    def __repr__(self):
        return "Enemy(\"%s\",%d,%d,%d)"%(self.name, self.hp, self.atk, self.defense)


e01 = Enemy("灭霸", 10000, 5000, 100000)
print(str(e01))

str02 = repr(e01)
print(str02)

# eval(str) 函数, 执行str代码
e02 = eval(str02)
e02.name = "灭霸之霸"
print(str(e02))

print(id(e01),id(e02))

"""
    运算符重载
"""