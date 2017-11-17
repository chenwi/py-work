#-*- coding:utf-8 -*-

import re
import time
import numpy as np
star = time.clock()
f = open('C:\\Users\\Administrator\\Desktop\基因序列\\442.txt')  #读取序列
line = f.readlines()
string = ''
for l in line:
    l = l.strip('\n')
    string += l
sub = ''#64种排列
arr = ['A','G','C','T']
save = [] #记录每种多连核苷酸出现的次数
m = 0 #记录基因序列数量
s = ''#每个基因序列，fasta格式
fw = open('C:\\Users\\Administrator\\Desktop\基因序列\\write.txt','w+') #将多连核苷酸比例写到文件write中
for l in string:
    if l == '>':
        print('>'+s);
        fw.write('>'+s+'\n')
        #构造16种情况
        for i in range(0, 4):
            for j in range(0, 4):
                sub = arr[i] + arr[j]
                # print s
                save.append(s.count(sub))#保存每条序列出现16种情况的次数
        # print(save)
        s = '' #每次大循环后s为空，接着保存下一条基因序列
    else:
        s += l #将s扩展为完整一条序列，由于“>”在前面，还需要一次循环，将save中添加最后一条序列各种情况出现的次数
print('>'+s);
fw.write('>'+s+'\n') #fasta格式输入到文本
fw.close()
# 下面的循环是为了保存最后一条序列的情况
for i in range(0, 4):
    for j in range(0, 4):
        sub = arr[i] + arr[j]
        # print s
        save.append(s.count(sub))
print(save)

#程序分两部分，前面是保存save，后面是计算ratio和输出到txt
#两部分可以合并到一起

fno = open('C:\\Users\\Administrator\\Desktop\基因序列\\num.txt','w+') #
fratio = open('C:\\Users\\Administrator\\Desktop\基因序列\\fratio.txt','w+') #
count = 0
SUM = 0.0
temp = []
ratio = []
for i in save:
    count += 1
    temp.append(i)
    #print(i,'',end='')
    fno.write(str(i)+' ')
    SUM += i
    if count % 16 == 0:
        if SUM == 0:
            SUM = 1.0
        for j in temp:
            j = j/SUM
            ratio.append(j)
            fratio.write(str(j) + ' ') #执行循环，每16个换行，每行写入的是每条基因16种情况出现的比例
        #fratio.write(str(ratio) + ' ') #直接讲数组变成字符串
        print(ratio)
        print()
        SUM = 0.0
        temp = []
        ratio = []

        fno.write('\n')
        fratio.write('\n')
fno.close()
fratio.close()

end = time.clock()
print('消耗：',end-star,' s')
