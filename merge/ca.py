
import numpy as np

a={12:[['abc','acd','aa'],['awe','www']],10:['aaa','add']}
print(a[12][1][0])

en = np.loadtxt('C:\\Users\\Administrator\\Desktop\\temp\\entity.txt',delimiter='\t',dtype=np.str,usecols=(0,1,2,3,4,5))
re = np.loadtxt('C:\\Users\\Administrator\\Desktop\\temp\\relation.txt',delimiter='\t',dtype=np.str,usecols=(0,1,2,3,4,5))



# print(en)
# print(en[:,4])

dic={}
for pmid in en:
    dic.setdefault(pmid[0],[]).append(pmid[1:5])
# print(dic)
# print(en[0,1:5])
# print(dic['14967461'][1])
i=0
# while i<len(dic['14967461']):
#         print(dic['14967461'][i][0])
#         i=i+1


for i,chem_r in enumerate(re):
    # print(i,chem_r)
    key=chem_r[0]
    arg1 = chem_r[4][5:]
    arg2 = chem_r[5][5:]
    # print(arg1)
    # print(dic[key][0])
    # if dic[key][0]==arg1:
    #     print(dic[key])


    # print(dic[key][0])
    # if dic[key][0]==arg1:
    #     print(dic[key])

# print(len(dic['14967461']))

# while i < len(dic[key]):
#     if dic[key][i][0] != arg1:
#         print(dic[key][i])
#         i = i + 1
#     print(i)
#     print(len(dic[key]))

# abstract = open('C:\\Users\\Administrator\\Desktop\\temp\\full_abst.txt', 'r')
# for i in abstract.readlines():
#     print('1',i)
#     print(i[1277:1286])
#     print(len(i))
#     print('2',a)
pmid = np.loadtxt('C:\\Users\\Administrator\\Desktop\\temp\\pmid.txt',dtype=np.str)
# print(pmid[1]) #读取pmid
# for i,pm in enumerate(entity) :
#     # print(pm,i)
#     if pm[0]==pmid[1]:
#         start=pm[3]
#         end=pm[4]
        # print(start)


abstract = open('C:\\Users\\Administrator\\Desktop\\temp\\abstract.txt', 'r')
a=[1,2,3]
lin=abstract.readlines()
for i in a:
    for r in lin:
        # print(r)
        print()
# for r in lin:
#     print(r)

st='Emer. ging. role. of epidermal growth.'
st='10047461	Cyclin E-cdk2 activation is associated with cell cycle arrest and inhibition of DNA replication induced by the thymidylate synthase inhibitor Tomudex.	Tomudex (ZD1694) is'
print(len(st))
print(st.rfind('.	',2,300))
print(st[149:161])
print(st.rfind('.',0,179))
# print(st.find('metalloproteinase',300))