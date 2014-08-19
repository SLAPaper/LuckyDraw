from __future__ import print_function
import io
import os
import random

file = open("input.txt", "r" ).read()
try:
    f = io.StringIO(file.decode("utf_8"))
except UnicodeDecodeError:
    try:
        f = io.StringIO(file.decode("gbk"))
    except UnicodeDecodeError:
        sys.exit("Check if your input.txt is encoded with UTF-8 or GBK")

data = {}
#为了能用py2exe编译为exe文件，因此暂时只能使用python2.7
s = f.readline()
while s != "":
    l = s.split()
    data[l[0]] = float(l[1])
    s = f.readline()

#求总权
total = 0.0
for x in data.values():
    total += x

#中文输出使用u前缀确保是unicode字符串
print(u"你输入的内容如下：\n")
print(u"总权重：%f\n" % total)
print(u"名字\t权重")
for x in data.items():
    print(u"%s\t%f" % x)

#求出幸运数
lucky = random.uniform(0.0,total)

#找出谁落在幸运数上，为了避免浮点误差所以使用了0.01的区分度
for x in data.items():
    if lucky - x[1] < 0.01:
        print(u"\n被抽中的是：%s" % x[0])
        break
    else:
        lucky -= x[1]

#还是python3大法好。。。
f.close()
