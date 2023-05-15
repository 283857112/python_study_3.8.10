"""
字符串，列表，字典，元组，集合
"""
"""
容器操作
    index:索引，访问容器元素
        正向索引从0开始，反向索引从-1开始
    slice:切片，从容器中取出相应的元素，组成一个新的容器
        [开始:结束:步长]
    数学运算符
    成员运算符
    内建函数
    len(), max(), min(), sum(),......
"""
"""
字符串：由一系列字符组成的不可变序列容器
编码函数：
    ord(字符):返回字符编码
    chr(整数):根据编码返回对应字符
转义符
    " \, \n, \t,... "
字符串格式化
    字符串%（变量） %s, %d, %f
字符串常用函数
"""
"""
列表:由一系列变量组成的可变序列容器
获取元素, 追加元素append(对象)，插入元素 insert(位置，对象)
删除元素：
list_name.remove(元素)
del list_name[索引]
for 遍历列表
    for item in list_name
    for index in range(len(list_name))

###  在对列表进行切片操作是，如果是定位修改，删除，切片不会生成一个新列表，如果是取元素，会生成一个新列表
###  切片复制一层是浅拷贝
     浅拷贝：复制过程中，只复制一层变量，不会复制深层变量绑定的对象的复制过程   
     深拷贝：复制整个依赖的变量 copy.deepcopy()

    变量 = 列表名[切片]  复制元素形成一个新列表
    列表名[切片] = 变量  修改一片元素

"""

#demo for list
#在控制台中录入学生姓名
#如果姓名重复，则提示："姓名已经存在"，不添加到列表中
#如果录入空字符串，则倒序打印所有学生

student_list = []
while True:
    name = input("请输入学生姓名:")
    if name == "":
        for index in range(-1,-len(student_list)-1,-1):
            print(student_list[index],end=" ")
        break
    if name in student_list:
        print("姓名重复，请重新输入：")
        continue
    else:
        student_list.append(name)
