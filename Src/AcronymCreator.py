#Summmary: Create an acronym of any entered phrase
import re
firstL = []
noiseWords = ["and", "to"]
#input
title = raw_input("Enter a title here: ")
#remove unwanted words
for word in noiseWords:
    if (word in title):
        title = title.replace(word, "")
#remove whitespace
"".join(title.split())
#find first letters and add to a list
for i in range(len(title)):
    if (i == 0 or (title[i - 1] != None and title[i - 1] == " ")):
        firstL.append(title[i])
#get the letters in a string
final = ""
for i in firstL:
    final += (firstL[firstL.index(i)].upper())
#read to console
print(final)
