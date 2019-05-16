# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:37:16 2019

@author: robpe
"""
import langdetect
import write_profiles
import os
import sys



class LangMatcher:

    def __init__(self, path):
        files = os.listdir(path)
        models = {}
        for file in files:
            lang = file.split('.')[0]
            model = langdetect.read_trigrams(path + lang + '.200.txt')
            models[lang] = model
        self.models = models

    def score(self, text, n=1, ngrams=200):
        trigram = langdetect.trigram_table(text, ngrams)
        scoretable = []
        for key, value in self.models.items():
            lang = key
            model = value
            scoretable.append([lang, langdetect.cosine_similarity(model, trigram)])
        scoretable.sort(key=lambda x: x[1], reverse=True)
        bestlangs = []
        for i in range(n):
            bestlangs.append([scoretable[i][0], scoretable[i][1]])
        return bestlangs

    def recognize(self, filename, encoding="utf-8", ngrams=200):
        file = open(filename, 'r', encoding)
        file.close()
        return self.score(file, 1, 200)

def findMath(filename):
    file = open('test-clean/' + filename, 'r', encoding='utf-8')
    best = matcher.score(file.read(), 1,200)
    file.close()
    print(filename + '\t' + best[0][0] + '\t' + str(best[0][1]) )
args = sys.argv
matcher = LangMatcher('trigram-models/')

for arg in args:
    if('.py' not in arg and '*' not in arg):
        findMath(arg)
    elif('*' in arg):
        spec = arg.split('*')[1]
        files = os.listdir('test-clean/'+ arg.split('*')[0])
        for file in files:
            if(spec in file):
                findMath(arg.split('*')[0] + file)
