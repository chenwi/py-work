# -*- coding:utf-8 -*-
import numpy as np
'''
--------------------------------------------------------
    #用来小样本测试
--------------------------------------------------------
'''

abstract = open('C:\\Users\\Administrator\\Desktop\\temp\\abstract.txt', 'r')
sen_f = np.loadtxt('C:\\Users\\Administrator\\Desktop\\temp\\2save_small.txt',delimiter='\t',dtype=np.str,usecols=(0,1,2,3,4,5,6,7,8,9))
# print(sen_f)
#将处理数据写到下面文件中
moti_train=open('C:\\Users\\Administrator\\Desktop\\temp\\2mt_train.txt','w+')

abst_lin=abstract.readlines()   #必须加这一句，否则readlines到达文件尾就不读了，会大致下面结果出错

for i,chem_all in enumerate(sen_f):
    pmid =chem_all[0]
    rel=chem_all[1]     #relations
    che_tag=chem_all[3]     #chemical
    gene_tag=chem_all[7]    #gene

    che_star=chem_all[4]    #position
    che_end=chem_all[5]
    gene_star=chem_all[8]   #position
    gene_end=chem_all[9]
    for abst in abst_lin :
        indx=abst.find('\t')+1  #加1的目的是为了字符串从摘要开始，而不是从\t开始
        pmid_a = abst[:indx]
        indx_pr=abst.find('.',int(gene_end))+1  #从第二个实体前向后找句号，这个加1是为了包含句号 .
        if (int(gene_end)>int(che_star)):
            indx_pl = abst.rfind('.', 0, int(gene_end)) + 2  # 从gene结尾的起始位置往左找第一个句号 .
        else:   indx_pl = abst.rfind('.', 0, int(che_end)) + 2  # 从chemical的结尾位置往左找第一个句号 .

        if indx_pl== 1:
            indx_pl=indx    #当左边没有句号就要从字串首开始读
#----------------------------------------------第一部分是打印---------------------------------------------------------------
        if int(pmid_a) == int(pmid):    #左边是<class 'str'>类型，右边是<class 'numpy.str_'>，这里都转换为int
            # print(pmid)
            #indx + int(che_end) 为命名实体开始位置
            if (int(gene_end)>int(che_star)):   #这里只用end和star比较就行（不是严格的）
                print(pmid + '\t' + abst[indx_pl:indx + int(che_star)] + '<' + che_tag + '>' +
                      abst[indx + int(che_star):indx + int(che_end)] + '</' + che_tag + '>' +
                      abst[indx + int(che_end):indx + int(gene_star)] + ' <' + gene_tag + '>' +
                      abst[indx + int(gene_star):indx + int(gene_end)] + '</' + gene_tag + '>' +
                      abst[indx + int(gene_end):indx_pr + 1])
                print(rel + '(' + che_tag + ',' + gene_tag + ')',indx_pl,che_star,abst.find('.',0,int(che_end)))
            elif (int(gene_end)<int(che_star)):
                print(pmid + '\t' + abst[indx_pl:indx + int(gene_star)] + '<' + gene_tag + '>' +
                      abst[indx + int(gene_star):indx + int(gene_end)] + '</' + gene_tag + '>' +
                      abst[indx + int(gene_end):indx + int(che_star)] + ' <' + che_tag + '>' +
                      abst[indx + int(che_star):indx + int(che_end)] + '</' + che_tag + '>' +
                      abst[indx + int(che_end):indx_pr + 1])
                print(rel + '(' + che_tag + ',' + gene_tag + ')',indx_pl,che_star,abst.find('.',0,int(che_end)))

#------------------------------------------------第二部分是写入文件--------------------------------------------------------------------------

            if (int(gene_end)>int(che_star)):   #这里只用end和star比较就行（不是严格的）
                moti_train.write(pmid + '\t' + abst[indx_pl:indx + int(che_star)] + '<' + che_tag + '>' +
                      abst[indx + int(che_star):indx + int(che_end)] + '</' + che_tag + '>' +
                      abst[indx + int(che_end):indx + int(gene_star)] + ' <' + gene_tag + '>' +
                      abst[indx + int(gene_star):indx + int(gene_end)] + '</' + gene_tag + '>' +
                      abst[indx + int(gene_end):indx_pr + 1]+'\n'+rel+'('+che_tag+','+gene_tag+')'+str(abst.find('.',0,int(che_end)))+'\n')

            elif (int(gene_end)<int(che_star)):
                moti_train.write(pmid + '\t' + abst[indx_pl:indx + int(gene_star)] + '<' + gene_tag + '>' +
                      abst[indx + int(gene_star):indx + int(gene_end)] + '</' + gene_tag + '>' +
                      abst[indx + int(gene_end):indx + int(che_star)] + ' <' + che_tag + '>' +
                      abst[indx + int(che_star):indx + int(che_end)] + '</' + che_tag + '>' +
                      abst[indx + int(che_end):indx_pr + 1]+'\n'+rel+'('+che_tag+','+gene_tag+')'+str(abst.find('.',0,int(che_end)))+'\n')

#-----------------------------------------------------------------------------------------------------------------
#下面是没考虑基因和化合物相对位置，有时基因在前
# print('<' + che_tag + '>' +
            #       abst[indx + int(che_star):indx + int(che_end)] + '</' + che_tag + '>' +
            #       abst[indx + int(che_end):indx + int(gene_star)]+' <' + gene_tag + '>' +
            #       abst[indx + int(gene_star):indx + int(gene_end)] + '</' + gene_tag + '>')
            # print(int(che_end),int(gene_star))
            # print(abst[1476+9:1483+9])
            # print(rel+'('+che_tag+','+gene_tag+')')
            # moti_train.write(pmid+'\t'+abst[indx_pl:indx + int(che_star)] + '<' + che_tag + '>' +
            #       abst[indx + int(che_star):indx + int(che_end)] + '</' + che_tag + '>' +
            #       abst[indx + int(che_end):indx + int(gene_star)]+' <' + gene_tag + '>' +
            #       abst[indx + int(gene_star):indx + int(gene_end)] + '</' + gene_tag + '>'+
            #       abst[indx + int(gene_end):indx_pr+1]+'\n'+rel+'('+che_tag+','+gene_tag+')'+'\n')






