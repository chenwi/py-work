#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    :
# @File    : eg7.py
# @Software: PyCharm
"""
从文本提取信息
"""
import nltk
# 读取语料库的“训练”部分的100 个句子的例子
from nltk.corpus import conll2000
print(conll2000.chunked_sents('train.txt')[99])
# # 使用chunk_types 参数选择
print(conll2000.chunked_sents('train.txt', chunk_types=['NP'])[99])

# 访问一个已分块语料，可以评估分块器
cp = nltk.RegexpParser("")
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
print(cp.evaluate(test_sents))

# 尝试一个初级的正则表达式分块器，查找以名词短语标记的特征字母（如CD、DT 和JJ）开头的标记。
grammar = r"NP: {<[CDJNP].*>+}"
cp = nltk.RegexpParser(grammar)
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
print(cp.evaluate(test_sents))

# 使用unigram 标注器对名词短语分块。
class UnigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]
                  for sent in train_sents]
        self.tagger = nltk.UnigramTagger(train_data)
    def parse(self, sentence):
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)
                     in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)
# # 可以使用CoNLL2000 分块语料库训练它，并测试其性能
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
unigram_chunker = UnigramChunker(train_sents)
print(unigram_chunker.evaluate(test_sents))

postags = sorted(set(pos for sent in train_sents
                     for (word,pos) in sent.leaves()))
print(unigram_chunker.tagger.tag(postags))

# 使用连续分类器对名词短语分块
class ConsecutiveNPChunkTagger(nltk.TaggerI):
    def __init__(self, train_sents):
        train_set = []
        for tagged_sent in train_sents:
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                featureset = npchunk_features(untagged_sent, i, history)
                train_set.append( (featureset, tag) )
                history.append(tag)
        self.classifier = nltk.MaxentClassifier.train(train_set, algorithm='megam', trace=0)
    def tag(self, sentence):
        history = []
        for i, word in enumerate(sentence):
            featureset = npchunk_features(sentence, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history)

class ConsecutiveNPChunker(nltk.ChunkParserI):
        def __init__(self, train_sents):
            tagged_sents = [[((w, t), c) for (w, t, c) in
                             nltk.chunk.tree2conlltags(sent)]
                            for sent in train_sents]
            self.tagger = ConsecutiveNPChunkTagger(tagged_sents)

        def parse(self, sentence):
            tagged_sents = self.tagger.tag(sentence)
            conlltags = [(w, t, c) for ((w, t), c) in tagged_sents]
            return nltk.chunk.conlltags2tree(conlltags)

# # 定义一个简单的特征提取器，它只是提供了当前标识符的词性标记
def npchunk_features(sentence, i, history):
    word, pos = sentence[i]
    return {"pos": pos}
train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
chunker = ConsecutiveNPChunker(train_sents)
print(chunker.evaluate(test_sents))


# 一个分块器，处理NP，PP，VP 和S
grammar = r"""
NP: {<DT|JJ|NN.*>+} # Chunk sequences of DT, JJ, NN
PP: {<IN><NP>} # Chunk prepositions followed by NP
VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
CLAUSE: {<NP><VP>} # Chunk NP, VP
"""
cp = nltk.RegexpParser(grammar)
sentence = [("Mary", "NN"), ("saw", "VBD"), ("the", "DT"), ("cat", "NN"),
("sit", "VB"), ("on", "IN"), ("the", "DT"), ("mat", "NN")]
print(cp.parse(sentence))
sentence = [("John", "NNP"), ("thinks", "VBZ"), ("Mary", "NN"),
            ("saw", "VBD"), ("the", "DT"), ("cat", "NN"), ("sit", "VB"),
            ("on", "IN"), ("the", "DT"), ("mat", "NN")]
print(cp.parse(sentence))

cp = nltk.RegexpParser(grammar, loop=2)
print(cp.parse(sentence))




# 在NLTK 中，创建了一棵树，通过给一个节点添加标签和一个孩子链表：
# tree1 = nltk.Tree('NP', ['Alice'])
# print(tree1)
# tree2 = nltk.Tree('NP', ['the', 'rabbit'])
# print(tree2)
# tree3 = nltk.Tree('VP', ['chased', tree2])
# tree4 = nltk.Tree('S', [tree1, tree3])
# print(tree4)
# print(tree4[1])
# print(tree4.leaves())
# print(tree4[1].node)
# print(tree4[1][1][1])

# 递归函数遍历树
# def traverse(t):
#     try:
#         t.node
#     except AttributeError:
#         print(t,)
#     else:
#         # Now we know that t.node is defined
#         print ('(', t.node,)
#         for child in t:
#             traverse(child)
#         print (')',)
#
# t = nltk.Tree('(S (NP Alice) (VP chased (NP the rabbit)))')
# print(traverse(t))


sent = nltk.corpus.treebank.tagged_sents()[22]
print(nltk.ne_chunk(sent, binary=True))
print(nltk.ne_chunk(sent))