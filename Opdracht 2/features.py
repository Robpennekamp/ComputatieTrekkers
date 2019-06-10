# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:21:40 2019

@author: Acer
"""
from nltk.corpus import conll2002 as conll


def simple_features_1(sentence, i, history):
    """Simplest chunker features: Just the POS tag of the word"""
    word, pos = sentence[i]
    return { "pos": pos,
            "pre1": word[0],
            "pre2": word[:2],
            "pre3": word[:3],
            "pre4": word[:4],
            "suf1": word[-1],
            "suf2": word[-2:],
            "suf3": word[-3:],
            "suf4": word[-4:],
            "cap": word[0] == word[0].upper(),
            "allcaps": word == word.upper(),
            "hascaps": word[1:].lower() != word[1:],
            "first": i ==0,
            "last": word == sentence[-1][0],
            "numeric": word.isdigit(),
            "hypen": "-" in word,
            "colon": ":" in word,
            }
def simple_features_2(sentence, i, history):
    """Simplest chunker features: Just the POS tag of the word"""
    word, pos = sentence[i]
    hasdigit = False
    for c in word:
        if c.isdigit():
            hasdigit = True
    
    #print(word)
    return { 
            "pos": pos,
            "pre1": word[0],
            "pre2": word[:2],
            "pre3": word[:3],
            "pre4": word[:4],
            "suf1": word[-1],
            "suf2": word[-2:],
            "suf3": word[-3:],
            "suf4": word[-4:],
            "cap": word[0] == word[0].upper(),
            "allcaps": word == word.upper(),
            "hascaps": word[1:].lower() != word[1:],
            "first": i ==0,
            "last": word == sentence[-1][0],
            "numeric": word.isdigit(),
            "hypen": "-" in word,
            "colon": ":" in word,
            "pred": '' if i==0 else sentence[i-1][0],
            "predpos": '' if i==0 else sentence[i-1][1],
            "preq": '' if word == sentence[-1][0] else sentence[i+1][0],
            "seqpos": '' if word == sentence[-1][0] else sentence[i+1][1],
            "seqcaps": '' if word == sentence[-1][0] else sentence[i+1][0].upper() == sentence[i+1],
            "date": hasdigit and "-" in word,
            "preqin":'' if i==0 else sentence[i-1][0] == 'in',
            
            }
