import os 

filename = input("please input a file name:")

try:
    f = open(filename,"rb")
except FileNotFoundError as e:
    print(e)
else:
    f2 = open("file/123.jpeg","wb")
    while True:
        data = f.read()
        if not data:
            break
        f2.write(data)
    f.close
    f2.close