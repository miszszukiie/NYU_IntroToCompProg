# Helen Li
# May 6, 2015
# Assignment #10, Part #1

import random

thesaurus = {"happy":["glad", "blissful", "ecstatic", "at ease"], "sad":["bleak", "blue", "depressed"]}

# convert phrase to all lower case
phrase = str.lower(input("Enter a phrase: "))

# split by space
splitphrase = phrase.split(" ")


for word in splitphrase:
    newword = ""

    # only record alphabets
    for c in word:
        if c.isalpha():
            newword = newword + c

    # if word in thesaurus, randomly choose a synonym
    # else, just print word
    if newword in thesaurus:
        a = random.randint(0, len(thesaurus[newword])-1)
        print (str.upper(thesaurus[newword][a]), end=" ")
    else:
        print (newword, end=" ")
