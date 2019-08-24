# Helen Li
# February 23, 2015
# Assignment #3: Problem #2: NYU Calendar Spring 2015

# This code prompts user to enter a month and day, which will then inform, if
# date is valid, if date is school holiday or not

# prompt user to enter month and day
month = int(input("Enter a month (1-12): "))
day = int(input("Enter a day (1-31): "))
print ()

# convert numeric months values to English equivalents
if month == 1:
   month_name = "January"
elif month == 2:
   month_name = "February"
elif month == 3:
   month_name = "March"
elif month == 4:
   month_name = "April"
elif month == 5:
   month_name = "May"
elif month == 6:
   month_name = "June"
elif month == 7:
   month_name = "July"
elif month == 8:
   month_name = "August"
elif month == 9:
   month_name = "September"
elif month == 10:
   month_name = "October"
elif month == 11:
   month_name = "November"
elif month == 12:
   month_name = "December"

# Semester is from 1/26 to 5/11
# check if date is valid or not
# 1/26 is first day of term, any dates before is before the term
# 5/11 is last day of term, any dates after is after the term
# 2/16 is Presidents' Day
# 3/16 - 3/22 is Spring Break
# otherwise, NYU is open
if month == 2 and day > 28 or month == 4 and day > 30 or month == 6 and day > 30 or month == 9 and day > 30 or month == 11 and day > 30:
   print ("Sorry, that is not a valid date.")
elif month < 1 or month > 12:
   print ("Sorry, that is not a valid date.")
elif day < 1 or day > 31:
   print ("Sorry, that is not a valid date.")
elif month == 1 and day == 26:
   print (month_name, day, "is the first day of the Spring 2015 term.")
elif month == 5 and day == 11:
   print (month_name, day, "is the last day of the Spring 2015 term.")
elif month == 2 and day == 16:
   print (month_name, day, "is Presidents' Day. NYU is not open on this day.")
elif month == 3 and day >= 16 and day <= 22:
   print (month_name, day, "is Spring Break. NYU is not open on this day.")
elif month == 1 and day < 26:
   print (month_name, day, "is before the Spring 2015 term.")
elif month >= 5 and day > 11 or month > 5:
   print (month_name, day, "is after the Spring 2015 term.")
else:
   print (month_name, day, "is not a holiday at NYU. NYU is open on this day.")
