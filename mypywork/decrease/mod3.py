# -*- coding:utf-8 -*-

import re
import time



result = []
query = 'CAA'
fopen1 = open('C:\\Users\\Administrator\\Desktop\\mod3\\mod.txt','r')

star = time.clock();

for line in fopen1:
    print(line)
    print('query第一次出现位置：', line.index(query))
    print('query出现次数：', line.count(query))
    for i in re.finditer(query,line):
        print('位置区间：',i.span())
fopen1.close()

end = time.clock();
print('用时1：',(end-star)*10000)

fopen2 = open('C:\\Users\\Administrator\\Desktop\\mod3\\quchu3.txt','w')

fopen1 = open('C:\\Users\\Administrator\\Desktop\\mod3\\mod.txt','r')
string = ''
i = 0
for str in fopen1:
    #print(str)
    for s in str:
        i = i + 1
        if i % 3 != 0:
            string += s
    print(string)
    fopen2.write(string)
    string = ''
    i = 0

fopen2 = open('C:\\Users\\Administrator\\Desktop\\mod3\\quchu3.txt','r')

star = time.clock();

for line in fopen2:
    print(line)
    print('query第一次出现位置：', line.index(query))
    print('query出现次数：', line.count(query))
    for i in re.finditer(query,line):
        print('位置区间：',i.span())

end = time.clock();
print('用时2：',(end-star)*10000)