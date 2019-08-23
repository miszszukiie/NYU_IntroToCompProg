# Helen Li
# February 23, 2015
# Assignment #3: Problem #1: Valid Triangle Tester

# This code prompts the user to enter 3 points on a coordinate plane, which will then calculate 
# the lengths of the 3 sides, and evaluates whether the triangle is valid or not valid

# prompt user to enter 3 points on coordinate plane
print ("Valid Triangle Tester")
p1x = float(input("Enter Point #1 - x position: "))
p1y = float(input("Enter Point #1 - y position: "))
p2x = float(input("Enter Point #2 - x position: "))
p2y = float(input("Enter Point #2 - y position: "))
p3x = float(input("Enter Point #3 - x position: "))
p3y = float(input("Enter Point #3 - y position: "))

# calculate lengths of the 3 sides
# format to two decimal places
side1 = ((p1x - p2x)**2 + (p1y - p2y)**2)**0.5
new_side1 = format(side1, ".2f")
side2 = ((p2x - p3x)**2 + (p2y - p3y)**2)**0.5
new_side2 = format(side2, ".2f")
side3 = ((p1x - p3x)**2 + (p1y - p3y)**2)**0.5
new_side3 = format(side3, ".2f")
print ()

# present lengths of 3 sides to user
print ("The length of each side of your test shape is:")
print ("Side 1:", new_side1)
print ("Side 2:", new_side2)
print ("Side 3:", new_side3)
print ()

# evaluate if the triangle is valid or not valid
if side1+side2 > side3 and side2+side3 > side1 and side1+side3 > side2:
   print ("This is a valid triangle!")
else:
   print ("This is not a valid triangle!")
