# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:31:09 2019

@author: Acer
"""

# FILE: model_test.py

import pickle
ner = pickle.load(open("best.pickle", "rb"))

from nltk.corpus import conll2002 as conll

# Usage 1: parse a list of sentences (with POS tags)
tagzinnen = conll.tagged_sents("ned.train")[1000:1050]
result = ner.parse_sents(tagzinnen)

# Usage 2: self-evaluate (on chunked sentences)
chunkzinnen = conll.chunked_sents("ned.testa")[1000:1500]
print(ner.evaluate(chunkzinnen))