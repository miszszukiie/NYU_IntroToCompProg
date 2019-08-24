def horizontal_line (width):
  print (width * "*")

def vertical_line (shift, height):
  for h in range(1, height+1):
     print (shift * " " + "*")

def two_vertical_lines(height, width):
  for h in range (1, height+1):
    print ("*" + (width-2) * " " + "*")

def number_0(width):
  horizontal_line(width)
  two_vertical_lines(3, width)
  horizontal_line(width)

def number_1(width):
  vertical_line(width-1,5)

def number_2(width):
  horizontal_line(width)
  vertical_line(width-1, 1)
  horizontal_line (width)
  horizontal_line (width-width+1)
  horizontal_line (width)

def number_3(width):
  horizontal_line(width)
  vertical_line(width-1, 1)
  horizontal_line(width)
  vertical_line(width-1, 1)
  horizontal_line(width)

def number_4(width):
  two_vertical_lines(2, width)
  horizontal_line(width)
  vertical_line(width-1, 2)

def number_5(width):
  horizontal_line(width)
  horizontal_line(width-width+1)
  horizontal_line(width)
  vertical_line(width-1, 1)
  horizontal_line(width)

def number_6(width):
  horizontal_line(width)
  horizontal_line(width-width+1)
  horizontal_line(width)
  two_vertical_lines(1, width)
  horizontal_line(width)

def number_7(width):
  horizontal_line(width)
  vertical_line(width-1, 4)

def number_8(width):
  horizontal_line(width)
  two_vertical_lines(1, width)
  horizontal_line(width)
  two_vertical_lines(1, width)
  horizontal_line(width)

def number_9(width):
  horizontal_line(width)
  two_vertical_lines(1, width)
  horizontal_line(width)
  vertical_line(width-1, 2)

def plus(width):
  vertical_line((width//2), 2)
  horizontal_line(width)
  vertical_line((width//2), 2)

def minus(width):
  print()
  print()
  horizontal_line(width)
  print()
  print()

def multi(width):
  two_vertical_lines(1, width)
  horizontal_line(width)
  vertical_line(width//2, 1)
  horizontal_line(width)
  two_vertical_lines(1, width)

def divid(width):
  vertical_line(width//2, 1)
  print()
  horizontal_line(width)
  print()
  vertical_line(width//2, 1)
  

def check_answer(number1,number2,answer,operator):
  if operator == "+":
    if number1 + number2 == answer:
      return True
  elif operator == "-":
    if number1 - number2 == answer:
      return True
  elif operator == "*":
    if number1 * number2 == answer:
      return True
  elif operator == "/":
    if number1 / number2 == answer:
      return True
