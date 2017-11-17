#-*- coding:utf-8 -*-

import re
import time

start = time.clock()

string=''
f = open('C:\\Users\\Administrator\\Desktop\\OMYK.txt','r')
lines = f.readlines()

for l in lines:
    l=l.strip('\n')
    string+=l
print (string)

AA = string.count('AA')
AG = string.count('AG')
AC = string.count('AC')
AT = string.count('AT')
GA = string.count('GA')
GG = string.count('GG')
GC = string.count('GC')
GT = string.count('GT')
CA = string.count('CA')
CG = string.count('CG')
CC = string.count('CC')
CT = string.count('CT')
TA = string.count('TA')
TG = string.count('TG')
TC = string.count('TC')
TT = string.count('TT')
SUM = AA+AG+AC+AT+GA+GG+GC+GT+CA+CG+CC+CT+TA+TG+TC+TT+0.0

print string.count('AA')/SUM
print string.count('AG')/SUM
print string.count('AC')/SUM
print string.count('AT')/SUM
print string.count('GA')/SUM
print string.count('GG')/SUM
print string.count('GC')/SUM
print string.count('GT')/SUM
print string.count('CA')/SUM
print string.count('CG')/SUM
print string.count('CC')/SUM
print string.count('CT')/SUM
print string.count('TA')/SUM
print string.count('TG')/SUM
print string.count('TC')/SUM
print string.count('TT')/SUM

end = time.clock()
print (end-start,"second")
