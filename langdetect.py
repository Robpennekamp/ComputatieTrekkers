# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:10:27 2019

@author: robpe
"""

#Testtest
import re
import collections
import numpy as np

# vervang interpunctietekens door spatie
def prepare(text):
    return re.sub('[\!\?\,\"\.\(\)\<\>]', ' ', text).split() 

#creer van elk woord trigrams en return een lijst van deze trigrams
def trigrams(seq):
    x = 0
    trigram_list = []
    while x < len(seq)-2:
        trigram_list.append(seq[x]+seq[x+1]+seq[x+2])
        x+=1
    return trigram_list

#creer een tabel met de trigrams en hun frequenties, return een dictionary met deze gegevens
def trigram_table(text, limit = 0):
    new_text = prepare(text)
    new_list = []
    full_trigram = []
    full_freq= []
    new_dict = {}
    for word in new_text:                   
        new_word = ("<" + word + ">")           #zet elk woord tussen < en >
        new_list = trigrams(new_word)           
        for i in range(0, len(new_list)):
            trigram = new_list[i]               
            if trigram not in full_trigram:     
                full_trigram.append(trigram)    #voeg elke unieke trigram toe aan de lijst full_trigram
                full_freq.append(1)             #verhoog de telling bij elke trigram
            else:
                index = full_trigram.index(trigram) 
                full_freq[index] += 1               #verhoog de telling bij elke trigram
    full_list = []
    for j in range(len(full_trigram)):
        full_list.append([full_trigram[j], full_freq[j]])   #voeg de trigrams en hun frequentie toe aan full_list
    full_list.sort(key=lambda x: x[1], reverse=True)        #sorteer van groot naar klein
    if(limit == 0):
        limit = len(full_list)
    elif(limit > len(full_list)):
        limit = len(full_list)
    for i in range(0, limit):
        new_dict[full_list[i][0]] = full_list[i][1]         #voeg trigrams en frequenties toe aan dictionary
    #print(new_dict)
    #sorted_dict = sorted(new_dict.items(), key = lambda k:k[1], reverse = True)
    return new_dict

#schrijf de trigramtabel om in een tekstbestand
def write_trigrams(table, filename):
    tablefile = open(filename, "w", encoding='utf-8')
    for key, value in table.items():
        tablefile.write(str(value) + " " + str(key) + '\n')
    tablefile.close()

#schrijf het tekstbestand met trigrams om in een tabel
def read_trigrams(filename):
    bestand = open(filename, "r", encoding='utf-8')
    woordenboek = {}
    for line in bestand:
        value = int(line.split()[0])
        key = line.split()[1]
        woordenboek[key] = value
    return woordenboek

#cosine similarity berekening
def cosine_similarity(known, unknown):
    #known is the language we know
    #unknown is the piece of text we need to analyze.
    #both are dictionaries
    sumab = 0
    magsuma = 0
    magsumb = 0
    for key, value in unknown.items():
        try:
            vknown = known[key]
        except:
            vknown = 0
        ab = value * vknown
        sumab += ab
        magsuma += value ** 2
    for key, value in known.items():
        magsumb += value ** 2
    maga = np.sqrt(magsuma)
    magb = np.sqrt(magsumb)
    cossim = sumab / (maga*magb)
    return cossim
