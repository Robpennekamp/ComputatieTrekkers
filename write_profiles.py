import os
import langdetect


#lees de bestanden, maak nieuwe bestanden aan met trigrams en frequenties
def make_profiles(datafolder, profilefolder, size):
    files = os.listdir(datafolder) 
    for file in files:
        languagename = file.split("-")[0]
        encodering = file.split("-")[1]
        bestand = open('training/' + file,'r' , encoding=encodering)            #lees met juiste codering 
        test = langdetect.trigram_table(bestand.read(), size)                   #maak een trigramtabel van tekst
        filename = languagename + '.' + str(size) + '.txt'                      #geef een nieuwe bestandsnaam
        newfile = open('trigram-models/' + filename, 'w', encoding="utf-8")     #maak een nieuw bestand aan
        langdetect.write_trigrams(test, 'trigram-models/' + filename)           #maak een tekstbestand aan met de trigrams en frequentie
        newfile.close()