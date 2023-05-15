"""
    内置高阶函数
"""
#demo 
class Enemy:
    def __init__(self, name, atk, denfense, hp):
        self.name = name
        self.atk = atk
        self.denfense = denfense
        self.hp = hp

    def __str__(self):
        return ("%s的攻击力是%d, 防御力是%d, 还有%d生命"%(self.name, self.atk, self.denfense, self.hp))

enemy_list = [
    Enemy("灭霸", 1000, 5000, 100000),
    Enemy("成昆", 20, 100, 1000),
    Enemy("乔峰", 100, 300, 5000),
    Enemy("虚竹", 100, 500, 3000)
]
# 内置 fiter() 函数,根据条件,筛选可迭代对象中的元素
# 获取所有 hp > 1000 的元素
for item in filter(lambda item: item.hp > 1000, enemy_list):
    print(item)

# 内置 map() 函数, 使用可迭代对象中的每个元素调用函数,返回新的迭代对象

for item in map(lambda item: item.name,enemy_list):
    print(item)

# sorted(*args, key = None)  排序

# max() 获取最大值

# min() 获取最小值

