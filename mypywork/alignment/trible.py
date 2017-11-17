#-*- coding:utf-8 -*-

import re
import time
start = time.clock()
string = ''
f = open('C:\\Users\\Administrator\\Desktop\\complete.txt','r')
lines = f.readlines()

for l in lines:
    l = l.strip('\n')
    string += l
print string
LEN = len(string)+0.0
print LEN
print string.count('AA')
print string.count('AA')/LEN
print string.count('AG')
print string.count('AG')/LEN
print string.count('AC')
print string.count('AC')/LEN
print string.count('AT')
print string.count('AT')/LEN
print string.count('GA')
print string.count('GA')/LEN
print string.count('GG')
print string.count('GG')/LEN
print string.count('GC')
print string.count('GC')/LEN
print string.count('GT')
print string.count('GT')/LEN
print string.count('CA')
print string.count('CA')/LEN
print string.count('CG')
print string.count('CG')/LEN
print string.count('CC')
print string.count('CC')/LEN
print string.count('CT')
print string.count('CT')/LEN
print string.count('TA')
print string.count('TA')/LEN
print string.count('TG')
print string.count('TG')/LEN
print string.count('TC')
print string.count('TC')/LEN
print string.count('TT')
print string.count('TT')/LEN


end = time.clock()
print end-start,"second"

















