# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:10:27 2019

@author: robpe
"""

#Testtest
import re
import numpy as np


def prepare(text):
    """
    Substitutes all punctuation in a text for a space. 
        
    text: the text to be altered.
    """
    return re.sub('[\!\?\,\"\.\(\)\<\>]', ' ', text).split() 


def trigrams(seq):
    """
    Takes a sequence and returns a list of its trigrams.
        
    seq: the sequence of which trigrams are created.
    """
    x = 0
    trigram_list = []
    while x < len(seq)-2:
        trigram_list.append(seq[x]+seq[x+1]+seq[x+2])
        x+=1
    return trigram_list


def trigram_table(text, limit = 0):
    """
    Prepares the words to extract the trigrams from each word, and uses a dictionary 
    to count how often each occurs, for each unique trigram. It determines, using 
    limit, how many ngrams to return, creates a new dictionary with the keys and 
    values and returns the dictionary.
        
    text: the filename of the file to be analyzed.
    limit: the number of frequent ngrams to be returned.
    """
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
                full_trigram.append(trigram)    #add each unique trigram to full_trigram
                full_freq.append(1)             #increase count
            else:
                index = full_trigram.index(trigram) 
                full_freq[index] += 1               #increase count
    full_list = []
    for j in range(len(full_trigram)):
        full_list.append([full_trigram[j], full_freq[j]])   #add trigrams and frequency to full_list
    full_list.sort(key=lambda x: x[1], reverse=True)        #sort from highest to lowest
    if(limit == 0):
        limit = len(full_list)
    elif(limit > len(full_list)):
        limit = len(full_list)
    for i in range(0, limit):
        new_dict[full_list[i][0]] = full_list[i][1]         #add trigrams and frequencies to dictionary
    #print(new_dict)
    #sorted_dict = sorted(new_dict.items(), key = lambda k:k[1], reverse = True)
    return new_dict


def write_trigrams(table, filename):
    """
    Takes a ngram table and writes the ngrams of the table to the file.
    
    table: the ngram table of the file.
    filename: the filename of the file to be analyzed.
    """
    tablefile = open(filename, "w", encoding='utf-8')
    for key, value in table.items():
        tablefile.write(str(value) + " " + str(key) + '\n')
    tablefile.close()


def read_trigrams(filename):
    """
    Reads the file's content and converts the values to a dictionary.
    
    filename: the filename of the file to be analyzed.
    """
    bestand = open(filename, "r", encoding='utf-8')
    woordenboek = {}
    for line in bestand:
        value = int(line.split()[0])
        key = line.split()[1]
        woordenboek[key] = value
    return woordenboek


def cosine_similarity(known, unknown):
    """
    Calculates the cosine similarity of the text and a known language. 
    
    known: a reference profile of a known language.
    unknown: the piece of text to be analyzed.
    """
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
