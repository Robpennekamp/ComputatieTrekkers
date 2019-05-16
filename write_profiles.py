import os
import langdetect

def make_profiles(datafolder, profilefolder, size):
    files = os.listdir(datafolder) 
    for file in files:
        languagename = file.split("-")[0]
        encodering = file.split("-")[1]
        bestand = open('training/' + file,'r' , encoding=encodering)
        test = langdetect.trigram_table(bestand.read(), size)
        filename = languagename + '.' + str(size) + '.txt'
        newfile = open('trigram-models/' + filename, 'w', encoding="utf-8")
        langdetect.write_trigrams(test, 'trigram-models/' + filename)
        newfile.close()