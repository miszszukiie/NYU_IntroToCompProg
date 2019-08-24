# Helen Li
# April 10, 2015
# Assignment #7: Problem #1b

while True:
  user = input("Enter a username: ")
  # username 8 - 15 characters
  if len(user) < 8:
    print ("Username too short. Username must be between 8 and 15 characters. Try again.")
    print()
  elif len(user) > 15:
    print ("Username too long. Username must be between 8 and 15 characters. Try again.")
    print()
  # username alphanumeric characters only
  elif user.isalnum() == False:
    print ("Username can only contain alphabetic and numeric characters. Try again.")
    print()
  # username first character cannot be digit
  elif user[0].isdigit() == True:
    print ("The first character cannot be a digit. Try again.")
    print()
  # username must contain one upper, one lower, one digit
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
      
print()

while True:
  password = input("Enter a password: ")
  # password must be at least 8 characters
  if len(password) < 8:
    print ("Password too short. Password must be at least 8 characters. Try again.")
    print()
  # password cannot contain username
  elif user in password:
    print ("You cannot use your username as part of your password. Try again.")
    print()
  # password must contain one upper, one lower, one digit, a selection of special characters
  else:
    upper1 = 0
    lower1 = 0
    digit1 = 0
    special = 0
    invalid = 0
    for character in password:
      if character.isupper() == True:
        upper1 += 1
      elif character.islower() == True:
        lower1 += 1
      elif character.isdigit() == True:
        digit1 += 1
      else:
        a = ord(character)
        if a >= 35 and a <= 38:
          special += 1
        else:
          invalid += 1
    if upper1 < 1:
      print ("Password must contain at least one uppercase character. Try again.")
      print()
    elif lower1 < 1:
      print ("Password must contain at least one lowercase character. Try again.")
      print()
    elif digit1 < 1:
      print ("Password must contain at least one digit character. Try again.")
      print()
    elif invalid >= 1:
      print ("Your password contains at least one invalid character. Try again.")
      print()
    elif special < 1:
      print ("Password must contain at least one special character (#, $, %, &). Try again.")
      print ()

    else:
      print ("Your password is valid!")
      break
