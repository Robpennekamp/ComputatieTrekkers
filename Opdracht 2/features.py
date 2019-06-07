# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:21:40 2019

@author: Acer
"""
from nltk.corpus import conll2002 as conll


def simple_features_1(sentence, i, history):
    """Simplest chunker features: Just the POS tag of the word"""
    word, pos = sentence[i]
    return { "pos": pos }
def word(sentence, i, history):
    return {"word": sentence[i]}
def first(sentence,i,history):
    return {"first": i == 0}
def last(sentence,i,history):
    return {"last": i == 0}
def capital(sentence, i, history):
    return {"capital": sentence[i][0] == sentence[i][0].upper()}
def lower(sentence, i, history):
    return {"lower": sentence[i] == sentence[i].lower()}
def allcaps(sentence, i, history):
    return{"all-caps": sentence[i] == sentence[i].upper()}
def pre1(sentence, i ,history):
    return{"pre1": sentence[i][0]}
def pre2(sentence, i ,history):
    return{"pre2": sentence[i][:2]}
def pre3(sentence, i ,history):
    return{"pre3": sentence[i][:3]}
def pre4(sentence, i ,history):
    return{"pre4": sentence[i][:4]}
def suf1(sentence, i, history):
    return{"suf1": sentence[i][-1]}
def suf2(sentence, i, history):
    return{"suf2": sentence[i][-2:]}
def suf3(sentence, i, history):
    return{"suf3": sentence[i][-3:]}
def suf4(sentence, i, history):
    return{"suf4": sentence[i][-4:]}
def pred(sentence, i, history):
    return {"pred": '' if index == 0 else: sentence[i -1 ]}
def next(sentence, i, history):
    return {"next": '' if index == len(sentence) - 1 else: sentence[i+1]}
def hypen(sentence, i , history):
    return{"hypen": '-' in sentence[i]}
def numeric(sentence, i, history):
    return{"numeric": sentence[i].isdigit()}
def hascapital(sentence, i, history):
    return{"hascapital" : sentence[i][1:].lower() != sentence[i][1:].lower()}
