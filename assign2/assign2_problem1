# Helen Li
# February 11, 2015
# Assignment #2: Problem #1: Dynamic Tip Calculator

# code will ask user how much was the bill, how much tip user wants to pay, and will generate tips 
# to pay and the total bill to pay

# ask how much was bill
bill = float(input("How much was your bill? (Enter as a number without dollar signs or commas): "))

# bill with 2 decimal places
new_bill = format(bill, ".2f")

# ask for how much tip user wants to pay
tips_per = int(input("How much tip would you like to leave? (Enter just a number): "))

# convert to decimal, to 2 places
tips = float(bill * (tips_per / 100))
new_tips = format(tips, ".2f")

# calculate total, to 2 decimal places
total = float(bill + tips)
new_total = format(total, ".2f")

print ()
print ("Bill: ", "$", new_bill, sep="") # the bill amount
print ("Tips percentage: ", tips_per, "%", sep="") # percentage of tips
print ("You need to leave $", new_tips, " as a tip.", sep="") # how much tip to leave
print ("Your total bill will be $", new_total, ".", sep="") # total bill
