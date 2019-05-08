# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:10:27 2019

@author: robpe
"""

#Testtest
import re
def prepare(text):
    return re.sub('[\!\?\,\"\.\(\)\<\>]', ' ', text).split()


text = "Hallo dit is een test"

def trigrams(seq):
    x = 0
    trigram_list = []
    while x < len(seq)-2:
        trigram_list.append(seq[x]+seq[x+1]+seq[x+2])
        x+=1
    return trigram_list

print(trigrams(seq))

def trigrams_table(text, limit = 0):
    new_text = prepare(text)
    for word in new_text:
        word = "<" + word + ">"



woord = "Hallo"
woord = "<" + woord + ">"
print(woord)
