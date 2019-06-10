# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:27:05 2019

@author: sepke
"""
from nltk.corpus import conll2002 as conll
from custom_chunker import ConsecutiveNPChunker

tiny_sample = 5000
# training = conll.chunked_sents("ned.train")  # Train with full dataset
training = conll.chunked_sents("ned.train") # SHORT DATASET: FOR DEMO/DEBUGGING ONLY!
testing = conll.chunked_sents("ned.testa")

simple_nl_NER = ConsecutiveNPChunker(features.simple_features_1, training)

output = open("nl-tagger.pickle", "wb")
pickle.dump(simple_nl_NER, output)
output.close()

simple_nl_NER2 = ConsecutiveNPChunker(features.simple_features_1, training, 'GIS')
print(simple_nl_NER2.evaluate(testing))



#output = open("nl-tagger.pickle", "wb")
#pickle.dump(simple_nl_NER, output)
#output.close()


#simple_nl_NER2 = ConsecutiveNPChunker(features.simple_features_1, training, 'GIS')
#print(simple_nl_NER2.evaluate(testing))

print(simple_nl_NER.evaluate(testing))
