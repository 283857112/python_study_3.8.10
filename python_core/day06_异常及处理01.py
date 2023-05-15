"""
    异常: 运行检测到的错误
         当异常发生是,程序不再往下执行,而转到函数的调用语句

    常见异常类型:
         名称异常:  NameError  变量未定义
         类型异常:  TypeError  不用类型数据进行计算
         索引异常:  IndexError 超出索引范围
         属性异常:  AttributeError      对象没有对应名称的属性
         键异常:    KeyError           没有对应名称的键
         未实现异常: NotImplementError  尚未实现的方法
         异常基类:   Exception
"""
"""
    异常处理
    try:
        可能触发异常的语句
    except: 错误类型  [ as 变量1]
        处理语句1
    except: 错误类型  [ as 变量2]
        处理语句2
    ....
    else:
        未发生异常的语句
    finally:
        无论是否发生异常都要执行的语句

"""
"""
    raise 语句:
    1.作用:抛出一个错误,让程序进入异常状态
    2.目的:在程序调用层数较深时,向主函数传递错误信息.通过人为抛出异常,可以直接传递错误信息.
"""
#demo
def div_app(apple_count):
    person_count = int(input("请输入人数:"))
    re = apple_count / person_count
    print("每个人分%d个苹果"%(re))
"""
try:
    div_app(10)
except:    #异常范围太宽泛,建议具体项
    print("wrong")
"""

"""
try:
    div_app(10)
except ValueError:
    print("输入错误")
except ZeroDivisionError:
    print("人数必须是大于0的整数")
except:
    print("未知错误")
"""

"""
try:
    div_app(10)
except ValueError:
    print("输入错误")
except ZeroDivisionError:
    print("人数必须是大于0的整数")
except:
    print("未知错误")
else:
    #pass
    print("没有出错") #没有出错的代码
"""
try:
    div_app(10)
except ValueError:
    print("输入错误")
except ZeroDivisionError:
    print("人数必须是大于0的整数")
except:
    print("未知错误")
else:
    #pass
    print("没有出错") #没有出错的代码
finally:    #可以不处理异常,直接 try  finally.不能处理异常,但一定要执行的代码定义的语句中
    print("无论是否异常一定会执行的代码")
#------------------------------------------
#如果出现异常,不处理,后续代码无法进行

print("后续逻辑")