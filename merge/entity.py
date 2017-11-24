# -*- coding:utf-8 -*-

import numpy as np
'''
--------------------------------------------------------
    #用来小样本测试
--------------------------------------------------------
'''
# abstract = open('C:\\Users\\Administrator\\Desktop\\temp\\abstract.txt', 'r')
# entity = open('C:\\Users\\Administrator\\Desktop\\temp\\entity.txt', 'r')
# relation = open('C:\\Users\\Administrator\\Desktop\\temp\\relation.txt', 'r')

'''
    merge relation and entity
'''
# print(entity) 二维数据
entity = np.loadtxt('C:\\Users\\Administrator\\Desktop\\temp\\entity.txt',delimiter='\t',dtype=np.str,usecols=(0,1,2,3,4,5))

relation=np.loadtxt('C:\\Users\\Administrator\\Desktop\\temp\\relation.txt',dtype=np.str,usecols=(0,1,2,3,4,5))
# print(relation)
#将结果写入sen_f文件
sen_f=open('C:\\Users\\Administrator\\Desktop\\temp\\2save_small.txt','w+')

for i,chem_r in enumerate(relation):
    # print(pm[4][5:])# 第4列字符串从index 5 开始，arg1：T1 变成 T1
    arg1 = chem_r[4][5:]
    arg2 = chem_r[5][5:]
    # print(chem_r,arg1,arg2)
    for j,chem_e in enumerate(entity):  #先处理arg T1再处理arg T2，循环匹配
        if chem_e[0]==chem_r[0] and chem_e[1]==arg1 :   #(chem_e[1]==chem_r[4][5:] or chem_e[1]==chem_r[5][5:]):
            # print(chem_r[3],chem_e[1],chem_e[2],chem_e[5])
            for k,chem_e2 in enumerate(entity):
                if chem_e2[0]==chem_r[0] and chem_e2[1]==arg2:
                    print(chem_r[0], chem_r[3], chem_e[1], chem_e[2],chem_e[3],chem_e[4],
                          chem_e2[1],chem_e2[2],chem_e2[3],chem_e2[4])
                    sen_f.write(chem_r[0]+'\t'+chem_r[3]+'\t'+chem_e[1]+'\t'+chem_e[2]+'\t'+chem_e[3]+'\t'+chem_e[4]+'\t'
                                +chem_e2[1]+'\t'+chem_e2[2]+'\t'+chem_e2[3]+'\t'+chem_e2[4]+'\n')
sen_f.close()








# -----------------------------------------------
# path = 'C:\\Users\\Administrator\\Desktop\\temp\\abstract.txt'
#
#
# def chem(path):
#     abstract = open(path, 'r')
#     abst = abstract.readline()
#     str = ''
#     for i in abst:
#         str += i
#         if i == '\t':
#             abst = abstract.readline()
#     return str
#
# lenth = len(chem(path)) + 1
# lenth -= 1  # from index 0
# print(lenth)
# print(chem(path))
# -------------------------------------------------



# print(abst[1277 + 9:1286 + 9])

# print(chem())
# ent = entity.readline()
# str1 = ''
# for i in ent:
#     print(i)
# print(len(ent))
# print(ent[1])

# e = open('C:\\Users\\Administrator\\Desktop\\temp\\entity.txt', 'r')
#
#
# en = np.loadtxt('C:\\Users\\Administrator\\Desktop\\temp\\entity.txt',dtype=np.str,usecols=(0,1,2,3,4,5))
# # a=np.loadtxt('C:\\Users\\Administrator\\Desktop\\temp\\abstract.txt',dtype=np.str,usecols=(-1))
# print(a)
# print(en[:,2])



