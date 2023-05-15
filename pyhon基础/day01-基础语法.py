#关键字
import keyword
print(keyword.kwlist)
"""
keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 
    'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
    'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
    'lambda', 'nonlocal', 'not', 'or', 
    'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""

###===================变量=====================================
"""
    变量
    语法： 变量名称 = 对象  a = 1, b = "123", c = []  d = {}
    变量名称: 真实内存地址的别名
    赋值号 “ = ” ：将右边对象的地址复制给左边内存空间
    del 语句: del变量名
        用于删除变量，同时解除与对象的关联，如果可能则释放对象。 
"""
"""
 python 变量名称没有类型，指向的对象有类型
 基本数据类型：空值对象 None,  整型 int, 浮点型 float, 布尔型 bool, 字符串 str, 元组 Tuple
            列表 list, 字典 dictionary, 集合 set

"""
"""
Python3 的六个标准数据类型中：

    不可变数据 (3 个) : Number 数字 、String 字符串、Tuple 元组；
    可变数据 (3 个): List 列表 、Dictionary 字典 、Set 集合。 
"""
"""
    float 科学计数法
        1.23e-2 = 0.0123
        1.23e5  = 123000.0
"""
# demos

data01 = input("first: ")
data02 = input("second:")
data01,data02 = data02,data01
print(data01,data02)

###============数据类型转换及基本运算符====================
"""
    数据类型转换  
    运算符 算术运算符, 比较运算符, 增强运算符, 逻辑运算符, 成员运算符, 身份运算符
    类型转换: int(), float(), str(),.....
    算术运算符："+", "-", "*", "/", 取余数 %, 取商 //, x的y次幂"**"  
    比较运算符: >, <, ==, !=, ......  
    增强运算符: +=, -=, ......
    逻辑运算符: or, and, not
        短路逻辑: 尽量将复杂的判断放在后面（节省内存）
    成员运算符: in,  not in 返回值为bool
        in	如果在指定的序列中找到值返回 True,否则返回 False。 	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
        not in	如果在指定的序列中没有找到值返回 True, 否则返回 False。 	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。
    身份运算符: is, not is
        is	is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True,否则返回 False
        is not	is not 是判断两个标识符是不是引用自不同对象	x is not y , 类似 id(x) != id(y)。如果引用的不是同一个对象则返回结果 True，否则返回 False。 
        id()函数，可以获取变量存储的地址。
        
"""
###=======================语句====================##########
"""
    行：物理行，逻辑行
    a = 1
    b = 2
    c = 3

    a = 1; b = 2; c = 3 

    " \ " 表示折行符

    d = 1 + 2 + 3
    d = 1 + 2\
        + 3

    (),[],{}隐式换行
"""

"""
    pass语句: 填充语法空白

    选择语句: if 条件1:
                pass
            elif 条件2:
                pass
            else:
                pass

    while语句: while 条件:
                    pass
                    break  #跳转语句
    while也可以有 else语句, 不满足条件时执行一次

    for语句:用来遍历可迭代对象的数据元素    
        for 变量列表 in 可迭代对象：
            语句块
        esle:
            语句块

    break: 结束循环
    continue:结束本次循环
            
"""

#demo 在控制台中循环获取一个大于2整数，判断是否为素数

while True:
    number01 = int(input("请输入一个数字:"))
    for i in range(2,number01):
        if number01 % i == 0:
            print("不是素数")
            break
    else:
        print("是素数")