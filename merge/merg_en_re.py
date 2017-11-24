# -*- coding:utf-8 -*-

import numpy as np

'''
    merge relation and entity
'''
#C:\Users\Administrator\Desktop\chemical\motify
# print(entity) 二维数据
entity = np.loadtxt(open('C:\\Users\\Administrator\\Desktop\\chemical\\motify\\chemprot_training_entities.tsv',encoding='latin-1'),
                    delimiter='\t',dtype=np.str,usecols=(0,1,2,3,4,5))

relation=np.loadtxt(open('C:\\Users\\Administrator\\Desktop\\chemical\\motify\\chemprot_training_relations.tsv',encoding='latin-1'),
                    dtype=np.str,usecols=(0,1,2,3,4,5))
# print(relation)
#将结果写入sen_f文件
sen_f=open('C:\\Users\\Administrator\\Desktop\\chemical\\motify\\sa.txt','w+')

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





