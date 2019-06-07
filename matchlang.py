# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:37:16 2019

@author: robpe
"""
import langdetect
import os
import sys



class LangMatcher:

    def __init__(self, path):
        """
        Creates a dictionary of dictionaries of languages with their respecitve trigram tables.
        
        Path: The path to the directory with all the trainingfiles for all languages.
        """
        files = os.listdir(path)
        models = {}
        for file in files:
            lang = file.split('.')[0]
            model = langdetect.read_trigrams(path + lang + '.200.txt')
            models[lang] = model
        self.models = models


    def score(self, text, n=1, ngrams=200):
        """
        Creates a trigramtable for the text to be analyzed, takes the top ngrams-ngrams and 
        returns a array of arrays of languages with the n-highest similarity-scores.
        
        text: The text to be analyzed
        n: Return the n-most similar languages
        ngrams: decides the ngram-amount of most frequent trigrams per language to be reported.
        """
        trigram = langdetect.trigram_table(text, ngrams)
        scoretable = []
        for key, value in self.models.items():
            lang = key
            model = value
            scoretable.append([lang, langdetect.cosine_similarity(model, trigram)])
        scoretable.sort(key=lambda x: x[1], reverse=True)
        return scoretable[0: n]


    def recognize(self, filename, encoding="utf-8", ngrams=200):
        """
        Uses the score-function to return the most similar language.
        
        filename: the filename of the file to be analyzed.
        encoding: the encoding with which the file should be read.
        ngrams: decides the ngram-amount of most frequent trigrams per language to be reported.
        """
        file = open(filename, 'r', encoding)
        file.close()
        return self.score(file, 1, 200)


args = sys.argv                                 
matcher = LangMatcher('trigram-models/')            #Initializes a Langmatcher object

#geeft de beste taal en cosine similarity score
def findMatch(filename, encoding):
    """
    Opens the file in a Langmatcher object to return the score of the most similar language, 
    using the Langmatcher class.

    filename: the filename of the file to be analyzed.
    encoding: the encoding with which the file should be read.
    """
    file = open('test-clean/' + filename, 'r', encoding=encoding)
    best = matcher.score(file.read(), 1,200)
    file.close()
    return best




#Prints the results of the findMatch function per file, which consist of the filename, 
#the most similar language, and its similarity score.
for arg in args:
    encoding = 'utf-8'
    if('-e' in arg):
        i = arg.split(' -e ')
        arg = i[0]
        encoding = i[1]
    if('.py' not in arg and '*' not in arg):
        best = findMatch(arg, encoding)
        print(arg + '\t' + best[0][0] + '\t' + str(best[0][1]) )
    elif('*' in arg):
        spec = arg.split('*')[1]
        files = os.listdir('test-clean/'+ arg.split('*')[0])
        for file in files:
            if(spec in file):
                filename = arg.split('*')[0] + file
                best = findMatch(filename, encoding)
                print(filename + '\t' + best[0][0] + '\t' + str(best[0][1]) )
