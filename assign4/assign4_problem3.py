# Helen Li
# March 2, 2015
# Assignment #4: Problem #3: Arrows

# This code prompts user to enter amount of columns that will create an arrow

# prompt user to input amount of columns
while True:
    columns = int(input("How many columns do you have? (Enter a positive number): "))
    if columns < 1:
        print ("Invalid entry, try again.")
    else:
        break

while True:
   # prompt user to choose if arrow will be left or right
   dir = str.lower(input("Is direction left or right? (Enter left or right): "))

   # if direction chosen is right
   if dir == "right":
      counter = 1
      while counter < columns:
         print (" " * (counter-1) + "*")
         counter += 1
      while columns > 0:
         print (" " * (columns-1) + "*")
         columns -= 1
      break

   # if direction chosen is left
   if dir == "left":
      counter = columns-1
      while counter > 0:
         print (" " * counter + "*")
         counter -= 1
      counter = 1
      while counter <= columns:
         print (" " * (counter-1) + "*")
         counter += 1
      break

   else:
      print ("Invalid entry! Try again.")
