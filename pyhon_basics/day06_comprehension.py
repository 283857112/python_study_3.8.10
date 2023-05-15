
###
    #推导式从一个可枚举数据(列表,元组,集合,字典等)推导出一个列表,也可以推导出生成器,集合或者字典
    #推导式可以加推导条件,只对符合条件的元素推导
    #要推导出的元素使用表达式生成,可以用if else语句生成不同元素.
###
#基本推导式
#demo01 生成1-10之间数字的平方列表

print([i * i for i in range(1,11)])

#带判定条件的推导式
#demo02 生成1-10之间奇数数字的平方列表

print([i * i for i in range(1,11) if i % 2 == 1])

#在推导式中应用分支语句
#emo02 生成1-10之间奇数数字生成平方,偶数数字生成3次方的列表

print([i ** 2 if i % 2 == 1 else i ** 3 for i in range(1,11)])

#在推导式中使用函数
#推导所有1-100之间的所有质数

def is_prime_number(num):
    for i in range(3,num):
        if num % i == 0:
            return False
    return True

print([i for i in range(1,101) if is_prime_number(i)])
# print([i if is_prime_number(i) else i*3 for i in range(1,101)]) 

#生成器推导式 (元组推导式) 元组推导式和列表推导式的用法也完全相同，只是元组推导式是用 ()
#  圆括号将各部分括起来，而列表推导式用的是中括号 []，另外元组推导式返回的结果是一个生成器对象。
#将中括号变成小括号,生成器表达式 

nums = (i*i for i in range(1,10000))
print(nums.__next__())
print(nums.__next__())

#字典推导式(使用大括号,使用键值对)
#demo 生成1-10之间数字的平方一一对应的字典

print({i:i**2 for i in range(1,11)})

#集合推导式
    #使用大括号,类似于推导字典,但它是单个元素,而不是键值对
    #集合会自动过滤掉重复的元素
# print(list(set([12,19,78,90,12,19]))) 去重 转换成集合再转换回来