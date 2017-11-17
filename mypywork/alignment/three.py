#-*- coding:utf-8 -*-

import re
import time

fo = open('C:\\Users\\Administrator\\Desktop\\基因序列\\RIB40.txt','r')
line = fo.readlines()
string = ''
for l in line:
    l = l.strip('\n')
    string += l
fo.close()

s = ''
# a = 'A'; g = 'G'; c = 'C';
# arr = {'A':1,'G':2,'C':3,'T':4}
# print arr.values()
arr = ['A','G','C','T']
save = []; m = 0
# a = arr[0]+arr[1]
# print a
#i = 0; j = 0; k = 0;
for i in range(0,4):
    for j in range(0,4):
        for k in range(0,4):
            s = arr[i]+arr[j]+arr[k]
            # print s
            save.append(string.count(s))
            # print save

# a = [i for i in range(11)]
# print a
SUM = sum(save)+0.0
print(SUM)
ratio = []
for i in save:
    i = i/SUM
    ratio.append(i)
# print ratio
fw = open('C:\\Users\\Administrator\\Desktop\基因序列\\write.txt','w+')
for i in ratio:
    print(i)
    t = str(i)
    fw.write(t)
fw.close()