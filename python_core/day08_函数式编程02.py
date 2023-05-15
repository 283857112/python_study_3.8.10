from list_helper import *

class Enemy:
    def __init__(self, name, atk, denfense, hp):
        self.name = name
        self.atk = atk
        self.denfense = denfense
        self.hp = hp

    def __str__(self):
        return ("%s的攻击力是%d, 防御力是%d, 还用%d生命"%(self.name, self.atk, self.denfense, self.hp))

enemy_list = [
    Enemy("灭霸", 1000, 5000, 100000),
    Enemy("成昆", 20, 100, 1000),
    Enemy("乔峰", 100, 300, 5000),
    Enemy("虚竹", 100, 500, 3000)
]

re = ListHelper.find_single(enemy_list, lambda item: item.name == "灭霸")
print(re)

#生成器属于惰性操作,具有节省内存的优点.缺点是获取结果不灵活(不能使用索引或者切片访问数据)
#将可迭代对象转换成列表属于立即操作,但是牺牲的节省内存的优点

re = ListHelper.find_all(enemy_list, lambda item: item.atk > 10)
# lre = list(re)
for item in re:
    print(item)
print("\n")

re = ListHelper.count(enemy_list, lambda item: item.hp > 0)
print(re)

if ListHelper.is_exist(enemy_list, lambda item: item.name == "成昆"):
    print("yes")
else:
    print("not")

if ListHelper.is_exist(enemy_list, lambda item: item.atk < 5 or item.denfense < 10):
    print("yes")
else:
    print("not")

print(ListHelper.get_sum_attribute(enemy_list, lambda item:item.hp))

print(ListHelper.get_all_to_list(enemy_list, lambda item:item.name))
print(ListHelper.get_all_to_list(enemy_list, lambda item:(item.hp, item.name)))

print(ListHelper.get_max_attribute(enemy_list, lambda item:item.hp))
print("------------------------------")
for item in enemy_list:
    print(item)

ListHelper.order_by_key(enemy_list, lambda item:item.denfense)
print("-------------------------------")
for item in enemy_list:
    print(item)
print("-------------------------------")