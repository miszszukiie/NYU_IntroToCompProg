# Helen Li
# April 10, 2015
# Assignment #7: Problem #2a

name = input("Name: ")

# convert all characters to lowercase
name1 = str.lower(name)

newname=""
reduction = 0

# alpha characters only
for character in name1:
    if character.isalpha() == True:
        newname += character
        a = ord(character)
        b = int(a)
        reduction += (b-96)
    else:
        newname += ""
    
print ("Your 'cleaned up' name is:", newname)
print ("Reduction:", reduction)
