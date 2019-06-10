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
<<<<<<< HEAD
tiny_sample = 10000
=======
tiny_sample = 500
>>>>>>> 2796aefcf4f2531207fb793fcf7920b9963c7c9e
=======
tiny_sample = 5000
>>>>>>> 8fd0734e59d562df4a888227d0e58a1e4353d57d
# training = conll.chunked_sents("ned.train")  # Train with full dataset
training = conll.chunked_sents("ned.train") # SHORT DATASET: FOR DEMO/DEBUGGING ONLY!
testing = conll.chunked_sents("ned.testa")
<<<<<<< HEAD
simple_nl_NER = ConsecutiveNPChunker(features.simple_features_2, training, 'NaiveBayes')
=======
simple_nl_NER = ConsecutiveNPChunker(features.simple_features_2, training, 'IIS')
>>>>>>> 8fd0734e59d562df4a888227d0e58a1e4353d57d

output = open("nl-tagger.pickle", "wb")
pickle.dump(simple_nl_NER, output)
output.close()


#simple_nl_NER2 = ConsecutiveNPChunker(features.simple_features_1, training, 'GIS')
#print(simple_nl_NER2.evaluate(testing))

print(simple_nl_NER.evaluate(testing))
