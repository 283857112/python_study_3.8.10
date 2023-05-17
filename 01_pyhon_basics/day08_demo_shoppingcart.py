# import time

# for i in range(101):
#     print("\r{:3}%".format(i),end=' ')
#     time.sleep(0.05)

dict_commodity_info = {
    101:{"name":"屠龙刀","price":10000},
    102:{"name":"倚天剑","price":10000},
    103:{"name":"九阴白骨爪","price":8000},
    104:{"name":"九阳神功","price":9000},
    105:{"name":"降龙十八掌","price":8000},
    106:{"name":"乾坤大挪移","price":10000}
}
def display_commodity_list():
    for id,commodity_info in dict_commodity_info.items():
        print("商品编号：%d, %s 价格:%s" % (id, "{:<10}".format(commodity_info["name"]),"{:<15}".format(commodity_info["price"])))

"""
    购物数据结构
    [
        [id,name,price,count],
        ...
    ]
"""
def adding_to_shopping_cart(id,shopping_cart):
    for item in shopping_cart:
        if id in item:
            item[3] += 1
            return
            
    commodity_list = []
    commodity_list.append(id)
    commodity_list.append(dict_commodity_info[id]["name"])
    commodity_list.append(dict_commodity_info[id]["price"])
    commodity_list.append(1)
    shopping_cart.append(commodity_list)

def show_shopping_cart(shopping_cart):
    for item in shopping_cart:
        print(item)

def calculate_total_price(shopping_cart):
    sum_price = 0 
    for item in shopping_cart:
        sum_price += item[2] * item[3]
    return sum_price


display_commodity_list()
list_commodity_id = [101,102,103,104,105,106]
shopping_cart = []

while True:
    item = input("1键购买,2查看购物车,3键结算")
    if item == "1":
        while True:
            commodity_id = input("请输入要购买的商品编号,按回车键确认,直接按回车键退出购买页面")
            if commodity_id == "":
                break
            commodity_id = int(commodity_id)
            if commodity_id not in list_commodity_id:
                print(commodity_id)
                print("按键错误,请重新选择")
                continue
            adding_to_shopping_cart(commodity_id,shopping_cart)
            print("已加入购物车，请继续选择")
        continue
    elif item == "2":
        show_shopping_cart(shopping_cart)
        continue
    elif item =="3":
        sum_price = calculate_total_price(shopping_cart)
        print("您购买的商品一共%d元"%sum_price)
        while True:
            pay = int(input("请输入您支付的金额："))
            if pay - sum_price >= 0:
                print("支付完毕，需要找零%d元"%(pay-sum_price)) 
                break
            else:
                print("支付金额不足请重新支付")
                continue
        break
    else:
        print("按键错误,请重新输入")
        continue