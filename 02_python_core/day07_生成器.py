"""
    生成器:能够动态(循环一次计算一次返回一次)提供数据的可迭代对象
    作用: 在循环过程中,按照某种算法推算数据,不必创建容器存储数据.从而节省内存空间.数据量越大,优势越明显.

    生成器函数:含有 yield语句的函数, 返回值为生成器对象.
    语法:
    ----创建:
        def 函数名():
            ....
            yield 数据
            ....
    ----调用:
        for 变量名 in 函数名()
            语句
"""
#demo 01
"""
    枚举函数 enumerate()
    for 变量 in enumerate(可迭代对象):
        语句
    for 索引, 元素 in enumerate(可迭代对象):
        语句
    作用:遍历可迭代对像时,可以将索引和元素组合为元组.

    zip()
    for 变量 in zip(可迭代对象1, 可迭代对象2,......)
    可以将多个可迭代对象一一对应的元素,组成一个元组
    
"""
"""
list01 = [3, 5, 78, 89, 29]
for item in list01:
    print(item)

for element in enumerate(list01):
    print(element)

for index, element in  enumerate(list01):
    print(index, element)
"""

"""
    exercise:定义一个生成器函数 my_enumerate,实现下列现象,将元素和索引合成一个元组.

"""
list01 = [3, 5, 78, 89, 29]

def my_enumerate():
    index = 0
    for item in list01:
        yield (index, item)
        index += 1

for  item in  my_enumerate():
    print(item)

# demo 02

list02 = ["孙悟空", "猪八戒", "沙僧", "唐僧"]
list03 = [101, 102, 103, 104, 105]
list04 = ["a", "b", "c"]

"""
for item in zip(list02, list03):
    print(item)
"""
def min_len(*args):
    min_len = len(args[0])
    for item in args:
        if min_len > len(item):
            min_len = len(item)
    return min_len

def my_zip(*args):
    
    for i in range(min_len(args)):
        re = []
        for j in range(len(args)):
            re.append(args[j][i])
        yield tuple(re)




    # for index in range(min(len(list02), len(list03))):
    #     yield (list02[index], list03[index])
    #     index += 1

for item in my_zip(list02,list03,list04):
    print(item)


"""
    生成器表达式
    列表推导式的形式生成可迭代对象
"""

#demo 03
list05 = [1, "ss", True, 0, 12, "zhangsan", False, 1.5, 18.3]

re = (item for item in list05 if type(item) == int)
for item in re:
    print(item)

re = (item for item in list05 if type(item) == str)
for item in re:
    print(item)


#demo 04
class SkillData:
    def __init__(self, id, name, atk_ratio, duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration

list_skill = [
    SkillData(101, "降龙十八掌", 5, 10),
    SkillData(101, "乾坤大挪移", 3, 15),
    SkillData(101, "六脉神剑", 8, 5),
    SkillData(101, "一阳指", 7, 6)
]

#获取攻击比例大于6的技能

re =(item.name for item in list_skill if item.atk_ratio > 6)
for item in re:
    print(item)