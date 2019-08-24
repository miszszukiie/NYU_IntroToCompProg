# Helen Li
# March 25, 2015
# Assignment #5: Problem #1: 99 Bottles of Beer on the Wall

# This code prompts the user to enter bottles of beer on the wall, then present the lyrics
# for the road trip song "99 Bottles of Beer"

# Ask user for a positive number bottles of beer on the wall
while True:
  bottles = int(input("How many bottles of beer on the wall? "))
  if bottles > 0:
    break
  else:
    print ("Sorry, that's not a valid number of bottles. Try again.")

print ()

# Present lyrics until no bottles of beer left on the wall
for bott in range (bottles, 0, -1):
    if bott > 2:
        print (bott, "bottles of beer on the wall,", bott, "bottles of beer.")
        print ("Take one down, pass it around,", bott-1, "bottles of beer on the wall.")
        print ()
    elif bott == 2: # Two bottles is plural, one bottle is singular
        print (bott, "bottles of beer on the wall,", bott, "bottles of beer.")
        print ("Take one down, pass it around,", bott-1, "bottle of beer on the wall.")
        print ()
    else: #Last verse to say no more, rather than 0
        print ("1 bottle of beer on the wall, 1 bottle of beer.")
        print ("Take it down, pass it around, no more bottles of beer on the wall!")
