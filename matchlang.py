# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:37:16 2019

@author: robpe
"""
import langdetect
import os
import sys



class LangMatcher:

    #initializer, maakt een dictionary van de trigram profielen
    def __init__(self, path):
        files = os.listdir(path)
        models = {}
        for file in files:
            lang = file.split('.')[0]
            model = langdetect.read_trigrams(path + lang + '.200.txt')
            models[lang] = model
        self.models = models

    #maakt een trigramtabel van de tekst en vergelijkt deze met de talen in models dictionary
    #returnt scores voor cosine similarity
    def score(self, text, n=1, ngrams=200):
        trigram = langdetect.trigram_table(text, ngrams)
        scoretable = []
        for key, value in self.models.items():
            lang = key
            model = value
            scoretable.append([lang, langdetect.cosine_similarity(model, trigram)])
        scoretable.sort(key=lambda x: x[1], reverse=True)
        return scoretable[0: n]


    #returnt de hoogste cosine similarity score en taal voor een file
    def recognize(self, filename, encoding="utf-8", ngrams=200):
        file = open(filename, 'r', encoding)
        file.close()
        return self.score(file, 1, 200)

#geeft de beste taal en cosine similarity score
def findMath(filename):
    file = open('test-clean/' + filename, 'r', encoding='utf-8')
    best = matcher.score(file.read(), 1,200)
    file.close()
    #print(filename + '\t' + best[0][0] + '\t' + str(best[0][1]) )
    return best
args = sys.argv
matcher = LangMatcher('trigram-models/')

#print het resultaat van de bovenstaande functies
for arg in args:
    if('.py' not in arg and '*' not in arg):
        best = findMath(arg)
        print(arg + '\t' + best[0][0] + '\t' + str(best[0][1]) )

    elif('*' in arg):
        spec = arg.split('*')[1]
        files = os.listdir('test-clean/'+ arg.split('*')[0])
        for file in files:
            if(spec in file):
                filename = arg.split('*')[0] + file
                best = findMath(filename)
                print(filename + '\t' + best[0][0] + '\t' + str(best[0][1]) )
