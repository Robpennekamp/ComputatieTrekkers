import re
import collections

def make_profiles(datafolder, profilefolder, size):
    for file in datafolder:
        languagename = file.split("-")[0]
        encoding = file.split("-")[1]
        if encoding == "UTF8":
            bestandutf = open(file, encoding="utf-8")
        if encoding == "Latin1":
            bestandlatin = open(file, encoding="Latin1")
        table =[size]
        