# Helen Li
# April 10, 2015
# Assignment #7: Problem #1a

while True:
  user = input("Enter a username: ")
  # username 8 - 15 characters
  if len(user) < 8:
    print ("Username too short. Username must be between 8 and 15 characters. Try again.")
    print()
  elif len(user) > 15:
    print ("Username too long. Username must be between 8 and 15 characters. Try again.")
    print()
  # username only alphanumeric characters
  elif user.isalnum() == False:
    print ("Username can only contain alphabetic and numeric characters. Try again.")
    print()
  # username first character cannot be digit
  elif user[0].isdigit() == True:
    print ("The first character cannot be a digit. Try again.")
    print()
  # username must contain at least one upper, one lower, one digit
  else:
    upper = 0
    lower = 0
    digit = 0
    for character in user:
      if character.isupper() == True:
        upper += 1
      elif character.islower() == True:
        lower += 1
      elif character.isdigit() == True:
        digit += 1
    if upper < 1:
      print ("Username must contain at least one uppercase character. Try again.")
      print()
    elif lower < 1:
      print ("Username must contain at least one lowercase character. Try again.")
      print()
    elif digit < 1:
      print ("Username must contain at least one digit character. Try again.")
      print()
    else:
      print ("Your username is valid!")
      break
