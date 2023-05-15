"""
    元组：由一系列变量组成的不可变系列容器（一旦创建，不可以再添加/删除/修改元素）
"""
"""
tuple01 = tuple()
tuple02 = tuple(["a","b"])  # 列表 - 元组
list01 = list(tuple02)      # 元组 - 列表

"""

#demo 
#在控制台中录入日期（年，月，日，）计算这是这一年的第几天

year = int(input("请输入年份:"))
month = int(input("请输入月份:"))
day = int(input("请输入日:"))
sum_of_days = 0

day_of_month = (31,28,31,30,31,30,31,31,30,31,30,31)

for i in range(month-1):
    sum_of_days += day_of_month[i]

print("这是这一年的第%d天"%(sum_of_days+day))


"""
    字典 dict
    1.由一系列键值对（key : value）组成的可变映射容器
    2.映射：一对一的对应关系，且每条记录无序
    3.键必须唯一且不可变（字符串/数字/元组），值没有限制
"""
#创建
"""
dict01 = {}
dict02 = dict()
dict03 = {"a":"b","c":"d"}
dict04 = dict([("a","b"),("c","d")])
"""

#查找----根据key查找value 字典名[key]
#如果 key 不存在，则报错，查找前须判断
# if key in 字典名：
#     字典名[key]

#遍历
#for key in 字典名  得到key
#for value in 字典名.values() 得到值
#for key,value in 字典名.items() 得到键值元组

#demo01 在控制台中循环录入商品信息（名称，单价），如果名称输入为空，则停止录入。将所有信息打印出来
"""
commodity_dict = {}
while True:
    name = input("请输入商品名称：")
    if name == "":
        break
    price = float(input("请输入单价"))
    if name not in commodity_dict:
        commodity_dict[name] = price
for key,value in commodity_dict.items():
    print(key,value)
"""
#demo02 在控制台中循环录入学生信息（姓名，年龄，成绩，性别），如果名称输入空字符，则停止录入，将所有信息打印出来
#数据结构{key:[]} 字典内嵌列表
"""
dict_student_info = {}
while True:
    name = input("请输入学生姓名:")
    if name == "":
        break
    if name not in dict_student_info:
        list_student = []
        age = int(input("请输入学生年龄:"))
        score = int(input("请输入学生成绩:")) 
        sex = input("请输入学生性别:")
        list_student.append(age)  
        list_student.append(score)  
        list_student.append(sex)  
        dict_student_info[name] = list_student
     #### dict_student_info[name] = [age,score,sex] 简单，比原代码方便
for name,stu in dict_student_info.items():
    print(name,stu)
"""

#demo02 在控制台中循环录入学生信息（姓名，年龄，成绩，性别），如果名称输入空字符，则停止录入，将所有信息打印出来
#数据结构{key:{}} 字典内嵌字典
"""
dict_student_info = {}
while True:
    name = input("请输入学生姓名:")
    if name == "":
        break
    if name not in dict_student_info:
        dict_student = {}
        age = int(input("请输入学生年龄:"))
        score = int(input("请输入学生成绩:")) 
        sex = input("请输入学生性别:")
        dict_student["age"] = age  
        dict_student["score"] = score  
        dict_student["sex"] = sex  
        dict_student_info[name] = dict_student
for name,stu in dict_student_info.items():
    # print(name,stu)
    print("%s的年龄是%d,成绩是%d,性别是%s"%(name,stu["age"],stu["score"],stu["sex"]))
"""

#demo03 在控制台中循环录入学生信息（姓名，年龄，成绩，性别），如果名称输入空字符，则停止录入，将所有信息打印出来
#数据结构[{}] 列表内嵌字典

list_student_info = []
while True:
    name = input("请输入学生姓名:")
    if name == "":
        break
    age = int(input("请输入学生年龄:"))
    score = int(input("请输入学生成绩:")) 
    sex = input("请输入学生性别:")
    list_student_info.append({"name":name,"age":age,"score":score,"sex":sex})
for item in list_student_info:
    # print(name,stu)
    print("%s的年龄是%d,成绩是%d,性别是%s"%(item["name"],item["age"],item["score"],item["sex"]))