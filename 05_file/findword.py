"""
    从终端输入一个单词,从单词本中找到该代词,打印解释内容.如果找不到,则打印"找不到"
"""
import os


f = open("file/dict.txt","r")
while True:
    word = input("Please input a word:")
    if word == "":
        break
    for item in f:
        dictword =item.split(" ")[0]
        if dictword > word:
            print("not found")
            break
        elif word == dictword:
            print(item)
            break
        
    else:
        print("not found")
    f.seek(0, 0)
f.close()
