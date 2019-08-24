# Helen Li
# April 10, 2015
# Assignment #7: Problem #3a

import random

# add a number of random letters to a string
def add_number (word, num):
  newword=""
  for x in word:
    newword += x
    for y in range (1, num+1):
      z = random.randint(33,126)
      a = chr(z)
      newword += a
  return (x+newword)[1:]

# remove letters from a string
def remove_letters (word, num):
  b = word[0::num+1]
  return b

# shift characters of string up or down ASCII
def shift_characters (word, num):
  newword=""
  for c in word:
    d = ord(c)
    g = int(d)
    e = g+num
    f = chr(e)
    newword += f
  return newword
