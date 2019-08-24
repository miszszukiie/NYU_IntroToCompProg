# Helen Li
# April 1, 2015
# Assignment #6

#import functions
import myfunctionsXC

import random

# counters for statistics
good = 0
addnum = 0
addgood = 0
subnum = 0
subgood = 0
mulnum = 0
mulgood = 0
divnum = 0
divgood = 0

# prompt user for # of attempts and validate
while True:
    attempts = int(input("How many problems would you like to attempt? "))
    if attempts < 1:
        print ("Invalid entry. Try again.")
    else:
        break

# prompt user for width of digits and validate
while True:
    wide = int(input("How wide would you like your digits to be? (5-10): "))
    if wide < 5 or wide > 10:
        print ("Invalid entry. Try again.")
    else:
        break

# ask user if want drill or not and validate
while True:
    drill = input("Would you like to activate 'drill' mode? yes or no? ")
    if drill == "no":

        print ()
        print ("Here we go!")
        print ()

        # repeat user's wanted # of attempts
        for x in range (1, attempts+1):
            print ("What is ........")
            print()
            num1 = random.randint(0, 9) # pick a random integer for first num
            ops = ("+", "-", "*", "/") # the operations for the problems
            oper = random.choice(ops) # randomly choose one of the operators
            num2 = random.randint(0, 9) # pick a second number
            # if operation is divide, must yield whole number
            # cannot divide by 0
            if oper == "/":
                while True:
                    if num1 % num2 != 0:
                        num1 = random.randint(0,9)
                        num2 = random.randint(0,9)
                    elif num2 == 0:
                        num1 = random.randint(0,9)
                        num2 = random.randint(0,9)                        
                    else:
                        break

            # print number chosen
            if num1 == 0:
                myfunctionsXC.number_0(wide)
            elif num1 == 1:
                myfunctionsXC.number_1(wide)
            elif num1 == 2:
                myfunctionsXC.number_2(wide)
            elif num1 == 3:
                myfunctionsXC.number_3(wide)
            elif num1 == 4:
                myfunctionsXC.number_4(wide)
            elif num1 == 5:
                myfunctionsXC.number_5(wide)
            elif num1 == 6:
                myfunctionsXC.number_6(wide)
            elif num1 == 7:
                myfunctionsXC.number_7(wide)
            elif num1 == 8:
                myfunctionsXC.number_8(wide)
            elif num1 == 9:
                myfunctionsXC.number_9(wide)
            print()

            # print operation chosen
            # count amount of times operations occur
            if oper == "+":
                myfunctionsXC.plus(wide)
                addnum += 1
            elif oper == "-":
                myfunctionsXC.minus(wide)
                subnum += 1
            elif oper == "*":
                myfunctionsXC.multi(wide)
                mulnum += 1
            elif oper == "/":
                myfunctionsXC.divid(wide)
                divnum += 1
            print()

            # print number chosen
            if num2 == 0:
                myfunctionsXC.number_0(wide)
            elif num2 == 1:
                myfunctionsXC.number_1(wide)
            elif num2 == 2:
                myfunctionsXC.number_2(wide)
            elif num2 == 3:
                myfunctionsXC.number_3(wide)
            elif num2 == 4:
                myfunctionsXC.number_4(wide)
            elif num2 == 5:
                myfunctionsXC.number_5(wide)
            elif num2 == 6:
                myfunctionsXC.number_6(wide)
            elif num2 == 7:
                myfunctionsXC.number_7(wide)
            elif num2 == 8:
                myfunctionsXC.number_8(wide)
            elif num2 == 9:
                myfunctionsXC.number_9(wide)

            print()

            # prompt user for an answer
            # check answer
            ans = int(input("= "))
            answ = myfunctionsXC.check_answer(num1, num2, ans, oper)
            print()
            # if answer is correct, keep count
            # otherwise, tell user it's incorrect
            if answ == True:
                print ("Correct!")
                good += 1
                if oper == "+":
                    addgood += 1
                elif oper == "-":
                    subgood += 1
                elif oper == "*":
                    mulgood += 1
                elif oper == "/":
                    divgood += 1
            else:
                print ("Incorrect!")
            print()

        # tell user the statistics
        print ("You got", good, "out of", attempts, "problems correct!")
        print ()
        while True:
            # if operation was presented, show stats
            # otherwise, say no problems presented
            if addnum > 0:
                print ("Total addition problems presented:", addnum)
                print ("Correct addition problems:", addgood, "(", addgood/addnum*100, "% )")
                break
            else:
                print ("No addition problems presented")
                break
        print ()
        while True:
            if subnum > 0:
                print ("Total subtraction problems presented:", subnum)
                print ("Correct subtraction problems:", subgood, "(", subgood/subnum*100, "% )")
                break
            else:
                print ("No subtraction problems presented")
                break
        print ()
        while True:
            if mulnum > 0:
                print ("Total multiplication problems presented:", mulnum)
                print ("Correct multiplication problems:", mulgood, "(", mulgood/mulnum*100, "% )")
                break
            else:
                print ("No multiplication problems presented")
                break
        print ()
        while True:
            if divnum > 0:
                print ("Total division problems presented:", divnum)
                print ("Correct division problems:", divgood, "(", divgood/divnum*100, "% )")
                break
            else:
                print ("No division problems presented")
                break
        break

    # if user wants to enter drill mode
    elif drill == "yes":

        print ()
        print ("Here we go!")
        print ()

        for x in range (1, attempts+1): # run # of times user chose
            print ("What is ........")
            print()
            num1 = random.randint(0, 9) # pick random number
            ops = ("+", "-", "*", "/") # operations possible
            oper = random.choice(ops) # choose operation randomly
            num2 = random.randint(0, 9) # pick random number

            # if operation is division, must yield whole number
            # num2 cannot be 0
            if oper == "/":
                while True:
                    if num1 % num2 != 0:
                        num1 = random.randint(0,9)
                        num2 = random.randint(0,9)
                    elif num2 == 0:
                        num1 = random.randint(0,9)
                        num2 = random.randint(0,9) 
                    else:
                        break

            # print number chosen
            if num1 == 0:
                myfunctionsXC.number_0(wide)
            elif num1 == 1:
                myfunctionsXC.number_1(wide)
            elif num1 == 2:
                myfunctionsXC.number_2(wide)
            elif num1 == 3:
                myfunctionsXC.number_3(wide)
            elif num1 == 4:
                myfunctionsXC.number_4(wide)
            elif num1 == 5:
                myfunctionsXC.number_5(wide)
            elif num1 == 6:
                myfunctionsXC.number_6(wide)
            elif num1 == 7:
                myfunctionsXC.number_7(wide)
            elif num1 == 8:
                myfunctionsXC.number_8(wide)
            elif num1 == 9:
                myfunctionsXC.number_9(wide)
            print()

            # print operator chosen
            # keep count
            if oper == "+":
                myfunctionsXC.plus(wide)
                addnum += 1
            elif oper == "-":
                myfunctionsXC.minus(wide)
                subnum += 1
            elif oper == "*":
                myfunctionsXC.multi(wide)
                mulnum += 1
            elif oper == "/":
                myfunctionsXC.divid(wide)
                divnum += 1
                
            print()

            # print number chosen
            if num2 == 0:
                myfunctionsXC.number_0(wide)
            elif num2 == 1:
                myfunctionsXC.number_1(wide)
            elif num2 == 2:
                myfunctionsXC.number_2(wide)
            elif num2 == 3:
                myfunctionsXC.number_3(wide)
            elif num2 == 4:
                myfunctionsXC.number_4(wide)
            elif num2 == 5:
                myfunctionsXC.number_5(wide)
            elif num2 == 6:
                myfunctionsXC.number_6(wide)
            elif num2 == 7:
                myfunctionsXC.number_7(wide)
            elif num2 == 8:
                myfunctionsXC.number_8(wide)
            elif num2 == 9:
                myfunctionsXC.number_9(wide)

            print()

            # prompt user for answer
            # if answer incorrect, prompt user to retry
            # keep count of extra attempts
            while True:
                ans = int(input("= "))
                answ = myfunctionsXC.check_answer(num1, num2, ans, oper)
                print()
                if answ == True:
                    print ("Correct!")
                    print()
                    break
                else:
                    print ("Sorry! That's not correct. Try again.")
                    if oper == "+":
                        addgood += 1
                    elif oper == "-":
                        subgood += 1
                    elif oper == "*":
                        mulgood += 1
                    elif oper == "/":
                        divgood += 1
                    print()

        print ("Thanks for playing.")
        print ()

        # print stats
        # show amount of extra attempts
        # if no problems for that operation presented, tell user
        while True:
            if addnum > 0:
                print ("Total addition problems presented:", addnum)
                if addgood == 0:
                    print ("# of extra attempts:", addgood, "(perfect!)")
                elif addgood != 0:
                    print ("# of extra attempts:", addgood)
                break
            else:
                print ("No addition problems presented")
                break
        print ()
        while True:
            if subnum > 0:
                print ("Total subtraction problems presented:", subnum)
                if subgood == 0:
                    print ("# of extra attempts:", subgood, "(perfect!)")
                elif subgood != 0:
                    print ("# of extra attempts:", subgood)
                break

            else:
                print ("No subtraction problems presented")
                break
        print ()
        while True:
            if mulnum > 0:
                print ("Total multiplication problems presented:", mulnum)
                if mulgood == 0:
                    print ("# of extra attempts:", mulgood, "(perfect!)")
                elif mulgood != 0:
                    print ("# of extra attempts:", mulgood)
                break
            else:
                print ("No multiplication problems presented")
                break
        print ()
        while True:
            if divnum > 0:
                print ("Total division problems presented:", divnum)
                if divgood == 0:
                    print ("# of extra attempts:", divgood, "(perfect!)")
                elif divgood != 0:
                    print ("# of extra attempts:", divgood)
                break
            else:
                print ("No division problems presented")
                break
        
        break

    else:
        print ("Invalid entry. Try again.")
