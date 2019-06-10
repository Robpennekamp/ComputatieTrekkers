# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:27:05 2019

@author: sepke
"""
from nltk.corpus import conll2002 as conll
from custom_chunker import ConsecutiveNPChunker
import pickle
import features

<<<<<<< HEAD
tiny_sample = 10000
=======
tiny_sample = 500
>>>>>>> 2796aefcf4f2531207fb793fcf7920b9963c7c9e
# training = conll.chunked_sents("ned.train")  # Train with full dataset
training = conll.chunked_sents("ned.train") # SHORT DATASET: FOR DEMO/DEBUGGING ONLY!
testing = conll.chunked_sents("ned.testa")
simple_nl_NER = ConsecutiveNPChunker(features.simple_features_2, training, 'NaiveBayes')

output = open("nl-tagger.pickle", "wb")
pickle.dump(simple_nl_NER, output)
output.close()


#simple_nl_NER2 = ConsecutiveNPChunker(features.simple_features_1, training, 'GIS')
#print(simple_nl_NER2.evaluate(testing))

print(simple_nl_NER.evaluate(testing))
