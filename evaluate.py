import matchlang
import os
dict = {
    'da': 'Danish',
    'de': 'German',
    'el': 'Greek',
    'en': 'English',
    'es': 'Spanish',
    'fi': 'Finnish',
    'fr': 'French',
    'it': 'Italian',
    'nl': 'Dutch',
    'pt': 'Portuguese',
    'sv': 'Swedish',
}

#vergelijkt de talen en telt de hoeveelheid correcte en incorrecte matches
def eval(path):
    dir = os.listdir('test-clean/' + path)
    correctCount = 0
    errorCount = 0
    for file in dir:
        match = matchlang.findMath(path +'/'+ file)[0][0]
        correct = file.split(".")[1]
        if(dict[correct] == match):
            print(file + ': ' + match)
            correctCount += 1
        else:
            print(file+ ': ' + match  + '\t \t' + ' ERROR: ' + dict[correct])
            errorCount += 1
    print('Correct: ' + str(correctCount))
    print('Incorrect: ' + str(errorCount))
eval('europarl-90')
eval('europarl-30')
eval('europarl-10')
