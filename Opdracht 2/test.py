# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 12:42:03 2019

@author: robpe
"""

import nltk
import pickle

input = open("nl-tagger.pickle", "rb")
pickler = pickle.load(input)
input.close()





tiny_sample = 100
# training = conll.chunked_sents("ned.train")  # Train with full dataset
training = conll.chunked_sents("ned.train")[50:tiny_sample] # SHORT DATASET: FOR DEMO/DEBUGGING ONLY! 
testing = conll.chunked_sents("ned.testa")




simple_nl_NER = ConsecutiveNPChunker(features.simple_features_1, training)
output = open("nl-tagger.pickle", "wb")
pickle.dump(simple_nl_NER, output)
output.close()

simple_nl_NER2 = ConsecutiveNPChunker(features.simple_features_1, training, 'GIS')
print(simple_nl_NER2.evaluate(testing))

print(simple_nl_NER.evaluate(testing))