# Helen Li
# March 25, 2015
# Assignment #5: Problem #2a: Prime Number Finder

# This code prompts user to enter a positive number, which is then tested to
# see if it is prime or not

# Prompt user to enter a positive number
# 1 is technically not a prime number
while True:
    num = int(input("Enter a positive number to test: "))
    if num > 1:
        break
    elif num == 1:
        print ("1 is technically not a prime number. Try again.")
    else:
        print ("Invalid entry. Try again.")

print()

# Test to see if number is prime or not
# Do not continue as soon as a number can evenly divide into the test number
for number in range (2, num):
    if num % number == 0:
        print (number, "is a divisor of", num, "...stopping")
        print ()
        print (num, "is not a prime number.")
        break
    else:
        print (number, "is NOT a divisor of", num, "...continuing")

# Report test number as prime only after all potential divisors are tested
if num == 2:
    print (num, "is a prime number!")
elif num % number != 0:
    print ()
    print (num, "is a prime number!")
