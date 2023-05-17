import time, os

print(time.strftime("%y-%m-%d  %H:%M:%S", time.localtime()))

f = open("file/time.txt","a+")
f.seek(0,0)
index = 1
for i in f:
    index += 1
while True:
    data = "%-2d  %s\n"%(index,time.strftime("%y-%m-%d  %H:%M:%S", time.localtime()))
    f.write(data)
    index += 1
    time.sleep(1)
    f.flush()
