# Helen Li
# April 22, 2015
# Assignment #8: Part #1: Sieve of Eratosthenes

counter = 0

mylist = [0] * 1000

# 0 and 1 are not prime numbers
mylist[0] = 1
mylist[1] = 1

# Test to see if number is prime
for x in range(3, len(mylist)):
  if mylist[x] == 0:
    for y in range(2, x-1):
      if x % y == 0:
        mylist[x] = 1

# If prime, print 
for a in range(0, len(mylist)):
  if mylist[a] == 0:
    print (format(a, ">7d"), end="")
    counter += 1
    if counter == 10:
      print ("\n")
      counter = 0
      
