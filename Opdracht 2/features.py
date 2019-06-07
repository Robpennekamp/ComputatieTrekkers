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


    