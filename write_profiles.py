import re
import collections
import langdetect

def make_profiles(datafolder, profilefolder, size):
    for file in datafolder:
        languagename = file.split("-")[0]
        encoding = file.split("-")[1]
        if encoding == "UTF8":
            bestand = open(file,'r' , encoding="utf-8")
        elif encoding == "Latin1":
            bestand = open(file, 'r', encoding="Latin1")
        test = langdetect.trigram_table(bestand, size)
        filename = languagename + '.' + size
        newfile = open(filename, 'w', encoding="utf-8")
        langdetect.write_trigrams(test, filename)
        newfile.close()