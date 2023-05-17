"""
    时间处理
"""

import time
#获取当前时间戳(从1970年1月1日到当前时间经过的秒数)
t01 = time.time()
print(t01, type(t01))

#根据当前时间戳获取一个时间元组,也可传入一个时间戳.
#(tm_year=2023, tm_mon=4, tm_mday=20, tm_hour=18, tm_min=13, tm_sec=2, tm_wday=3, tm_yday=110, tm_isdst=0)
tuple01 = time.localtime()
print(time.localtime())
print(time.localtime().tm_year)

#时间元组 --> str
str_time01 = time.strftime("%y/%m/%d %H:%M:%S",tuple01)
print(str_time01,type(str_time01))

#str --> 时间元组
print(time.strptime(str_time01,"%y/%m/%d %H:%M:%S"))

#demo
#定义一个函数,根据年月日,返回星期数.
#格式:"星期一","星期二"......

def get_week(year,month,day):
    dict_weeks ={
        0:"星期一",
        1:"星期二",
        2:"星期三",
        3:"星期四",
        4:"星期五",
        5:"星期六",
        6:"星期日"
    }
    str01 = "%d/%d/%d"%(year,month,day)
    tuple01 = time.strptime(str01, "%Y/%m/%d")
    return dict_weeks[tuple01.tm_wday]

print(get_week(2023,4,17))
