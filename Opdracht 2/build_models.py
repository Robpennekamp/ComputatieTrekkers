# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:27:05 2019

@author: Acer
"""
from nltk.corpus import conll2002 as conll
from custom_chunker import ConsecutiveNPChunker
import features 
import pickle

tiny_sample = 50
# training = conll.chunked_sents("ned.train")  # Train with full dataset
training = conll.chunked_sents("ned.train")[:tiny_sample] # SHORT DATASET: FOR DEMO/DEBUGGING ONLY! 
testing = conll.chunked_sents("ned.testa")
simple_nl_NER = ConsecutiveNPChunker(features.simple_features_1, training)
output = open("nl-tagger.pickle", "wb")
pickle.dump(simple_nl_NER, output)
output.close()

simple_nl_NER2 = ConsecutiveNPChunker(features.simple_features_1, training, 'GIS')
print(simple_nl_NER2.evaluate(testing))

print(simple_nl_NER.evaluate(testing))