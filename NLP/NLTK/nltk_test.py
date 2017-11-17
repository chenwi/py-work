#-*- coding:utf-8 -*-

import nltk
# nltk.download()
# from nltk.book import *
#text1
# text1.concordance("beautiful")
# text1.similar('private')

from random import randint

def segment(text,segs):
    words=[]
    last=0
    for i in range(len(segs)):
        if segs[i]=='1':
            words.append(text[last:i+1])
            last=i+1
    words.append(text[last:])
    return words

def evaluate(text,segs):
    words=segment(text,segs)
    text_size=len(words)
    lexicon_size=len(' '.join(list(set(words))))
    return text_size+lexicon_size


def flip(segs,pos):
    return segs[:pos]+str(1-int(segs[pos]))+segs[pos+1:]

def flip_n(segs,n):
    for i in range(n):
        sges=flip(segs,randint(0,len(segs)-1))
    return segs

def anneal(text,segs,iterations,cooling_rate):
    temperature = float(len(segs))
    while temperature>0.5 :
        best_segs,best=segs, evaluate(text,segs)
        for i in range(iterations):
            guess = flip_n(segs,int(round(temperature)))
            score = evaluate(text,guess)
            if score<best:
                best,s=best_segs=score,guess
        score,segs=best,best_segs
        temperature=temperature/cooling_rate
        print evaluate(text,segs), segment(text,segs)
    print
    return segs

if __name__ == '__main__':
    text="doyouseethekittyseetthedoggydoyoulikethekitty"
    seg='0000100100000001000000001000000010000001000000'
    anneal(text,seg,5000,2.0)




