#-*- coding:utf-8 -*-

import re
import time
star = time.clock()
f = open('C:\\Users\\Administrator\\Desktop\基因序列\\RIB40.txt')
line = f.readlines()
string = ''
for l in line:
    l = l.strip('\n')
    string += l
sub = ''
arr = ['A','G','C','T']
save = [] #记录每种多连核苷酸出现的次数
m = 0 #记录基因序列数量
fw = open('C:\\Users\\Administrator\\Desktop\基因序列\\write.txt','w+') #将多连核苷酸比例写到文件write中
for l in string:
    sub += l
    if l == '>':
        s = ''
        for i in range(0, 4):
            for j in range(0, 4):
                for k in range(0, 4):
                    s = arr[i] + arr[j] + arr[k]
                    # print s
                    save.append(sub.count(s))

        SUM = sum(save) + 0.0
        if SUM == 0.0:
            SUM = 1.0
        print(SUM)
        ratio = [] #记录多连核苷酸出现的比例
        for i in save:
            i = i / SUM
            ratio.append(i)
            t = str(i)
            fw.write(t)
        print(ratio)
        m += 1
        print('第',m,'条\n-------------------------------------------')
        fw.write('\n--------------第'+str(m)+'条-------------------\n')

fw.close()

end = time.clock()
print('耗时：',end-star)