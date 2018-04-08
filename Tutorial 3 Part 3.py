
import turtle #import the turtle module
wn = turtle.Screen() # creates a graphics window
my_turtle = turtle.Turtle() # create a turtle named my_turtle
# my_turtle.forward(...< you fill in some amount here>)#go forward by amount my_turtle.left(90) # turn left by 90 degrees

def drawSquare(t):
    for i in range (0,101,10):
        t.forward(i)
        t.left(90)
        t.forward(i)
        t.left(90)

drawSquare(my_turtle)



#
# Inside the for loop:
# • draw two sides of the spiral at a time
# • then increase the size of the sides when it goes through the for loop
#     the next time by using the range() function that steps up by a specified increment
#     e.g. range(0, 101, 10) will produce numbers from 0, 10, 20, 30…100 (increments of 10)
# If you start with sides of minimum 0 and maximum 101 with an increase of 10 for each loop
#     your spiral would look like something like this:

wn.exitonclick() # wait for a user click on the canvas
