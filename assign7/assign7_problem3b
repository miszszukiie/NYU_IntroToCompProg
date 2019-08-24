# Helen Li
# April 10, 2015
# Assignment # 7: Problem #3b

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

while True:
  action = input("(e)ncode, (d)ecode, or (q)uit: ")
  # to encode, add characters and shift string up
  if action == "e":
    number = int(input("Enter a number between 1 and 5: "))
    original = input("Enter a phrase to encode: ")
    h = add_number(original, number)
    i = shift_characters (h, number)
    print ("Your encoded word is:", i)
    print()
  # to decode, subtract characters and shift string down
  elif action == "d":
    number2 = int(input("Enter a number between 1 and 5: "))
    original2 = input("Enter a phrase to decode: ")
    j = remove_letters(original2, number2)
    k = shift_characters(j, -number2)
    print ("Your decoded word is:", k)
    print ()
  else:
    break
