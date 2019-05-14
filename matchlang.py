# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:37:16 2019

@author: robpe
"""
import langdetect
import write_profiles
import os



class LangMatcher:
    
    def __init__(self, path):
        make_profiles(path, 'trigram-models', 200)
        languages =[]
        for file in mainfile:
            languages.append(file.split("-")[0])
            trigram_table()
        
    
    def score(self, text, n=1, ngrams=200):
        langdetect.trigram_table(text, ngrams)

