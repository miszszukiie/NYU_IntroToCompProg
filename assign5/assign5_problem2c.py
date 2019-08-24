# Helen Li
# March 25, 2015
# Assignment #5: Problem #2c: Custom Number Range

# This code tests for all prime numbers in range chosen by user, and presented
# with 10 numbers per line

# Set counter for values per line
counter = 0

# Test range must be positive numbers
# End number must be greater than start number
while True:
    first = int(input("Start number - Enter a positive number: "))
    last = int(input("End number - Enter a positive number: "))
    if first <= 0 or last <= 0:
        print ("Start and end numbers must be positive. Try again.")
    elif last <= first:
        print ("End number must be greater than start number. Try again.")
    else:
        break

# 1 is technically not a prime number
if first == 1:
    first = 2

print ()
for p in range(first,last+1): # Range of numbers being tested
    for i in range(2,p): #Range between 2 and test value
        if p%i == 0:
            break
    else:
        print (format(p, "6d"), end="") # Format the numbers
        counter += 1
        if counter == 10: # Ten numbers per line
            print ()
            counter = 0
