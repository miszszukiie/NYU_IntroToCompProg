# Helen Li
# April 22, 2015
# Assignment #8: Part #4

import random

# For any given integer, determine and return whether it is odd or even.
def oddOrEven(num):
    if num % 2 == 0:
        return ("even")
    else:
        return ("odd")

def sample1():
    print ("This program will evaluate if a number is even or odd.")
    number = int(input("Enter a number: "))
    x = oddOrEven(number)
    if x == "even":
        print (number, "is even.")
    else:
        print (number, "is odd.")

sample1()
print ()

# For any given (small) number, print a square of asterisks with the length of each side equal to the given number.
def square(height):
    print (height * "*")
    for h in range(1, height-1):
        print ("*" + (height-2)*" " + "*")
    print (height * "*")

def sample2():
    print ("This program will print a square of asterisks.")
    a = int(input("Enter a small number: "))
    square(a)

sample2()
print ()

# Simulate tossing a coin and return the result.
def cointoss(z):
    if z == 1:
        return ("heads")
    else:
        return ("tails")

def sample3():
    print ("This program is a coin toss program.")
    print ("Tossing the coin...")
    print ()
    y = random.randint(1,2)
    b = cointoss(y)
    if b == "heads":
        print ("You got heads.")
    else:
        print ("You got tails.")

sample3()
print ()

# Given a number from 1-12, return the name of the appropriate month
def month(s):
    if s == 1:
        return ("January")
    elif s == 2:
        return ("February")
    elif s == 3:
        return ("March")
    elif s == 4:
        return ("April")
    elif s == 5:
        return ("May")
    elif s == 6:
        return ("June")
    elif s == 7:
        return ("July")
    elif s == 8:
        return ("August")
    elif s == 9:
        return ("September")
    elif s == 10:
        return ("October")
    elif s == 11:
        return ("November")
    else:
        return ("December")

def sample4():
    print ("This program will give the month name.")
    m = int(input("Enter a number between 1 and 12: "))
    n = month(m)
    print ("Month #", m, "is", n)

sample4()
print ()

# Given 5 numbers, return the average (mean)
def average(c, d, e, f, g):
    j = c+d+e+f+g
    aver = j/5
    return aver

def sample5():
    print ("This program will find the average of five numbers.")
    print ("Please enter 5 numbers")
    num1 = float(input("Enter one number: "))
    num2 = float(input("Enter one number: "))
    num3 = float(input("Enter one number: "))
    num4 = float(input("Enter one number: "))
    num5 = float(input("Enter one number: "))
    k = average(num1,num2,num3,num4,num5)
    print ("The average is", format(k, ".2f"))

sample5()
