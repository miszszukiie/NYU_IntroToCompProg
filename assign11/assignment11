# Helen Li
# May 11, 2015
# Assignment #11

# import turtle and random
import turtle
import random

# name the project
turtle.title("Landscape")

# set background color
turtle.bgcolor("#324567")

# set up screen size, and starting point
turtle.setup(500, 500, 0, 0)

# hide the cursor
turtle.hideturtle()

# input: receive the dimensions to draw the river - in a triangular shape
# processing: draw the river - as a triangle
# output: blue river is drawn
def river():
    # draw two diagonal lines

    # do not show drawing being drawn
    turtle.tracer(0)

    # set pen color to blue
    turtle.pencolor("blue")
    # pick up pen and move to desired location, put pen back down
    turtle.penup()
    turtle.goto(-300, -200)
    turtle.pendown()

    # set fill color to blue
    turtle.fillcolor("blue")
    turtle.begin_fill()

    # draw river as a triangle
    turtle.right(330)
    turtle.forward(670)

    turtle.left(200)
    turtle.forward(630)

    turtle.end_fill()

    turtle.update()

# input: receive the dimensions to draw the fishes
# processing: draw the fishes - bow-like
# output: fishes are drawn
def fish():
    # draw 3 fishes
    counter = 3

    # set list so locations do not repeat
    xposlist2 = []
    yposlist2 = []

    # do not show drawing being drawn
    turtle.tracer(0)

    turtle.pensize(1)
    
    while counter > 0:
        # randomly choose location
        xpos2 = random.randrange(-240, -170, 20)
        ypos2 = random.randrange(-220, -180, 20)

        # if location is new
        if xpos2 not in xposlist2 or ypos2 not in yposlist2:
            xposlist2.append(xpos2)
            yposlist2.append(ypos2)

            # draw fishes
            turtle.penup()
            turtle.goto(xpos2, ypos2)
            turtle.pendown()
            turtle.setheading(120)
            turtle.pencolor("#8B8378")

            turtle.fillcolor("#8B8378")
            turtle.begin_fill()
                    
            turtle.forward(10)
            turtle.left(150)
            turtle.forward(15)
            turtle.left(150)
            turtle.forward(20)
            turtle.right(150)
            turtle.forward(20)


            turtle.end_fill()
            counter -=1
            
        else:
            xpos2 = random.randrange(-240, -170, 20)
            ypos2 = random.randrange(-220, -180, 20)
            

        turtle.update()

# input: receive the dimensions to draw the house
# processing: draw the house - triangular ceiling, square body, rectangular door
# output: house is drawn   
def house():
    # draw house
    turtle.penup()
    turtle.goto(70, -150)
    turtle.pendown()
    turtle.setheading(0)
    turtle.left(30)

    turtle.pencolor("black")

    turtle.fillcolor("#8B7355")
    turtle.begin_fill()

    # draw the triangular ceiling
    for tri in range(1, 3):
        turtle.forward(75)
        turtle.right(180/3)

    turtle.end_fill()

    turtle.fillcolor("#8B7355")
    turtle.begin_fill()

    # draw the square body
    for squ in range(2):
        turtle.forward(70)
        turtle.right(360/4)
        turtle.forward(129)
        turtle.right(360/4)

    turtle.end_fill()

    turtle.penup()
    turtle.goto(100, -220)
    turtle.pendown()
    turtle.setheading(90)

    turtle.fillcolor("black")
    turtle.begin_fill()

    # draw the rectangular door
    for squ2 in range(2):
        turtle.forward(40)
        turtle.right(360/4)
        turtle.forward(25)
        turtle.right(360/4)

    turtle.end_fill()

# input: receive the dimensions to draw the birds
# processing: draw the birds - two triangles
# output: birdss are drawn
def birds():
    # draw x amount of birds

    xposlist1 = []
    yposlist1 = []
    
    turtle.tracer(0)

    # ask user for number of birds to draw
    birdnum = int(input("How many birds to draw? "))

    while birdnum > 0:
        turtle.pensize(1)

        xpos1 = random.randrange(-200, 200, 30)
        ypos1 = random.randrange(-100, 220, 30)

        # draw birds in new locations
        if xpos1 not in xposlist1 or ypos1 not in yposlist1:
            xposlist1.append(xpos1)
            yposlist1.append(ypos1)


            turtle.penup()
            turtle.goto(xpos1, ypos1)
            turtle.pendown()
            turtle.setheading(0)
            turtle.left(30)

            # draw two triangles for birds
            for i in range(2):
                turtle.pencolor("#ddd")

                turtle.fillcolor("#ddd")
                turtle.begin_fill()

                turtle.forward(10)
                turtle.right(180/3)
                turtle.forward(10)
                turtle.right(180/3)
                turtle.end_fill()
            
            birdnum -= 1
        else:
            xpos1 = random.randrange(-200, 200, 30)
            ypos1 = random.randrange(-100, 220, 30)
            

    turtle.update()

# input: receive the dimensions to draw the stars
# processing: draw the stars
# output: stars are drawn
def stars():
    # draw stars

    xposlist = []
    yposlist = []
    
    turtle.tracer(0)

    # ask user for # of stars to draw
    starnum = int(input("How many stars to draw? "))

    while starnum > 0:
        turtle.pensize(7)

        xpos = random.randrange(-220, 220, 40)
        ypos = random.randrange(100, 220, 40)

        # draw stars in new location
        if xpos not in xposlist or ypos not in yposlist:
            xposlist.append(xpos)
            yposlist.append(ypos)

            turtle.penup()
            turtle.goto(xpos, ypos)
            turtle.pendown()
            turtle.pencolor("yellow")

            turtle.fillcolor("yellow")
            turtle.begin_fill()

            # draw stars
            for i in range(5):
                turtle.forward(20)
                turtle.right(144)

            turtle.end_fill()
            starnum -= 1
        else:
            xpos = random.randrange(-220, 220, 40)
            ypos = random.randrange(100, 220, 40)
            

    turtle.update()

# call functions
river()
fish()
house()
stars()
birds()
