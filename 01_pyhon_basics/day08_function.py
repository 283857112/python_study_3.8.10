"""
    自定义函数
    def 函数名(形式参数):
        函数体
    定义: 用于封装一个特定的功能,表示一个功能或者行为.是可以重复执行的语句块,可以被重复调用
    函数,单一功能,如多个功能需重构
    
"""
def fun01():
    """
        功能
    :param   参数描述
    :return  返回值描述
    """
    pass

def print_matrix(matrix):
    """
        打印矩阵
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j],end = " ")
        print("\n")

def transport_matrix(matrix):
    """
        转置矩阵
    """
    for r in range(len(matrix)):
        for c in range(r,len(matrix[r])):
            matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c]

square_matrix = [
    ["00","01","02","03"],
    ["10","11","12","13"],
    ["20","21","22","23"],
    ["30","31","32","33"]
]

print_matrix(square_matrix)
transport_matrix(square_matrix)
print_matrix(square_matrix)

"""
函数传参

1,不可变类型的数据传参时,函数内部不会改变原数据的值
2,可变类型的数据传参时,函数内部可以改变原数据
"""

"""
    变量作用域
"""

"""
    函数参数
        实际参数:
        1,位置实参      *list   序列实参,将序列拆分后,按位置与形参对应
        2,关键字实参    **dict  字典实参,将字典拆分后,按关键字与形参一一对应

        形式参数:
        1,缺省参数:如果没有实参,使用默认值 def fun01(a=0,b=0,c=0,d=0)
            关键字实参 + 缺省参数:调用者可以随意传递参数

        2,位置形参
        3,星号元组形参,让实参个数无限制  def fun01(*args)  用for取单个参数
        4,命名关键字形参:在星号元组形参以后的位置形参,必须使用关键字实参
        5,字典形参,要求实际参数必须使用关键字,数量不限制    def funo1(**kwargs)
"""
#demo
 
def fun01(a,b,*args,c,d,**kwargs):
    print(a,b,args,c,d,kwargs)

fun01(*[1,2,3,4,5],**{"c":6,"d":7,"e":8}) 