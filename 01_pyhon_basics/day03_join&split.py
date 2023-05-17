"""
    将多个字符串拼接成一个
    result = "连接符".join(列表)

    将一个字符串拆分成多个
    列表 = "字符串".split("分隔符")
"""
# 拼接字符串“0123456789”
#1
num_list = []
for i in range(10):
    num_list.append(str(i))
result = "".join(num_list)
print(type(result),result)

#2 字符串不可变，每一次拼接生成一个新对象。浪费内存。不建议使用2方法。
#  字符串频繁拼接浪费内存
result = ""
for i in range(10):
    result += str(i)
print(result)

## 在控制台中循环输入字符串，如果输入空则停止。最后打印所有内容
"""
str_list = []
while True:
    str01 = input("请输入字符串:")
    if str01 == "":
        break
    str_list.append(str01)
print("".join(str_list))

"""
## 英文单词翻转
## "how are you" -> "you are how"
word_str = "how are you"
word_list = word_str.split(" ")
word_list.reverse()
word_str = " ".join(word_list)
word_str1 = " ".join(word_list[-1:-len(word_list)-1:-1])
print(word_str, word_str1)