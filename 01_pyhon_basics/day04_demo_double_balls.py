"""
    彩票--双色球 Version 1.0
"""

import random
from time import sleep

def is_winning(buy,sys):
    blue_flag = 0
    red_ball_count = 0
    if buy[6] == sys[6]:
        blue_flag = 1
    for i in buy:
        if i in sys[0:5]:
            red_ball_count += 1
    
    if blue_flag == 1 and red_ball_count == 6:
        print("获得一等奖")
    elif blue_flag == 0 and red_ball_count == 6:
        print("获得二等奖")
    elif blue_flag == 1 and red_ball_count == 5:
        print("获得三等奖")
    elif (blue_flag == 1 and red_ball_count == 4) or (blue_flag == 0 and red_ball_count == 5):
        print("获得四等奖")
    elif (blue_flag == 1 and red_ball_count == 3) or (blue_flag == 0 and red_ball_count == 4):
        print("获得五等奖")
    elif (blue_flag == 1 and red_ball_count == 2) or (blue_flag == 1 and red_ball_count == 1) or (blue_flag == 1 and red_ball_count == 0):
        print("获得六等奖")
    else:
        print("没有中奖")

double_ball_list = []

while len(double_ball_list) < 6:
    try:
        redball_num = int(input("请输入第%d个红球号码:"%(len(double_ball_list) + 1)))
        if redball_num > 33 or redball_num < 1:
            print("红球号码不在范围内,请重新输入:")
        elif redball_num in double_ball_list:
            print("号码重复,请重新输入:")
        else:
            double_ball_list.append(redball_num)
    except Exception as e:
        print(e)
        continue
double_ball_list.sort()
#print(double_ball_list)
while True:
    blueball_num = int(input("请输入蓝球号码:"))
    if blueball_num > 16 or blueball_num < 1:
        print("蓝球号码不在范围内,请重新输入:")
        continue
    else:
        double_ball_list.append(blueball_num)
        break
print("您购买的彩票号码为:",double_ball_list)  
print("------------------------------------------")
print("系统摇奖中........")
print("------------------------------------------")
sleep(2)
sys_double_ball_list = []
while len(sys_double_ball_list) < 6:
    sys_redball_num =  random.randint(1, 33)
    if sys_redball_num not in sys_double_ball_list:
        sys_double_ball_list.append(sys_redball_num)
sys_double_ball_list.sort()
sys_double_ball_list.append(random.randint(1,16))
print("系统摇奖的彩票号码为:",sys_double_ball_list) 
print("正在为您计算奖项........")
print("------------------------------------------")
sleep(2)
is_winning(double_ball_list, sys_double_ball_list)