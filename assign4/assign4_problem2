# Helen Li
# March 2, 2015
# Assignment #4: Problem #2: Pick Up Sticks

# prompts user for number of sticks to start with, then 2 players will take turns removing sticks from table, 
# player to remove last stick loses

# input amount of sticks to start with
while True:
   sticks = int(input("How many sticks are on the table? (Enter a number between 10 and 100): "))
   if sticks < 10 or sticks > 100:
      print ("Invalid number of sticks, try again.")
   else:
      break

while True:
   if sticks > 0:
      # prompt Player 1 to choose amount of sticks to remove (1-3)
      while True:
         print ("There are", sticks, "sticks on the table.")
         p1 = int(input("Player 1: How many sticks do you want to remove from the table? (1, 2 or 3): "))
         if p1 > 0 and p1 < 4:
            # make sure we don't go negative
            if p1 > sticks:
               print ("Invalid! We don't have that many sticks.")
            else:            
               sticks -= p1
               # player to remove last stick loses
               if sticks == 0:
                  print ("There are 0 sticks on the table.")
                  print ("Player 1 loses!")
                  break
               else:
                  break
         else:
            print ("Invalid entry, try again.")

      # prompt Player 2 to choose amount of sticks to remove (1-3)
      while True and sticks > 0:
         print ("There are", sticks, "sticks on the table.")
         p2 = int(input("Player 2: How many sticks do you want to remove from the table? (1, 2 or 3): "))
         if p2 > 0 and p2 < 4:
            # make sure we don't go negative
            if p2 > sticks:
               print ("Invalid! We don't have that many sticks.")
            else:            
               sticks -= p2
               # player to remove last stick loses
               if sticks == 0:
                  print ("There are 0 sticks on the table.")
                  print ("Player 2 loses!")
                  break
               else:
                  break
         else:
            print ("Invalid entry, try again.")
