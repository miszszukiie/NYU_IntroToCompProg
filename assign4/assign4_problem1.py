# Helen Li
# March 2, 2015
# Assignment #4: Problem #1: Roll the Dice

# This code prompts user to enter number of sides on dice, and will roll until roll snake eyes

# random roll
import random

# accumulate values for each roll
die_one = 0
die_two = 0

total_die_one = 0
total_die_two = 0

# accumulate times dices are rolled
roll_one = 0
roll_two = 0

# accumulate doubles rolled
doubles = 0

counter = 1

# prompt user for number of sides on dice (>3)
while True:
   number_of_sides = int(input("Enter the number of sides on your dice: "))
   if number_of_sides <= 3:
      print ("Sorry, that is not a valid size value. Please choose a positive number greater than 3.")
   else:
      break

# keep rolling dice until snake eyes
while True:
   roll_one += 1
   roll_two += 1
   die_one = random.randint(1, number_of_sides)
   die_two = random.randint(1, number_of_sides)
   total_die_one += die_one
   total_die_two += die_two
   if die_one == die_two:
      doubles += 1
   if die_one == 1 and die_two == 1:
      print (counter, ". Die one: 1 and Die two: 1", ".", sep="")
      break
   else:
      # report results of each roll
      print (counter, ". Die one: ", die_one, " and Die two: ", die_two, ".", sep="")
      counter += 1

print ()

# report times rolled to get snake eyes
print ("Congrats! You got snake eyes! It took", roll_one, "tries!")

# report times doubles rolled
print ("Along the way, you rolled doubles", doubles, "times.")

average_die_one = total_die_one/roll_one
new_average_die_one = format(average_die_one, ".2f")
average_die_two = total_die_two/roll_two
new_average_die_two = format(average_die_two, ".2f")

# report average roll for each die
print ()
print ("Average roll of Die one was: ", new_average_die_one, ".", sep="")
print ("Average roll of Die two was: ", new_average_die_two, ".", sep="")
