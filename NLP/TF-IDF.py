from gensim import corpora,models,similarities
import jieba
from collections import defaultdict
import urllib.request

#d1=open("C:/Users/yyq/Desktop/毕业论文/文档1.txt").read()
#d2=open("C:/Users/yyq/Desktop/毕业论文/文档2.txt").read()

jieba.load_userdict("C:/Users/yyq/Desktop/毕业论文/词典.txt")
d1=urllib.request.urlopen("file:///C:/php/WWW/%E6%96%87%E6%A1%A31.html").read().decode("gbk","ignore")
d2=urllib.request.urlopen("file:///C:/php/WWW/%E6%96%87%E6%A1%A3%202.html").read().decode("gbk","ignore")

#print(data2)
data1=jieba.cut(d1)
data2=jieba.cut(d2)

data11=""
for item in data1:
    data11+=item+"  "
data21=""
for item in data2:
    data21+=item+"  "
documents=[data11,data21] #存储到数组
texts=[[word for word in document.split()]for document in documents]
#print(texts)
frequency=defaultdict(int)
for text in texts:
    for token in text:
        frequency[token]+=1
#print(frequency)
#texts=[[word for word in text if frequency[token]>2]for text in texts]

dictionary=corpora.Dictionary(texts)
#dictionary.save("C:/php/WWW/分词2.html")


d3=urllib.request.urlopen("file:///C:/php/WWW/%E6%96%87%E6%A1%A33.html").read().decode("gbk","ignore")
data3=jieba.cut(d3)
data31=""
for item in data3:
    data31+=item+"  "
new_doc=data31

new_vec=dictionary.doc2bow(new_doc.split())
#print(new_vec)
corpus=[dictionary.doc2bow(text) for text in texts]
#print(corpus)
corpora.MmCorpus.serialize("C:/Users/yyq/Desktop/毕业论文/corpus.txt",corpus)
tfidf=models.TfidfModel(corpus)
featureNum=len(dictionary.token2id.keys())
index=similarities.SparseMatrixSimilarity(tfidf[corpus],num_features=featureNum)
sim=index[tfidf[new_vec]]
print(sim)