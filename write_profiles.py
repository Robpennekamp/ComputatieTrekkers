import os
import langdetect


#lees de bestanden, maak nieuwe bestanden aan met trigrams en frequenties
def make_profiles(datafolder, profilefolder, size):
    """
    Reads each file in the datafolder using the appropriate encoding, and generates a table
    of the given size. Then it writes the created ngram table files in the profilefolder under
    the new defined name.
    
    datafolder: the folder in which the language files are stored.
    profilefolder: the folder in which the table files are written.
    size: decides the ngram-amount of most frequent trigrams per language to be reported.
    """
    files = os.listdir(datafolder) 
    for file in files:
        languagename = file.split("-")[0]
        encodering = file.split("-")[1]
        bestand = open('training/' + file,'r' , encoding=encodering)            #Reads with the correct encoding.
        test = langdetect.trigram_table(bestand.read(), size)                   #Creates a ngram table of the content of the file.
        filename = languagename + '.' + str(size) + '.txt'                      #Creates a new filename.
        newfile = open('trigram-models/' + filename, 'w', encoding="utf-8")    
        langdetect.write_trigrams(test, 'trigram-models/' + filename)           #Creates a new file with the ngrams and their frequency.
        newfile.close()