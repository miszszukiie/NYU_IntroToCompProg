# Helen Li
# May 6, 2015
# Assignment #10, Part #0

thesaurus = {
              "happy": "glad",
              "sad"  : "bleak"
            }

# make inputted phrase all lower case
phrase = str.lower(input("Enter a phrase: "))

# split by space between words
splitphrase = phrase.split(" ")

for word in splitphrase:
    newword = ""

    # only record alphabets
    for c in word:
        if c.isalpha():
            newword = newword + c

    # if word in thesaurus, print synonym
    # otherwise, print word
    if newword in thesaurus:
        print (str.upper(thesaurus[newword]), end=" ")
    else:
        print (newword, end=" ")
       
