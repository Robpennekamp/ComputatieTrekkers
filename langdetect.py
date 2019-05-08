# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:10:27 2019

@author: robpe
"""

#Testtest
import re
import collections
def prepare(text):
    return re.sub('[\!\?\,\"\.\(\)\<\>]', ' ', text).split()


text = "Hallo dit is een test est"

def trigrams(seq):
    x = 0
    trigram_list = []
    while x < len(seq)-2:
        trigram_list.append(seq[x]+seq[x+1]+seq[x+2])
        x+=1
    return trigram_list

def trigram_table(text, limit = 0):
    new_text = prepare(text)
    new_list = []
    full_trigram = []
    full_freq= []
    new_dict = {}
    for word in new_text:
        new_word = ("<" + word + ">")
        new_list = trigrams(new_word)
        for i in range(0, len(new_list)):
            trigram = new_list[i]
            if trigram not in full_trigram:
                full_trigram.append(trigram)
                full_freq.append(1)
            else:
                index = full_trigram.index(trigram)
                full_freq[index] += 1
    full_list = []
    for j in range(len(full_trigram)):
        full_list.append([full_trigram[j], full_freq[j]])
    full_list.sort(key=lambda x: x[1], reverse=True)
    if(limit == 0):
        limit = len(full_list)
    for i in range(0, limit):
        new_dict[full_list[i][0]] = full_list[i][1]
    #print(new_dict)
#    sorted_dict = sorted(new_dict.items(), key = lambda k:k[1], reverse = True)
    return new_dict
