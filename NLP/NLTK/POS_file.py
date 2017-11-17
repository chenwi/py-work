#-*- coding:utf-8 -*-
from nltk.corpus import brown
import nltk
from nltk import book

pos={}
pos['color']='N'
pos['ideas']='N'
pos['sleep']='V'
print pos.keys()
for w in pos:
    print w+':',pos[w]



alice=nltk.Text(word.lower() for word in nltk.corpus.brown.words())
alice=' '.join( alice[-100:])
print alice

fre=nltk.FreqDist(alice)
#表格输出,但是输出字符
# fre.tabulate()
print fre

last=nltk.defaultdict(list)
words=nltk.corpus.words.words('en')
# print words
for word in words:
    key=word[-2:]
    last[key].append(word)
#默认字典类型
print type(last)




# arg=nltk.Index((' '.join(sorted(w)),w) for w in words)
# print arg['aeilnrt']